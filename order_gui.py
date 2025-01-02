from tkinter import *
import tkinter.font as font
import config

class order_frame:
    def __init__(self, root):
        print(config.receipt)
        self.master = Frame(root)
        self.frame = Frame(self.master, bg = "#edeff1")
        self.shopping_cart_frame = Frame(self.frame, bg = "#edeff1")
        self.user_info_frame = Frame(self.frame, bg = "#edeff1")
        self.order_cost = config.order_cost
        self.number_of_items = len(config.receipt) - 1
        self.shopping_cart()
        self.user_info_gui(self.frame)
        # self.shopping_cart_frame.after(100, self.update)

    def shopping_cart(self):   
        number_of_items = self.number_of_items
        noi_str = str(number_of_items)
        noi_display = Label(self.shopping_cart_frame, text = "Number of items in cart: " + noi_str)
        noi_display.pack(side = TOP)
        self.shopping_cart_frame = Frame(self.frame, bg = "#edeff1")
        
        print("CHECKING ORDER:")
        cost_str = "Order cost: $" + str(config.order_cost) + ".00"
        print(f"!!!! ORDER COST: {cost_str} ! ! ! !")
        order_cost_display = Label(self.shopping_cart_frame, textvariable = StringVar(value = str(config.order_cost)))
        
        order_cost_display.pack(side = TOP, pady = (0, 10))
        print("egydewdyedygweydweyyd")
        
        warning_font = font.Font(size = 7)
        warning_display1 = Label(self.shopping_cart_frame, text = "PRESS 'ENTER' AFTER ENTERING INPUT TO SAVE IT")
        warning_display2 = Label(self.shopping_cart_frame, text = "ONCE ALL FIELDS ARE COMPLETE, PRESS 'SAVE' TO CONFIRM ORDER")
        warning_display1["font"] = warning_font
        warning_display2["font"] = warning_font
        warning_display1.pack(side = TOP)
        warning_display2.pack(side = TOP)
        
        order_cost_display.config(text = cost_str)

        self.shopping_cart_frame.pack(side = TOP)
        self.frame.pack()
        
        

    def user_info_gui(self, root):
        padding = 30
        
        # Full Name
        Label(self.user_info_frame, text = "Full Name").pack(pady = (padding, 0))
        name = StringVar()
        self.name_entry = Entry(self.user_info_frame, textvariable = name)
        self.name_entry.pack()
        
        # Address
        Label(self.user_info_frame, text = "Address").pack(pady = (padding, 0))
        address = StringVar()
        self.address_entry = Entry(self.user_info_frame, textvariable = address)
        self.address_entry.pack()
        
        # Province
        Label(self.user_info_frame, text = "Province").pack(pady = (padding, 0))
        options = read_province("provinces.txt")
        self.province = StringVar()
        self.province.set("Select")
        self.province_entry = OptionMenu(self.user_info_frame, self.province, *options)
        self.province_entry.pack()
        
        # City
        Label(self.user_info_frame, text = "City").pack(pady = (padding, 0))
        city = StringVar()
        self.city_entry = Entry(self.user_info_frame, textvariable = city)
        self.city_entry.pack()
        
        # Email
        Label(self.user_info_frame, text = "Email").pack(pady = (padding, 0))
        email = StringVar()
        self.email_entry = Entry(self.user_info_frame, textvariable = email)
        self.email_entry.pack()
        
        # Save/Reset order
        button_text = font.Font(size = 30)
        
        reset = Button(self.user_info_frame, text = 'Reset Order', bg = "#9c8249", fg = "#053374", command = lambda: [self.reset_entrybox(), test()])
        reset["font"] = button_text
        reset.pack(pady = (30, 0))
        
        save = Button(self.user_info_frame, text = 'Save  Order', bg = "#9c8249", fg = "#053374", command = lambda: [save_data(name, address, self.province, city, email, self.number_of_orders), self.update_order()])
        save["font"] = button_text
        save.pack()
        
        # GUI packing and padding
        self.user_info_frame.pack(side = BOTTOM)
        self.frame.pack(side = RIGHT)
        self.frame.config(highlightbackground = "#053374", highlightthickness = 2)
        
        self.master.pack(side = TOP, pady = (36, 0))


    def update_order(self):
        self.number_of_orders += 1
    
    def reset_entrybox(self):
        print("HELLO")
        self.name_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.province.set("Select")
        self.city_entry.delete(0, END)
        self.email_entry.delete(0, END)
    
    def update(self):
        self.shopping_cart()
        self.shopping_cart_frame.after(1000, self.update)

def test():
    print("*****TEST******")

def save_data(name, address, province, city, email, number_of_orders, receipt, total):
    print("WOOOOOOOPOOOOOAHHHHHHH")
    fileD = open('orders.txt','a', encoding = "UTF-8")
    fileD.write(f"***** ORDER {number_of_orders} ***** \n")
    
    username = name.get()
    fileD.write(f'Full name: {username} |  ')
    
    useraddress = address.get()
    fileD.write(f'Address: {useraddress} | ')
    
    userprov = province.get()
    fileD.write(f'Province: {userprov} | ')
    
    usercity = city.get()
    fileD.write(f'City: {usercity} | ')
    
    useremail = email.get()
    fileD.write(f'Email: {useremail} \n')
    
    fileD.write("ITEMS ORDERED: \n")
    
    for order in receipt:
        fileD.write(order + "\n")

    fileD.write(f"^^^ORDER TOTAL^^^: {total}")
    
    fileD.close()
    
    
def read_province(file):
    depots = []
    depots_f=open(file)
    for line in depots_f:
        depots.append(line.rstrip())
    return depots


    


