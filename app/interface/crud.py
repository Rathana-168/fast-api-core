from abc import ABCMeta, abstractmethod

class CRUDInterface(metaclass=ABCMeta):
    
    @abstractmethod
    async def list(self):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def read(self):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def create(self):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def update(self):
        raise NotImplementedError()
    
    
    @abstractmethod
    async def delete(self):
        raise NotImplementedError()