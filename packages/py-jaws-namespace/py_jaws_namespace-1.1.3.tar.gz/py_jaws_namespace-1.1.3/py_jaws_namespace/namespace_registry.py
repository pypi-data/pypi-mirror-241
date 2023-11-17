import toml
import re

class NamespaceRegistry:
    __PYPROJECT_SECTION = "py_jaws_namespace"

    __instance = None
    __registry = dict()
    
    def __init__(self):
        return RuntimeError("Call get_namespace_ctx() instead")
    
    @classmethod
    def get_namespace_ctx(cls, namespace: str) -> dict:
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            cls.__instance.__load_registry()
            
        if namespace not in cls.__instance.__registry:
            return None

        return cls.__instance.__registry[namespace]
    
    def __load_registry(self):
        with open("pyproject.toml", 'r') as toml_file:
            data = toml.load(toml_file)
            if self.__PYPROJECT_SECTION in data:
                self.__registry = data[self.__PYPROJECT_SECTION]