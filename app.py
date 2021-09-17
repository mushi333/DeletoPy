"""
A python cmd prompt application to delete certain file types in your folder
"""

import os, glob

# folder = "tmp"
# file_type = "asdf.txt"
# current_file_path = folder + "/" + file_type
global_file_type = "jpg"
global_glob_files = glob.glob('*.' + global_file_type, recursive=True)


class Delete:
    def __init__(self, glob_files):
        self.glob_files = glob_files

    def delete_file(self):
        if self.glob_files == []:
            print("No specified file type: " + global_file_type + " was found")
            return

        for file in self.glob_files:
            try:
                print("Found file: " + file)
                print("Attempting to delete file: " + file)
                os.remove(file)
                print("File: " + file + " was deleted succesfully")
            except OSError as exception:
                print("Error: %s : %s" % (file, exception.strerror))


if __name__ == '__main__':
    delete_instance = Delete(global_glob_files)
    delete_instance.delete_file()
    print("Exiting app")
    exit()
