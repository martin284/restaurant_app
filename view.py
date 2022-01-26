import tkinter as tk
import model

class App:
    def __init__(self, restaurant):
        root = tk.Tk()
        root.title('Overview')
        for table_nr in range(restaurant.number_of_tables):
            table = Table(root, table_nr, restaurant)
            table.grid(row=table_nr, column=0, padx=20, pady=20)
        root.mainloop()

class Table(tk.Frame):
    def __init__(self, master, table_nr, restaurant):
        super().__init__(master)
        self.ext_padding_y = 5
        self.ext_padding_x = 15
        table_label = TableLabel(self, table_nr)
        table_label.grid(row=0, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        order_btn = OrderButton(self, restaurant, table_nr)
        order_btn.grid(row=1, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        bill_btn = ShowBillButton(self)
        bill_btn.grid(row=2,column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)

class TableLabel(tk.Label):
    def __init__(self, master, table_nr):
        self.text = 'Table '+str(table_nr)
        super().__init__(master, text=self.text)

class MenuSelection(tk.Toplevel):
    def __init__(self, master, restaurant, table_nr):
        super().__init__(master)
        self.title('Menu')
        # show menu
        chosen_selections = []
        for i in range(len(restaurant.menu.menu)):
            food_name = restaurant.menu.menu[i].name
            chosen_selections.append(tk.IntVar())
            c = tk.Checkbutton(self, text=food_name,
            variable=chosen_selections[i])
            c.grid(row=i, column=0)
        def show_selection():
            for i in range(len(menu)):
                print(chosen_selections[i].get())
        # safe selections in model
        def safe_selections():
            for i in range(len(chosen_selections)):
                chosen_selections[i] = chosen_selections[i].get()
            restaurant.add_orders(table_nr, chosen_selections)
        show_selection_btn = tk.Button(self, text='Show',
        command=show_selection)
        show_selection_btn.grid(row=len(restaurant.menu.menu), column=0)
        def finish():
            safe_selections()
            self.destroy()
        finish_btn = tk.Button(self, text='Finish', command=finish)
        finish_btn.grid(row=len(restaurant.menu.menu)+1, column=0)

class OrderButton(tk.Button):
    def __init__(self, master, restaurant, table_nr):
        self.text = "Add Order"
        def show_menu():
            MenuSelection(self, restaurant, table_nr)
        super().__init__(master, text=self.text, command=show_menu)

class ShowBillButton(tk.Button):
    def __init__(self, master):
        self.text = "Show Bill"
        super().__init__(master, text=self.text)

if __name__ == '__main__':
    App()
