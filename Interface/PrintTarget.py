import abc


class Target(metaclass=abc.ABCMeta):
    """
    Define the domain-specific interface that Client uses.
    """

    def __init__(self, adaptee):
        self._adaptee = adaptee

    @abc.abstractmethod
    def show(self):
        pass
