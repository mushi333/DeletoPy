"""
Version - 0.1
Author - Mujtaba Zahidi
Documentation Formatting - NumPy
Credit to https://linuxize.com/post/python-delete-files-and-directories/ for deletion logic.
"""

import os
import glob


class Delete:
    """
    A class to delete objects in a windows environment safely and efficiently.

    Attributes
    ----------
    final_files_exempted : str list
        A string list containing the files to be exempted from being deleted.

    glob_files: glob
        A glob object containing the objects/files to delete from

    Methods
    -------
    delete_file()
        Iterates through the glob files and deletes those that are not exempted

    """
    def __init__(self, new_file_type, new_files_exempted):
        """
        Combines the files exempted with the file type to create a new list of
        exempted files.

        Parameters
        ----------
        new_file_type : str
            String containing the .file format.
        new_files_exempted : str
            String list containing the files to not delete.

        Returns
        -------
        None
        """
        self.file_type = file_type
        self.final_files_exempted = []
        i = 0
        while i < len(new_files_exempted):
            self.final_files_exempted.append(new_files_exempted[i] + new_file_type)
            i += 1

        self.glob_files = glob.glob('*' + file_type, recursive=True)

    def delete_file(self):
        """
        Iterates through the glob files and deletes the non-exempted files

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # Exit if there are specified files found
        if not self.glob_files:
            print("No specified file type: *" + self.file_type + " was found")
            return

        # Loop through and delete each file found
        for file in self.glob_files:
            try:
                #TODO - Account for random length strings in files exempted
                num_last_n_char = len(self.final_files_exempted[0])
                if file[-num_last_n_char:] not in self.final_files_exempted:
                    print("Found file: " + file)
                    print("Attempting to delete file: " + file)
                    os.remove(file)
                    print("File: " + file + " was deleted successfully")
            except OSError as exception:
                print("Error: %s : %s" % (file, exception.strerror))
                return


if __name__ == '__main__':
    """
    Instructions:
    1. Change the file_type variable with the dot notation to the file type
    you want to delete.
    2. Insert the file ending strings into the files_exempted list. You can 
    add as many file endings as you want.
    3. An example could be using ".jpg" and ["1"]. With this only files ending
    with *1.jpg will be exempted from being deleted.
    """
    file_type = ".jpg"
    files_exempted = ["1", "2", "3"]
    delete_instance = Delete(file_type, files_exempted)
    delete_instance.delete_file()
    print("Exiting app")
    exit()
