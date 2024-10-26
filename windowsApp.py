import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Super Mead App")
        self.geometry("300x200")

        btn_new_recipe = tk.Button(self, text="New Recipe", command=self.open_new_recipe)
        btn_new_recipe.pack(pady=40)

        btn_show_recipe = tk.Button(self, text="Show Recipes", command=self.open_show_recipe)
        btn_show_recipe.pack(pady=20)

    def open_new_recipe(self):
        NewRecipeWindow(self)

    def open_show_recipe(self):
        ShowRecipeWindow(self)

class NewRecipeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("New Recipe")
        self.geometry("200x150")

        label = tk.Label(self, text="New Recipe Window")
        label.pack(pady=20)

class ShowRecipeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Show Recipes")
        self.geometry("200x150")

        label = tk.Label(self, text="Show Recipes Window")
        label.pack(pady=20)