import os
import time


def only_folders(files: list, directory: str):
    sorted_list = [[], []]
    for file in files:
        try:
            os.listdir(directory + f"\\{file}")
            sorted_list[1].append(file)
        except (NotADirectoryError):
            sorted_list[0].append(file)
        except (PermissionError):
            continue
        
    return sorted_list
            
def only_files(files: list, directory: str):
    sorted_list = []
    for file in files:
        if "." in file:
            sorted_list.append(file)
    return sorted_list

def sort_files_wo_sorting_files(files: list, directory: str):
    sorted_list = []
    sorted_list2 = []
    for file in files:
        if "." not in file:
            sorted_list.append(file)
        elif "." in file:
            sorted_list2.append(file)
    sorted_list.extend(sorted_list2)
    
    return sorted_list
            

def sort_files(files: list, directory: str):
    sorted_list_folders = []
    koncovky = set()
    for file in files:
        if "." not in file:
            sorted_list_folders.append(file)
    for file in files:
        if "." in file:
            file_end = file.split(".")[-1]
            koncovky.add(file_end)
    koncovky = list(koncovky)
    koncovky.sort()

    for k in koncovky:
        for f in files:
            f_end = f.split(".")
            f_end = f_end[-1]
            if f_end == k:
                sorted_list_folders.append(f)

    return sorted_list_folders



directory = "D:\\Filip\\Škola\\Python"

files = os.listdir(directory)

sorted_files = only_folders(files, directory)
sorted_files2 = only_files(files, directory)
sorted_files3 = sort_files_wo_sorting_files(files, directory)


def recursion_find(directory: str, file_name: str, final_list: list = []):
     
    files = os.listdir(directory)
    
    filess = only_folders(files, directory)[0]
    folders = only_folders(files, directory)[1]
    
    if filess != []:
        for f in filess:
            if file_name in f:
                final_list.append(directory + f"\\{f}")
                # print(directory + f"\\{f}")
    if folders != []:
        for fold in folders:
            recursion_find(directory + f"\\{fold}", file_name)
    
    return final_list


directory = "D:\\Filip\\Škola\\Python"

t1 = time.time()
fin_dir = recursion_find(directory, "learning__")
os.startfile(fin_dir[0])
t2 = time.time()
print(fin_dir)
print(t2- t1)