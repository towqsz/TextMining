from FileManager import FileManager


class Data:
    def __init__(self):
        self.file = FileManager()
        self._text = self.file.file

    def set_data(self, file):
        self._text = file
        self.file.set_file(self._text)
