import os

folder = "tmp"
file = "asdf.txt"
current_file_path = folder + "/" + file


class Delete:
    def __init__(self, file_path):
        self.file_path = file_path

    def delete_file(self):
        try:
            os.remove(self.file_path)
            print("File was successfully deleted")
        except FileNotFoundError:
            print("File does not exist or could not be found")


if __name__ == '__main__':
    delete_instance = Delete(current_file_path)
    delete_instance.delete_file()
    print("Exiting app")
    exit()
