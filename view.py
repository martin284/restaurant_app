import tkinter as tk

class App:
    def __init__(self, master, number_of_tables):
        master.title('Overview')
        tables = list(range(number_of_tables))
        iterator = 0
        for x in range(2):
            for y in range(2):
                table = Table(master, iterator)
                table.grid(row=x, column=y, padx=20, pady=20)
                iterator += 1

class Table(tk.Frame):
    def __init__(self, master, table_nr):
        super().__init__(master)
        self.ext_padding_y = 5
        self.ext_padding_x = 15
        table_nr = TableNumber(self, table_nr)
        table_nr.grid(row=0, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        order_btn = OrderButton(self)
        order_btn.grid(row=1, column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)
        bill_btn = ShowBillButton(self)
        bill_btn.grid(row=2,column=0, padx=self.ext_padding_x,
        pady=self.ext_padding_y)

class TableNumber(tk.Label):
    def __init__(self, master, table_nr):
        self.text = 'Table '+str(table_nr)
        super().__init__(master, text=self.text)

class OrderButton(tk.Button):
    def __init__(self, master):
        self.text = "Add Order"
        super().__init__(master, text=self.text)

class ShowBillButton(tk.Button):
    def __init__(self, master):
        self.text = "Show Bill"
        super().__init__(master, text=self.text)

number_of_tables = 4
root = tk.Tk()
app = App(root, number_of_tables)
root.mainloop()
