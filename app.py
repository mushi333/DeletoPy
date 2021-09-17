"""
A python cmd prompt application to delete certain file types in your folder.

Credit to https://linuxize.com/post/python-delete-files-and-directories/ for deletion logic.
"""

import os, glob


class Delete:
    def __init__(self, new_file_type, new_files_exempted):
        # Append the files exempted and the file type to create a list of files to ignore
        self.final_files_exempted = []
        i = 0
        while i < len(new_files_exempted):
            self.final_files_exempted.append(new_files_exempted[i] + new_file_type)
            i += 1

        self.glob_files = glob.glob('*' + file_type, recursive=True)

    def delete_file(self):
        # Exit if there are specified files found
        if not self.glob_files:
            print("No specified file type: *" + self.file_type + " was found")
            return

        # Loop through and delete each file found
        for file in self.glob_files:
            try:
                if file not in self.final_files_exempted:
                    print("Found file: " + file)
                    print("Attempting to delete file: " + file)
                    os.remove(file)
                    print("File: " + file + " was deleted successfully")
            except OSError as exception:
                print("Error: %s : %s" % (file, exception.strerror))
                return


# Specifies the file type and exempted file endings then deletes those that are not exempted
if __name__ == '__main__':
    file_type = ".jpg"
    files_exempted = ["1", "2", "3"]
    delete_instance = Delete(file_type, files_exempted)
    delete_instance.delete_file()
    print("Exiting app")
    exit()
