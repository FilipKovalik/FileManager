import os
import time


def only_folders(files: list, directory: str):
    sorted_list = [[], []]
    for file in files:
        if os.path.isdir(directory +f"\\{file}"):
            sorted_list[1].append(file)
        else:
            sorted_list[0].append(file)
        
    return sorted_list

def recursion_find(directory: str, file_name: str, final_list: list = []):
     
    files = os.listdir(directory)
    _f = only_folders(files, directory)
    
    filess = _f[0]
    folders = _f[1]
    
    if filess != []:
        for f in filess:
            if file_name in f:
                final_list.append(directory + f"\\{f}")
                # print(directory + f"\\{f}")
    if folders != []:
        for fold in folders:
            recursion_find(directory + f"\\{fold}", file_name)
    
    return final_list


directory = "D:\\Filip"

t1 = time.time()
fin_dir = recursion_find(directory, "main")
# os.startfile(fin_dir[0])
t2 = time.time()
print(fin_dir)
print(t2- t1)