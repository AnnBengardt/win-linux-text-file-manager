import platform

while True:
        if platform.system() == "Windows":
            exec(open("windows.py").read())
            break
        elif platform.system() == "Linux":
            exec(open("linux.py").read())
            break
        else:
            print("Your OS is not supported!")
