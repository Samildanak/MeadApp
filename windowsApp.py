import tkinter as tk
from datetime import datetime

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Super Mead App")
        self.geometry("300x200")

        btn_new_recipe = tk.Button(self, text="New Recipe", command=self.open_new_recipe, width=20, height=2)
        btn_new_recipe.pack(pady=40)

        btn_show_recipe = tk.Button(self, text="Show Recipes", command=self.open_show_recipe, width=20, height=2)
        btn_show_recipe.pack()

    def open_new_recipe(self):
        NewRecipeWindow(self)

    def open_show_recipe(self):
        ShowRecipeWindow(self)

class NewRecipeWindow(tk.Toplevel):
    # A New Recipe should provide :
    #   - Name (Text Box)
    #   - Batch Id (Label auto calculated)
    #   - Date (Label auto provided)
    #   - Honey Quantity (Label auto calculated)
    #   - yeast type (Selection from yeast available)
    #   - use of K Fermaid (Check box)
    #   - Alcohol predict (Text box)
    #   - Volume prepared (Text box)
    #   - Residual Sugar wanted (Text box)
    #   - Table for Residual Sugar to help (Label)
    #   - Note page (Text box)
    #   - Save Button (Button)

    def __init__(self, parent):
        super().__init__(parent)
        self.title("New Recipe")
        self.geometry("600x400")

        self.residual_frame = tk.Frame(self)
        self.note_frame = tk.Frame
        self.button_frame = tk.Frame(self)

        self.create_name_id_frame()
        self.create_ingredients_frame()

    def create_name_id_frame(self):
        self.id = self.get_id()
        self.date = datetime.now().strftime("%d/%m/%Y")

        self.name_id_frame = tk.Frame(self)
        self.name_id_frame.place(x=10,y=10)

        self.batch_lbl = tk.Label(self.name_id_frame, text=("Batch n° " + str(self.id)))

        self.name_lbl = tk.Label(self.name_id_frame, text="Name : ")
        self.name_txt_box = tk.Text(self.name_id_frame, height=1, width=40)

        self.date_lbl = tk.Label(self.name_id_frame, text="Date")
        self.date_calc_lbl = tk.Label(self.name_id_frame, text=self.date)

        self.batch_lbl.grid(column=0, row=0)
        self.name_lbl.grid(column=1, row=1)
        self.name_txt_box.grid(column=2, row=1)
        self.date_lbl.grid(column=1, row=2)
        self.date_calc_lbl.grid(column=2, row=2)

    def create_ingredients_frame(self):
        self.ingredients_frame = tk.Frame(self)
        self.ingredients_frame.place(x=10, y=100)

        self.lbl = tk.Label(self.ingredients_frame, text="Ici")
        self.lbl.pack()

    def get_id(self):
        return 1
    
    def save_recipe(self):
        pass

class ShowRecipeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Show Recipes")
        self.geometry("200x150")

        label = tk.Label(self, text="Show Recipes Window")
        label.pack(pady=20)