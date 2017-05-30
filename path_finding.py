import os
import queue

dir_queue = queue.Queue()
dir_queue.put("/home/tsenguun/")
all_dir = []

def get_subdir(path):
    subdir_list = []
    try:
        dirfiles = os.listdir(path)

    except PermissionError:
        return subdir_list


    for each in dirfiles:
        full_name = path + each
        print(full_name)
        if os.path.isdir(full_name):
            subdir_list.append(full_name + "/")
    return subdir_list





while not dir_queue.empty():
    dir_name = dir_queue.get()
    subdir_names = get_subdir(dir_name)
    all_dir.append(dir_name)
    for each in subdir_names:
        dir_queue.put(each)
