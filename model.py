import csv
import view

class Restaurant:
    def __init__(self):
        self.number_of_tables = 3
        self.order_list = [ [] for _ in range(self.number_of_tables) ]
        self.menu = Menu()

    def add_orders(self, table_nr, orders):
        # get foot item from orders
        for i in range(len(orders)):
            if orders[i] == 1:
                food_item = self.menu.menu[i]
                self.order_list[table_nr].append(food_item)

    def print_orders(self, table_nr):
        print('Table-Number:', table_nr)
        for i in range(len(self.order_list[table_nr])):
            print(self.order_list[table_nr][i].name)

class Menu():
    def __init__(self):
        self.menu = []
        file = open('food.csv', 'r')
        csvreader = csv.reader(file, delimiter = ';')
        # build FoodItem object for every row in csv file
        next(csvreader)
        for row in csvreader:
            row[3] = row[3].replace(',','.')
            food_item = FoodItem(row[0], row[1], row[2], float(row[3]))
            self.menu.append(food_item)

    def show_menu(self):
        print(self.menu)

class FoodItem:
    def __init__(self, name, type, category, price):
        self.name = name
        self.type = type
        self.category = category
        self.price = price
        self.special_wishes = []

    def add_special_wishes(self, wish):
        self.special_wishes.append(wish)

if __name__ == '__main__':
    restaurant = Restaurant()
    # start app
    view.App(restaurant)
