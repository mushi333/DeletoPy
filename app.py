"""
A python cmd prompt application to delete certain file types in your folder
"""

import os, glob


class Delete:
    def __init__(self, new_file_type):
        self.file_type = new_file_type
        self.glob_files = glob.glob('*' + new_file_type, recursive=True)

    def delete_file(self):
        # Exit if there are specified files found
        if not self.glob_files:
            print("No specified file type: *" + self.file_type + " was found")
            return

        # Loop through and delete each file found
        for file in self.glob_files:
            try:
                print("Found file: " + file)
                print("Attempting to delete file: " + file)
                os.remove(file)
                print("File: " + file + " was deleted succesfully")
            except OSError as exception:
                print("Error: %s : %s" % (file, exception.strerror))
                return


if __name__ == '__main__':
    file_type = "3.jpg"
    delete_instance = Delete(file_type)
    delete_instance.delete_file()
    print("Exiting app")
    exit()
