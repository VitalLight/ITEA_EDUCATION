class File:
    def __init__(self, file_neme, path):
        file_name = input('вкажіть назву файлу'+'txt')
        self.file_name = file_name
        self.path = 'D:\\Python_ITed\\Lesson_11'

    def get_file_extension(self):
        pass

class Jsonfile(File):
    def open_file(self):

        pass

    def write_to_file(self):
        file_name = self.file_name
        path = self.path
        with open(f'{path}' + {file_name}, 'r') as f:
            text = f.read()
            print(text)

class Txtfile(File):
    pass