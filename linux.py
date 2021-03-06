import os

list_of_commands = ["1", "2", "3", "4", "5", "6", "exit"]
print('Welcome to the python file manager for Linux!\n')


def listDirectories():
    listdir = os.listdir(os.getcwd())
    for x in listdir:
        print(x)


while True:
    print("\n1.Open files/folders \n2.Write into file \n3.Create file/dir \n4.Copy and Paste \n5.Delete\n6.Rename\nexit"
          )
    need_com = input("Choose option: ")
    if need_com == "1":
        while True:
            listDirectories()
            need_dir = input("Type folder path or command: ")
            if need_dir == 'back':
                os.chdir('..')
            elif os.path.isdir(need_dir):
                os.popen('cd ' + need_dir)
                os.chdir(os.path.expandvars(need_dir))
                listDirectories()
            elif os.path.isfile(need_dir):
                os.system('cat ' + need_dir)
            elif need_dir == 'exit':
                break
            else:
                print("Folder not found")
    if need_com == "2":
        while True:
            res = input("Type file path: ")
            if os.path.isfile(res):
                write_res = input("Type text: ")
                os.system('echo ' + '"' + write_res + '" ' + '>> ' + res)
            elif res == "exit":
                break
            else:
                print("File not found")
    if need_com == '3':
        while True:
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.popen('cd ' + res)
                os.chdir(os.path.expandvars(res))
                file_or_dir = input("You want to create dir or file? ")
                if file_or_dir == 'file':
                    name_input = input("Type filename: ")
                    os.system('touch ' + name_input)
                if file_or_dir == 'dir':
                    name_input = input("Type dirname: ")
                    os.system('mkdir ' + name_input)
                    listDirectories()
            elif res == "exit":
                break
            else:
                print("Incorrect file path")
    if need_com == "4":
        while True:
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.chdir(os.path.expandvars(res))
                need_file = input("Type filename: ")
                if os.path.isfile(need_file):
                    copy_dir = input("Type path to copy: ")
                    if os.path.isdir(copy_dir):
                        os.system('cp ' + need_file + " " + copy_dir)
                        listDirectories()
            elif res == "exit":
                break
            else:
                print("Incorrect dir input")
    if need_com == "5":
        while True:
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.chdir(os.path.expandvars(res))
                listDirectories()
                need_file = input("Type filename to delete: ")
                if os.path.isfile(need_file):
                    os.system('rm ' + need_file)
                else:
                    print("It is not a file")
            elif res == "exit":
                break
            else:
                print("Incorrect file path")
    if need_com == "6":
        while True:
            res = input("Type file path: ")
            if os.path.isdir(res):
                os.popen('cd ' + res)
                listDirectories()
                res2 = input("Type filename: ")
                if os.path.isfile(res2):
                    res3 = input("Type new filename: ")
                    os.system('mv ' + res2 + " " + res3)
                    listDirectories()
            elif res == "exit":
                break
            else:
                print("file not found")
    if need_com == "exit":
        break
    if not (need_com in list_of_commands):
        print("Wrong input")

