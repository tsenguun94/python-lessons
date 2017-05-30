import os

path = "/"
dirfiles = os.listdir(path)
dir_names = []
file_names = []

for each in dirfiles:
    full_name = path + each
    if os.path.isdir(full_name):
        dir_names.append(full_name + '/')
    else:
        file_names.append(full_name)
print("Directory name: ")
print(dir_names)
print("File names: ")
print(file_names)