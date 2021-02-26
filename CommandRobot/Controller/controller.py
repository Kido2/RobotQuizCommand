from abc import ABC, abstractmethod


class Controller(ABC):
    # ABCAbstract Base Class
    @abstractmethod
    def executebot(self):
        pass
