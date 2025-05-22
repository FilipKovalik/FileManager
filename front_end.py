from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from functools import partial
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.properties import ObjectProperty
import os


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


def sort_files(files: list):
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



directory = "D:\\Filip\\Škola\\Python\\numpy__x"

files = os.listdir(directory)

sorted_files = sort_files(files)

class customButton(Button):
    root_widget = ObjectProperty()
    
    def on_release(self, **kwargs):
        super().on_release(**kwargs)
        self.root_widget.__folder_func(self.text)

class StLayout(GridLayout):
    sorted_files = sorted_files
    directory = directory
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.search = ""
        self.build()
    def build(self):
        
        self.size_hint = 1, 1
        self.cols = 6
        
        
        
        back_search_widget = BoxLayout()
        back_search_widget.height = 50
        back_search_widget.orientation = "horizontal"
        back_search_widget.spacing = "20dp"
        back_button = Button(text="Back")
        back_button.bind(on_press=partial(self.__back_func))
        self.search_text = TextInput(hint_text="Search file")
        search_button = Button(text="SEARCH")
        search_button.bind(on_press=partial(self.__search))
        
        back_search_widget.add_widget(back_button)
        back_search_widget.add_widget(self.search_text)
        back_search_widget.add_widget(search_button)
        
        self.add_widget(back_search_widget)
        
        self.rows = len(self.sorted_files)
        for i in range(self.rows):
            widget = BoxLayout()
            widget.orientation = "horizontal"
            widget.spacing = "1dp"
            widget.size = (10, 10)
            button = Button(text=f"{self.sorted_files[i]}")
            button.bind(on_press=partial(self._customButton__folder_func, self.sorted_files[i]))
            widget.add_widget(button)
            self.add_widget(widget)
        
    def _customButton__folder_func(self, direct, instance):
        _directory = os.listdir(self.directory)
        folders = only_folders(_directory, self.directory)[1]
        if direct in folders:
            self.directory += f"\\{direct}"
            files = os.listdir(self.directory)
            self.sorted_files = sort_files(files)
            self.clear_widgets()
            self.__init__()
        else:
            os.startfile(f"{self.directory}\\{direct}")
    def __back_func(self, instance):
        prev_dir = self.directory.split("\\")
        prev_dir = "\\".join(prev_dir[:-1])
        self.directory = prev_dir
        files = os.listdir(self.directory)
        self.sorted_files = sort_files(files)
        self.clear_widgets()
        self.__init__()
    def __search(self, instance):
        file_filder = recursion_find(self.directory, self.search_text.text)
        print(self.directory, self.search_text.text, file_filder)
        
        
class BLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
    def build(self):
        return self

class FrontEndApp(App):
    pass

if __name__ == "__main__":
    app = FrontEndApp()
    app.run()