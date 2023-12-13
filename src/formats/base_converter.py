from abc import ABC, abstractmethod

class BaseConverter(ABC):
    """
    Abstract base class for converters.
    """

    @abstractmethod
    def convert(self) -> str:
        """
        Abstract method to be implemented by subclasses for conversion logic.
        """
        pass
