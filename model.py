import csv

class Order:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, food_item):
        self.food_items.append(food_item)

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
