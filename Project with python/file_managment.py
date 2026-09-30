import os
import shutil
from datetime import datetime


class FileManager:

    # 1. Create File
    def create_file(self):
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            print("File already exists!\n")
        else:
            open(filename, "w").close()
            print("File created successfully!\n")

    # 2. Write File
    def write_file(self):
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            data = input("Enter data to write: ")

            with open(filename, "w") as f:
                f.write(data)

            print("Data written successfully!\n")
        else:
            print("File not found!\n")

    # 3. Read File
    def read_file(self):
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            with open(filename, "r") as f:
                data = f.read()

            print("\n----- File Content -----")
            print(data)
            print("------------------------\n")
        else:
            print("File not found!\n")

    # 4. Append File
    def append_file(self):
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            data = input("Enter data to append: ")

            with open(filename, "a") as f:
                f.write("\n" + data)

            print("Data appended successfully!\n")
        else:
            print("File not found!\n")

    # 5. Delete File
    def delete_file(self):
        filename = input("Enter file name: ")

        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted successfully!\n")
        else:
            print("File not found!\n")

    # 6. Rename File
    def rename_file(self):
        old_name = input("Enter current file name: ")
        new_name = input("Enter new file name: ")

        if os.path.exists(old_name):
            if os.path.exists(new_name):
                print("New file name already exists!\n")
            else:
                os.rename(old_name, new_name)
                print("File renamed successfully!\n")
        else:
            print("File not found!\n")

    # 7. Copy File
    def copy_file(self):
        source = input("Enter source file name: ")
        destination = input("Enter destination file name: ")

        if os.path.exists(source):
            if os.path.exists(destination):
                print("Destination file already exists!\n")
            else:
                shutil.copy(source, destination)
                print("File copied successfully!\n")
        else:
            print("Source file not found!\n")

    # 8. Move File
    def move_file(self):
        source = input("Enter file name: ")
        destination = input("Enter destination path: ")

        if os.path.exists(source):
            try:
                shutil.move(source, destination)
                print("File moved successfully!\n")
            except Exception as e:
                print("Error:", e, "\n")
        else:
            print("File not found!\n")

    # 9. File Information
    def file_information(self):
        filename = input("Enter file name: ")

        if os.path.isfile(filename):

            size = os.path.getsize(filename)
            location = os.path.abspath(filename)
            modified_time = os.path.getmtime(filename)

            print("\n----- File Information -----")
            print("File Name:", os.path.basename(filename))
            print("File Size:", size, "bytes")
            print("File Location:", location)
            print(
                "Last Modified:",
                datetime.fromtimestamp(modified_time)
            )
            print("File Extension:", os.path.splitext(filename)[1])
            print("----------------------------\n")

        else:
            print("File not found!\n")

    # 10. Search File
    def search_file(self):
        filename = input("Enter file name to search: ")

        found = False

        for root, folders, files in os.walk("."):
            if filename in files:
                print("\nFile found!")
                print("Location:", os.path.abspath(
                    os.path.join(root, filename)
                ))
                found = True

        if not found:
            print("File not found!\n")
        else:
            print()

    # 11. List Files
    def list_files(self):
        files = os.listdir(".")

        print("\n----- Files and Folders -----")

        found = False

        for item in files:
            if os.path.isfile(item):
                print("[FILE]  ", item)
                found = True

        if not found:
            print("No files found.")

        print("-----------------------------\n")

    # 12. Create Folder
    def create_folder(self):
        foldername = input("Enter folder name: ")

        if os.path.exists(foldername):
            print("Folder already exists!\n")
        else:
            os.mkdir(foldername)
            print("Folder created successfully!\n")

    # 13. Delete Folder
    def delete_folder(self):
        foldername = input("Enter folder name: ")

        if os.path.isdir(foldername):

            try:
                os.rmdir(foldername)
                print("Folder deleted successfully!\n")
            except OSError:
                print("Folder is not empty!\n")

        else:
            print("Folder not found!\n")


# ================= MAIN PROGRAM =================

fm = FileManager()

while True:

    print("======================================")
    print("       FILE MANAGEMENT SYSTEM")
    print("======================================")

    print("1.  Create File")
    print("2.  Write File")
    print("3.  Read File")
    print("4.  Append File")
    print("5.  Delete File")
    print("6.  Rename File")
    print("7.  Copy File")
    print("8.  Move File")
    print("9.  File Information")
    print("10. Search File")
    print("11. List Files")
    print("12. Create Folder")
    print("13. Delete Folder")
    print("14. Exit")

    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        fm.create_file()

    elif choice == "2":
        fm.write_file()

    elif choice == "3":
        fm.read_file()

    elif choice == "4":
        fm.append_file()

    elif choice == "5":
        fm.delete_file()

    elif choice == "6":
        fm.rename_file()

    elif choice == "7":
        fm.copy_file()

    elif choice == "8":
        fm.move_file()

    elif choice == "9":
        fm.file_information()

    elif choice == "10":
        fm.search_file()

    elif choice == "11":
        fm.list_files()

    elif choice == "12":
        fm.create_folder()

    elif choice == "13":
        fm.delete_folder()

    elif choice == "14":
        print("\nExiting File Management System...")
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice! Please try again.\n")