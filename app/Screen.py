from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, manager):
        self.manager = manager
        pass

    @abstractmethod
    def render(self):
        pass
