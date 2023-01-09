import os
import platform

# Prints the name of your operating system.
result = os.name
# Prints the name of your operating system.
result = platform.system()
# Prints the version of your operating system.
result = platform.release()
# Operates terminal actions.
result = os.system("pip install pandas")
# Gives the path of the directory.
result = os.getcwd()
# Creates a directory.
result = os.mkdir("WEINOOSE")
# old, new given parameters changes the file names.
result = os.rename("weinoose.py","WEINOOSE.py")
# Removes the file from the directory.
result = os.remove("pythoncourse.json")
