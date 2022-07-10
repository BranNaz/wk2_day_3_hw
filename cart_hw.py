# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():


    def __init__(self, add_list, remove_list, show_list):
        self.add = add_list
        self.remove = remove_list
        self.show = show_list


    def addList(self):
        item = input('What item would you like to add to your cart?').lower()
        self.add.append(item)
        return {self.add}


    def removeList(self):
        item = input("What item do you want to remove from your cart?").lower()
        if item in self.show:
            self.show.remove(item)
        print(f"Succesfully removed {item} from your cart")


    def showList(self):
        self.show
        return (f'This is your cart. {self.show}')



    def goShopping(self, show_list):
        li_1 = []
        while True:
            action = input("What do you want to do? add/remove/show/quit").lower()
            if action == 'add':
                self.add(li_1)
            elif action == 'remove':
                self.remove(li_1)
            elif action == 'show':
                self.show(li_1)
            elif action == 'quit':
                break

cartlist = Cart('Add' 'Remove''Show')
print(cartlist.show_list)
cartlist.__dict__
