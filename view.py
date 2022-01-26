import tkinter as tk
import model

class App:
    def __init__(self, menu):
        number_of_tables = 4
        root = tk.Tk()
        root.title('Overview')
        tables = list(range(number_of_tables))
        iterator = 0
        for x in range(2):
            for y in range(2):
                table = Table(root, iterator, menu)
                table.grid(row=x, column=y, padx=20, pady=20)
                iterator += 1
        root.mainloop()

class Table(tk.Frame):
    def __init__(self, master, table_nr, menu):
        super().__init__(master)
        self.ext_padding_y = 5
        self.ext_padding_x = 15
        table_nr = TableNumber(self, table_nr)
        table_nr.grid(row=0, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        order_btn = OrderButton(self, menu)
        order_btn.grid(row=1, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        bill_btn = ShowBillButton(self)
        bill_btn.grid(row=2,column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)

class TableNumber(tk.Label):
    def __init__(self, master, table_nr):
        self.text = 'Table '+str(table_nr)
        super().__init__(master, text=self.text)

class MenuSelection(tk.Toplevel):
    def __init__(self, master, menu):
        super().__init__(master)
        self.title('Menu')
        chosen_selections = []
        for i in range(len(menu)):
            food_name = menu[i].name
            chosen_selections.append(tk.IntVar())
            c = tk.Checkbutton(self, text=food_name,
            variable=chosen_selections[i])
            c.grid(row=i, column=0)
        def show_selection():
            for i in range(len(menu)):
                print(chosen_selections[i].get())
        show_selection_btn = tk.Button(self, text='Show',
        command=show_selection)
        show_selection_btn.grid(row=len(menu), column=0)
        finish_btn = tk.Button(self, text='Finish', command=self.destroy)
        finish_btn.grid(row=len(menu)+1, column=0)

class OrderButton(tk.Button):
    def __init__(self, master, menu):
        self.text = "Add Order"
        def show_menu():
            MenuSelection(self, menu)
        super().__init__(master, text=self.text, command=show_menu)

class ShowBillButton(tk.Button):
    def __init__(self, master):
        self.text = "Show Bill"
        super().__init__(master, text=self.text)

if __name__ == '__main__':
    App()
