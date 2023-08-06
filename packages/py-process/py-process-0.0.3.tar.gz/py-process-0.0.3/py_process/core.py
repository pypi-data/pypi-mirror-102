from py_expression.core import Exp
from .base import *
import uuid
import threading
from multiprocessing import Process as ParallelProcess, process


class ProcessError(Exception):pass
class Object(object):pass
class ProcessSpec(object):pass
class Token(object):pass

"""
para la implementacion de python se usara un diccionario para almacenar
pero para la implementacion en go usar REDIS
"""
class TokenManager():
    def __init__(self):
        self._list={}

    def create(self,process,parent=None,node=None,status='running')->Token:
        token = Token()
        token.id= str(uuid.uuid4())
        token.process= process,
        token.mainId = parent.mainId if parent!= None else token
        token.parentId = parent.id if parent!= None else token
        token.status= status
        token.node = node
        token.childs = []
        return self.set(token)

    def set(self,token:Token):
        self._list[token.id] = token
        return token

    def get(self,key:str)-> Token:
        return self._list[key]

    def getChilds(self,parentId):
        parent = self.get(parentId)
        list = []
        for childId in parent.childs:
            list.append(self.get(childId))
        return list

    def update(self,token,data:dict):        
        for p in data:
            setattr(token, p,data[p])
        return self.set(token) 

    def delete(self,id:str):
        del self._list[id]

    def deleteChilds(self,parent):
        for childId in parent.childs:
            self.delete(childId)
        parent.childs = []
        return self.set(parent)    

class ProcessParser():
    def __init__(self,exp):        
        self.exp = exp   

class BpmParser(ProcessParser):
    def __init__(self,exp):
        super(BpmParser,self).__init__(exp) 

    def parse(self,spec:dict)-> ProcessSpec:
        process = ProcessSpec()
        process.name= spec['name']
        process.kind= spec['kind']
        # TODO: el bind deberia estar definido en la vista y no en el proceso. esta pendiente resolverlo
        process.bind = spec['bind'] if 'bind' in spec else []
        process.input=self.parseInput(spec) 
        process.declare=self.parseDeclare(spec)
        process.init=self.parseInit(spec)  
        process.vars=self.getVars(process)
        process.nodes = {}        
        for key in spec['nodes']:
            specNode=spec['nodes'][key]
            specNode['name']=key
            process.nodes[key] =self.parseNode(specNode)
        for key in process.nodes:
            node=process.nodes[key]
            node.entries= self.getEntries(key,process.nodes)
        return process    

    def parseInput(self,spec:dict):
        input = []
        if 'input' in spec:
            for p in spec['input']:
                param  = Object()
                param.name = p
                param.type = spec['input'][p]
                input.append(param)
        return input         

    def parseDeclare(self,spec:dict):
        declare = []
        if 'declare' in spec:
            for p in spec['declare']:
                param  = Object()
                param.name = p
                param.type = spec['declare'][p]
                declare.append(param)
        return declare 

    def parseInit(self,spec:dict):
        init = Object()
        if 'init' in spec:
            init.expression = self.exp.parse(spec['init']['exp']) 
        else:
            init.expression = None              
        return init                                

    def getVars(self,process:ProcessSpec):
        vars={}    
        for p in process.input:
            var = Object
            var.type=p.type
            var.isInput = True
            var.bind = True if p.name in process.bind else False
            vars[p.name]=var        
        for p in process.declare:
            var = Object
            var.type=p.type
            var.isInput = False
            var.bind = True if p.name in process.bind else False
            vars[p.name]=var
        return vars
    
    def getEntries(self,key,nodes):
        list = []
        for name in nodes:
            node=nodes[name]
            for t in node.transition:
                if t.target == key:
                    s = Object()
                    s.source= node
                    s.transition = t
                    list.append(s) 
        return list  

    def parseNode(self,spec):
        kind=spec['kind'] 
        if kind == 'start':return self.parseNodeStart(spec)
        elif kind == 'end':return self.parseNodeDefault(Object(),spec)           
        elif kind == 'task':return self.parseNodeTask(spec)
        elif kind == 'exclusiveGateway':return self.parseNodeGateway(spec)
        elif kind == 'inclusiveGateway':return self.parseNodeGateway(spec)
        elif kind == 'parallelGateway':return self.parseNodeGateway(spec)
        else: raise ProcessError('not found node kind :'+kind) 
     
    def parseNodeStart(self,spec):        
        node= self.parseNodeDefault(Object(),spec)
        node.expression = self.exp.parse(spec['exp']) if 'exp' in spec else None
        return node

    def parseNodeTask(self,spec):        
        node= self.parseNodeDefault(Object(),spec)
        node.expression= self.exp.parse(spec['exp']) if 'exp' in spec else None 
        return node

    def parseNodeGateway(self,spec):        
        node= self.parseNodeDefault(Object(),spec)
        node.key = spec['key'] if 'key' in spec else 'default'
        return node
    # TODO
    def parseNodeScript(self,spec):pass
    # TODO
    def parseNodeEventGateway(self,spec):pass
    # TODO
    def parseNodeSubProcess(self,spec):pass
    # TODO
    def parseNodeUserTask(self,spec):pass
    # TODO
    def parseNodeServiceTask(self,spec):pass
    # TODO
    def parseNodeEventSignal(self,spec):pass
    # TODO
    def parseNodeStartSignal(self,spec):pass
    # TODO
    def parseNodeRaiseSignal(self,spec):pass

    def parseNodeDefault(self,node,spec):
        node.name = spec['name']
        node.kind = spec['kind']
        node.transition = self.parseTransition(spec)
        return node

    def parseTransition(self,spec):
        transition = []
        if 'transition' in spec:
            for p in spec['transition']:
                item = Object()
                item.target = p['target']
                item.expression = self.exp.parse(p['exp']) if 'exp' in p else None
                transition.append(item)
        return transition        

class ProcessInstance:
    def __init__(self,parent:str,spec:ProcessSpec,context:dict,tokenManager:TokenManager,exp:Exp):
        self._id=None 
        self._parent=parent 
        self._context=context
        self._status='ready'
        self._spec=spec      
        self.tokenManager=tokenManager
        self.exp = exp 
        self.init()
        

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,value):
        self._id=value      
    @property
    def parent(self):
        return self._parent
    @property
    def spec(self):
        return self._spec        
    @property
    def context(self):
        return self._context

    def init(self):
        if self._spec.init.expression != None:
            self.exp.eval(self._spec.init.expression,self._context)

class BpmInstance(ProcessInstance):
    def __init__(self,parent:str,spec:ProcessSpec,context:dict,tokenManager:TokenManager,exp:Exp):
        super(BpmInstance,self).__init__(parent,spec,context,tokenManager,exp)   
    
    def start(self,parent=None):
        self._status='running'        
        
        starts = dict(filter(lambda p: p[1].kind == 'start', self._spec.nodes.items()))
        target=None
        for name in starts:
            p = starts[name]
            if p.expression != None:
                if self.exp.eval(p.expression,self._context):
                    target= name
                    break
            else:
                target= name
                break 

        if target == None: raise ProcessError('not found start node enabled')         
        token=self.tokenManager.create(process=self._spec.name,parent=parent,node=target)             
        self.execute(token)    


    def stop(self):
        self._status='stopping'
    def pause(self):
        self._status='pausing'   

    def execute(self,token):
        if self._status=='running':            
            node=self._spec.nodes[token.node]
            
            # self._context['__current']={'name':node.name ,'kind': node.kind } 

            if node.kind == 'start': self.nextNode(node,token)                 
            elif node.kind == 'task': self.executeTask(node,token)                    
            elif node.kind == 'end':  self.executeEnd(node,token)
            elif node.kind == 'exclusiveGateway':self.nextNode(node,token)
            elif node.kind == 'inclusiveGateway':self.executeInclusiveGateway(node,token)
            elif node.kind == 'parallelGateway':self.executeParallelGateway(node,token)

            else: raise ProcessError('not found node kind :'+node.kind)                          

            # self._context['__last']={'name':node.name ,'kind': node.kind}   
            
        elif self._status=='pausing':
            self._status='paused'   
        elif self._status=='stopping':
            self._status='stopped'
         
    def executeEnd(self,node,token):
        token=self.tokenManager.update(token,{'status':'end'})
    def executeTask(self,node,token):
        try:
            self.exp.eval(node.expression,self._context)
        except Exception as ex:
            print(ex)
            raise
        self.nextNode(node,token)  

    def executeInclusiveGateway(self,node,token):
        subToken=False
        pending = False
        if len(node.entries) > 1:
            if token.parentId != None:
                childs = self.tokenManager.getChilds(token.parentId) 
                subToken=True
                token=self.tokenManager.update(token,{'status':'end'})                
                for child in childs:
                    if child.id != token.id and child.status != 'end':
                        pending=True
                        break
        if subToken:
            if pending: return
            else: 
                parent = self.tokenManager.get(token.parentId) 
                parent = self.tokenManager.deleteChilds(parent)        
                token = parent
        targets=self.getTargets(node,onlyFirst=False)       
        if len(targets) == 1:
            token=self.tokenManager.update(token,{'node':targets[0],'status':'ready'}) 
            self.execute(token)
        else:
            for target in targets:
               child=self.tokenManager.create(process=self._spec.name,parent=token,node=target)
               token.childs.append(child)
            token=self.tokenManager.update(token,{'childs':token.childs,'status':'await'})   
            for child in token.childs:
                self.execute(token)

    # https://stackoverflow.com/questions/7207309/how-to-run-functions-in-parallel
    # https://stackoverflow.com/questions/1559125/string-arguments-in-python-multiprocessing 
    def executeParallelGateway(self,node,token):

        subToken=False
        pending = False
        if len(node.entries) > 1:
            if token.parentId != None:
                childs = self.tokenManager.getChilds(token.parentId) 
                if len(childs) > 1 :
                    subToken=True
                    token=self.tokenManager.update(token,{'status':'end'})
                    token.thread.join()               
                    for child in childs:
                        if child.id != token.id and child.status != 'end':
                            pending=True
                            break
        if subToken:
            if pending: return
            else:
                parent = self.tokenManager.get(token.parentId) 
                parent = self.tokenManager.deleteChilds(parent)        
                token=parent
        targets=self.getTargets(node,onlyFirst=False)       
        if len(targets) == 1:
            token=self.tokenManager.update(token,{'node':targets[0],'status':'ready'}) 
            self.execute(token)
        else:
            for target in targets:
               child=self.tokenManager.create(process=self._spec.name,parent=token,node=target)             
               thread =  ParallelProcess(target=self.execute ,args=(token,))
               child=self.tokenManager.update(child,{'thread':thread})
               token.childs.append(child)
            token=self.tokenManager.update(token,{'childs':token.childs,'status':'await'})     
            for child in token.childs:
                child.thread.start()
       
    def nextNode(self,node,token):
        targets=self.getTargets(node)
        token=self.tokenManager.update(token,{'node':targets[0] })              
        self.execute(token)        
        
    def getTargets(self,node,onlyFirst=True):
        targets=[]
        for p in node.transition:
            if p.expression != None:
                if self.exp.eval(p.expression,self._context):
                    targets.append(p.target)
                    if onlyFirst:break 
            else:
                targets.append(p.target)
                if onlyFirst:break

        if len(targets) == 0:
            raise ProcessError('node '+node.name+' not found targets')         
        return targets            
      
class ProcessInstanceFactory():
    def __init__(self,tokenManager:TokenManager,exp:Exp):
        self.tokenManager = tokenManager        
        self.exp = exp        

    def create(self,spec:ProcessSpec,context:dict,parent=None)-> ProcessInstance:
        pass

class BpmInstanceFactory(ProcessInstanceFactory):
    def __init__(self,tokenManager:TokenManager,exp:Exp):        
        super(BpmInstanceFactory,self).__init__(tokenManager,exp) 

    def create(self,spec:ProcessSpec,context:dict,parent=None)-> ProcessInstance:
        return BpmInstance(parent,spec,context,self.tokenManager,self.exp)

class Process(metaclass=Singleton):
    def __init__(self):
        self._parsers={}
        self._instanceFactory={}        
        self._specs={}
        self._instances= {}
        self.exp= Exp()
        self.tokenManager = TokenManager()
        self.init()

    def init(self):
        self.addParser('bpm',BpmParser)
        self.addInstanceFactory('bpm',BpmInstanceFactory) 

    def addParser(self,key:str,parser:ProcessParser):
        self._parsers[key] = parser(self.exp)  

    def addInstanceFactory(self,key:str,factory:ProcessInstanceFactory):
        self._instanceFactory[key] = factory(self.tokenManager,self.exp) 

    def addSpec(self,key:str,spec:dict)-> ProcessSpec:
        processSpec =self.parse(key,spec)
        self._specs[key] =processSpec
        return processSpec      

    def parse(self,key:str,spec:dict)-> ProcessSpec:
        spec['name'] = key
        kind =spec['kind']
        if kind not in self._parsers: raise ProcessError('not found parser kind :'+kind) 
        return self._parsers[kind].parse(spec)

    def getSpec(self,key:str)-> ProcessSpec:
        return self._specs[key] if key in self._specs else None 
    
    def createInstance(self,spec:ProcessSpec,context:dict,parent=None)-> ProcessInstance:
        if spec.kind not in self._instanceFactory: raise ProcessError('not found instance factory kind :'+spec.kind) 
        instance=self._instanceFactory[spec.kind].create(spec,context,parent)
        instance.id = str(uuid.uuid4())
        return instance
    
    def create(self,key:str,context:dict,parent=None)-> ProcessInstance:
        spec=self._specs[key]
        return self.createInstance(spec,context,parent) 

    # https://www.genbeta.com/desarrollo/multiprocesamiento-en-python-threads-a-fondo-introduccion
    # https://rico-schmidt.name/pymotw-3/threading/
    def start(self,instance:ProcessInstance,sync=False):        
        try:            
            thread = threading.Thread(target=self._process_start, args=(instance,))
            self._instances[instance.id]= {"instance":instance,"thread":thread }            
            if not sync: thread.setDaemon(True)            
            thread.start()
            if sync: thread.join()            
        except Exception as ex:
            print(ex)
            raise

    def stop(self,id):
        self._instances[id]['instance'].stop() 
    def pause(self,id):
        self._instances[id]['instance'].pause()     
    def _process_start(self,instance:ProcessInstance):
        instance.start()
    def getInstance(self,id)->ProcessInstance:
        return self._instances[id]