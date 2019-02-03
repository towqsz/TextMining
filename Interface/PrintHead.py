from Interface.PrintTarget import Target


class PrintHead(Target):
    """
    Adapt the interface of Adaptee to the Target interface.
    """
    def __init__(self, adaptee):
        super(PrintHead, self).__init__(adaptee)
        self.show()

    def show(self):
        print(self._adaptee.head())
