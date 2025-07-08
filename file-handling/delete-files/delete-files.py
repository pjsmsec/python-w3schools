# Delete files
# To delete a file, you must import the OS module and run it's os.remove() function:
import os

# os.remove("demofile.txt")
# Note: if the file does not exist, this will raise an error

# Chek if file exists
import os

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

# Delete folder
# To delete an entire folder, use the os.rmdir() method:
import os

# os.rmdir("myfolder")
# If the folder does not exist, this will raise an error
# Note: you can only remove empty folders
