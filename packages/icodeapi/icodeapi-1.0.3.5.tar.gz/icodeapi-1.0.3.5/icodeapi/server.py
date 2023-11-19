'''
icodeapi server.
This module can structure IcodeShequ bots.
'''
from . import *
from typing import Callable, Awaitable, Union
from types import FunctionType
import inspect, asyncio

class IcodeServer:
    __api : AsyncIcodeAPI
    __events : list[Awaitable]
    __tocomment : list[Awaitable]
    __tolike : list[Awaitable]
    debug : bool
    running : bool
    ban : set[str]
    results : list[list[list]] # 最外面的一层表示所有从开始run以来所有的返回值，第二层表示一次检测(while一次)获得的所有返回值，第三层是例如self.CheckMessage这样的函数的返回值，由于一般是个列表就把它标注为列表了
    
    def __init__(self, api : AsyncIcodeAPI, ban : set[str] = set(), debug : bool = True) -> None:
        '''Create a IcodeShequ bot.
        need a `AsyncIcodeAPI` object.'''
        self.__api = api
        self.__events = []
        self.__tocomment = []
        self.__tolike = []
        self.ban = ban
        self.running = False
        self.debug = debug
        self.results = []
    
    def __GetKwargs(self, func : Callable, allparameters : list[str]) -> dict:
        kwargs = {}
        parameters = inspect.signature(func).parameters
        for i, j in parameters.items():
            if i in allparameters:
                kwargs[i] = None
        return kwargs
    
    async def login(self, newCookie : str = None):
        await self.__api.login(newCookie)
        self.ban.add(self.__api.getInfo().get('userId'))
    
    async def closeBot(self):
        await self.__api.closeClient()
        
    def getInfo(self):
        return self.__api.getInfo()
    
    def getLoginStatus(self):
        return self.__api.getLoginStatus()
    
    def comment(self, workId : str, content : str):
        '''
        Left bot comment a work.  
        Don't use `AsyncIcodeAPI.comment`, errors may occur due to comment time limits.
        '''
        self.__tocomment.append(self.__api.comment(workId, content))
        
    def like(self, workId : str, mode : int = 1):
        '''
        Left bot like a work.  
        Don't use `AsyncIcodeAPI.like`, errors may occur due to like time limits.
        '''
        self.__tolike.append(self.__api.like(workId, mode))
        
    def reply(self, content : str, commentId : int, replyId : int = None):
        '''
        Left bot reply a comment or another reply.  
        Don't use `AsyncIcodeAPI.reply`, errors may occur due to comment time limits.
        '''
        self.__tocomment.append(self.__api.reply(content, commentId, replyId))
        
    async def fastReply(self, userId : str, content : str) -> None:
        '''
        A fast way to comment in a user's first work.

        Need a userId and the comment's content.
        '''
        works = await self.__api.getPersonWorks(userId, getNum = 1)
        assert works, 'The user has no work'
        works = works[0]
        self.__tocomment.append(self.__api.comment(works.get('id'), content))
    
    def cancel(self, func : Callable) -> None:
        '''Cancel a event'''
        try:
            i = self.__events.index(func)
        except:
            raise ValueError('Function is not in events')
        self.__events.pop(i)
        
    async def __Comment(self):
        i = 0
        length = len(self.__tocomment)
        while i < length:
            await asyncio.sleep(5.1)
            await self.__tocomment[i]
            length = len(self.__tocomment)
            i += 1
        self.__tocomment = []
            
    async def __Like(self):
        j = 0
        length = len(self.__tolike)
        while j < length: # 不使用for可以实时检测新的所需等待操作，不会误删（alpha 0.5新优化）
            await asyncio.sleep(3.1)
            await self.__tolike[j]
            length = len(self.__tolike)
            j += 1
        self.__tolike = []
        
    async def __returnAValue(value : any) -> any:
        return value
        
    def __debugging(self, func : Callable, callerFunc : Awaitable, callerFuncName : str, content : str):
        if self.debug:
            print('\nNew Excuting Log:')
            print(f'Bot: {(info := self.getInfo()).get("userId")} ({info.get("name")})')
            print(f'Be Called Function info: {func.__name__} {func}')
            print(f'Function Caller: {callerFunc.__name__}({callerFuncName}) {callerFunc}')
            print(f'Running Status: {self.running}')
            print(content)
        
    def CheckMessage(self,
                        workList : list[str] | None = None,
                        checkFunc : Callable[[str, str], bool] = (lambda x, y : True),
                        autoRead : bool = True,
                        checkRead : bool = True,
                        checkNum : int = 30,
                        name : any = None) -> Callable[[Awaitable[[str, str]]], Awaitable[list]]:
        '''
        Listen to the messages in messages hub, and call `checkFunc`. if `checkFunc` return True, execute the corresponding function.

        Goto [https://xbzstudio.github.io/_book/Server.html](https://xbzstudio.github.io/_book/Server.html) to learn more.
        '''
        def outside(func : Callable[[str, str, AsyncIcodeAPI], any]) -> Awaitable[list]:
            async def inner() -> list:
                api = self.__api
                msgs = []
                gotMsgs = await api.getMessages(getNum = checkNum)
                gotMsgs = [i for i in gotMsgs if (True if not workList else (False if i.get('worksId') in workList else True))]
                gotMsgs = [i for i in gotMsgs if (not i.get('actionUserId') in self.ban) and (not i.get('haveRead'))]
                if not isinstance(checkFunc, FunctionType):
                    raise TypeError('checkFunc must be function or awaitable.')
                if not isinstance(func, FunctionType):
                    raise TypeError('func must be function or awaitable.')
                if inspect.iscoroutinefunction(checkFunc):
                    coros = [checkFunc(i.get('content'), i.get('actionUserId')) for i in gotMsgs]
                    msgs = await asyncio.gather(*coros)
                else:
                    msgs = list(
                        map(checkFunc, [i['content'] for i in gotMsgs], [j['actionUserId'] for j in gotMsgs])
                    )
                msgs = [gotMsgs[i] for i in range(len(gotMsgs)) if msgs[i]]
                if msgs == []:
                    return []
                self.__debugging(func, self.CheckMessage, name, 'Start to call functions.')
                kwargs = self.__GetKwargs(func, ['content', 'userId', 'api', 'bot'])
                if 'api' in kwargs:
                    kwargs['api'] = api
                if 'bot' in kwargs:
                    kwargs['bot'] = self
                if inspect.iscoroutinefunction(func):
                    coros = []
                    for i in msgs:
                        if 'content' in kwargs:
                            kwargs['content'] = i.get('content')
                        if 'userId' in kwargs:
                            kwargs['userId'] = i.get('actionUserId')
                        coros.append(func(**kwargs))
                    results = await asyncio.gather(*coros)
                    results += [self.CheckMessage, name]
                else:
                    results = []
                    for i in msgs:
                        if 'content' in kwargs:
                            kwargs['content'] = i.get('content')
                        if 'userId' in kwargs:
                            kwargs['userId'] = i.get('actionUserId')
                        results.append(func(**kwargs))
                    results += [self.CheckMessage, name]
                self.__debugging(func, self.CheckMessage, name, 'Finish to call functions.')
                msgIds = [i.get('id') for i in msgs]
                if autoRead:
                    coros = [self.__api.readMessage(i) for i in msgIds]
                    await asyncio.gather(*coros)
                return results
            self.__events.append(inner)
            return inner
        return outside
    
    def CheckWork(self, workId : str,
                    addBrowseNum : bool = False,
                    checkFunc : Callable | None = (lambda **kwargs : bool(kwargs)),
                    name : str = None) -> Callable[[Callable], Awaitable]:
        '''
        Listen to the work data, and call `checkFunc`. if `checkFunc` return True, execute the corresponding function.

        Goto [https://xbzstudio.github.io/_book/Server.html](https://xbzstudio.github.io/_book/Server.html) to learn more.
        '''
        def outside(func : Callable) -> Awaitable:
            async def inner() -> list:
                if not isinstance(func, FunctionType):
                    raise TypeError('func must be function or awaitable.')
                if not isinstance(checkFunc, FunctionType):
                    raise TypeError('checkFunc must be function or awaitable.')
                api = self.__api
                kwargs = self.__GetKwargs(func, ['detail', 'submitInfo', 'comments', 'moreWorks', 'api', 'bot'])
                coros = []
                n = 0
                if 'detail' in kwargs:
                    kwargs['detail'] = n
                    coros.append(api.getWorkDetail(workId, addBrowseNum))
                    n += 1
                if 'submitInfo' in kwargs:
                    kwargs['submitInfo'] = n
                    coros.append(api.getWorkSubmitInfo(workId))
                    n += 1
                if 'comments' in kwargs:
                    kwargs['comments'] = n
                    coros.append(api.getWorkComments(workId, getNum = 30))
                    n += 1
                if 'moreWorks' in kwargs:
                    kwargs['moreWorks'] = n
                    coros.append(api.getMoreWorks(workId = workId))
                    n += 1
                temp = []
                if 'api' in kwargs:
                    kwargs['api'] = n
                    temp += [api]
                    n +=1
                if 'bot' in kwargs:
                    kwargs['bot'] = n
                    temp += [self]
                    n +=1
                results = await asyncio.gather(* coros)
                results += temp
                kwargs = {i : results[kwargs.get(i)] for i in kwargs}
                if not checkFunc:
                    self.__debugging(func, self.CheckWork, name, 'Start to call function')
                    if inspect.iscoroutinefunction(func):
                        result = await func(**kwargs)
                    else:
                        result = func(**kwargs)
                else:
                    if inspect.iscoroutinefunction(checkFunc):
                        allow = await checkFunc(**kwargs)
                    else:
                        allow = checkFunc(**kwargs)
                    if allow:
                        self.__debugging(func, self.CheckWork, name, 'Start to call function')
                        if inspect.iscoroutinefunction(func):
                            result = await func(**kwargs)
                        else:
                            result = func(**kwargs)
                    else:
                        return []
                self.__debugging(func, self.CheckWork, name, 'Finish to call function')
                return [result, self.CheckWork, name]
            self.__events.append(inner)
            return inner
        return outside
    
    def CheckPerson(self, userId : str,
                    checkFunc : Callable | None = (lambda **kwargs : True),
                    name : str | None = None) -> Callable[[Callable], Awaitable]:
        '''
        Listen to the user data, and call `checkFunc`. if `checkFunc` return True, execute the corresponding function.

        Goto [https://xbzstudio.github.io/_book/Server.html](https://xbzstudio.github.io/_book/Server.html) to learn more.
        '''
        def outside (func : Callable) -> Awaitable:
            async def inner():
                if not isinstance(func, FunctionType):
                    raise TypeError('func must be function or awaitable.')
                if not isinstance(checkFunc, FunctionType):
                    raise TypeError('checkFunc must be function or awaitable.')
                api = self.__api
                kwargs = self.__GetKwargs(func, ['info', 'works', 'enshrines', 'api', 'bot'])
                coros, temp, n = [], [], 0
                if 'info' in kwargs:
                    coros.append(api.getPersonInfo(userId))
                    kwargs['info'] = n; n+=1
                if 'works' in kwargs:
                    coros.append(api.getPersonWorks(userId, getNum = 30))
                    kwargs['works'] = n; n += 1
                if 'enshrines' in kwargs:
                    coros.append(api.getPersonEnshrines(userId, getNum = 100000))
                    kwargs['enshrines'] = n; n+=1
                if 'api' in kwargs:
                    kwargs['api'] = n; n+=1
                    temp += [api]
                if 'bot' in kwargs:
                    kwargs['bot'] = n; n+=1
                    temp += [self]
                results = await asyncio.gather(* coros)
                results += temp
                kwargs = {i : results[kwargs[i]] for i in kwargs}
                if not checkFunc:
                    self.__debugging(func, self.CheckPerson, name, 'Start to call function')
                    if inspect.iscoroutinefunction(func):
                        result = await func(**kwargs)
                    else:
                        result = func(**kwargs)
                else:
                    if inspect.iscoroutinefunction(checkFunc):
                        allow = await checkFunc(**kwargs)
                    else:
                        allow = checkFunc(**kwargs)
                    if allow:
                        self.__debugging(func, self.CheckPerson, name, 'Start to call function')
                        if inspect.iscoroutinefunction(func):
                            result = await func(**kwargs)
                        else:
                            result = func(**kwargs)
                    else:
                        return []
                return [result, self.CheckPerson, name]
            self.__events.append(inner)
            return inner
        return outside
    
    async def run(self):
        '''Start listening'''
        self.running = True
        self.results = []
        print(f'Start Running: Bot {self.getInfo().get("userId")}')
        while self.running:
            coros = [i() for i in self.__events]
            coros += [self.__Comment(), self.__Like()]
            results = await asyncio.gather(*coros) 
            results = [i for i in results if i] # 一般在判断为不需要执行操作的时候，返回空列表或任何为假的值，例如CheckMessage的[]，可以用这个判断
            self.results += [results]
        self.running = False
        print(f'Stop Running: Bot {self.getInfo().get("userId")}')
        
class ServerPool:
    __servers : list
    
    def __init__(self, *servers : IcodeServer):
        '''ServerPool, you can put all the `IcodeServer` object into the pool, and manage them.'''
        self.__servers = servers
    
    async def addAPI(self, * api : AsyncIcodeAPI):
        '''
        Add some API to pool.

        The function will turn the APIs into servers.
        '''
        newServers = [IcodeServer(i) for i in api]
        self.__servers += newServers
        await self.login()
        
    async def addServers(self, * servers : IcodeServer):
        '''Add some servers to pool.'''
        self.__servers += servers
        await self.login()
    
    async def login(self):
        coros = [i.login() for i in self.__servers]
        await asyncio.gather(* coros)
        
    async def closePool(self):
        coros = [i.closeBot() for i in self.__servers]
        await asyncio.gather(* coros)
        
    async def RunServers(self):
        '''Run all the servers in pool'''
        coros = [i.run() for i in self.__servers]
        await asyncio.gather(* coros)
        
    def stopRunning(self):
        '''stop running'''
        for i in self.__servers:
            i.running = False

def RunServer(server : IcodeServer) -> None:
    '''
    Run a server

    This function will create a new asyncio eventloop, and finally close it.
    '''
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(server.login())
        loop.run_until_complete(server.run())
    finally:
        loop.run_until_complete(server.closeBot())
        loop.close()

'''
pass
'''
