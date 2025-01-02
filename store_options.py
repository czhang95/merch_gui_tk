from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.font as font
import config



# ***** STORE OPTION *****
class store_option:
    def __init__(self, root, name, img, price, app):
        self.app = app
        self.cost = 0

        self.color = "#edeff1"
        self.root = root
        self.name = name
        self.img = img
        self.price = price
        
        self.frame = Frame(self.root, bg = self.color, width = 1000, height = 1000)
        self.item_options_frame = Frame(self.frame, bg = self.color)
        
        self.misc()
        self.size()

    def misc(self):        
        # store option image
        original = Image.open(self.img)
        resized = original.resize((150, 140))
        display = ImageTk.PhotoImage(resized)
        banner = Label(self.frame, image = display)
        banner.image = display
        banner.pack(side = TOP)
        
        item = Label(self.frame, text = self.name, font = ("Arsenal" , 12), wraplength = 100)
        item.pack()
        item.config(bg = self.color)
        
        price = Label(self.frame, text = self.price)
        price.pack()
        price.config(bg = self.color)
        
        self.order_button = Button(self.item_options_frame, text= "Add to cart", command = lambda: [self.order_receipt(name = self.name, price = self.price), self.update_order()])
        self.item_options_frame.pack(side = BOTTOM)
        
        self.frame.pack(side = LEFT, pady = (36, 0), padx = (0, 10))
        self.frame.config(highlightbackground = "#9c8249", highlightthickness = 2)
    
    def size(self):
        self.order_button.pack(side = RIGHT, padx = (41, 41), pady = (22, 3))
        self.order_button.config(bg = self.color)
    
    def test(self, test):
        print(test)
    
    def order_receipt(self, **kwargs):
        print("HELLO")
        print(kwargs)

        order = []
        price = 0
        for key, order_request in kwargs.items():
            order.append(order_request)
        
        if len(kwargs) == 3:
            if kwargs["size"] != "Select":
                config.receipt.append(order)
                print(config.receipt)
        
                for order in config.receipt:
                    price += int(float(order[1][1:]))
            
                config.order_cost = price
                print(config.order_cost, "***************************************************************")
            else:
                error_popup(self.root, "store", kwargs["name"])
        else:
            config.receipt.append(order)
            print(config.receipt)
        
            for order in config.receipt:
                price += int(float(order[1][1:]))
            
            config.order_cost = price
            print(config.order_cost, "***************************************************************")
    
    def update_order(self):
        row = len(config.receipt) + 1
        print("HSHDHDHSDHSHD")
        print(config.receipt)
        receipt.config(state = NORMAL)
        if (len(config.receipt) != 0) and (config.receipt[-1][0] == self.name):
            print("**************JHEFHEHFEHFHEFHEF*****&&&&&")
            noi_display["text"] = "Number of items in cart: " + str(len(config.receipt))
            print(config.order_cost)
            order_cost_display["text"] = "Order cost: $" + str(config.order_cost) + ".00"
            print("LAST:", config.receipt[-1])
            receipt_str_len = len(str(config.receipt[-1]))
            order_text = str(config.receipt[-1])[1: receipt_str_len - 1]
            # receipt.insert(str(row) + ".0", order_text + "\n")
            receipt.insert(END, order_text + "\n\n")
            receipt.see("end")
            receipt.config(state = DISABLED)
            row += 1


class clothes(store_option):
    def __init__(self, root, name, img, price, app):
        super().__init__(root, name, img, price, app)
        
    def size(self):        
        size_select_prompt = Label(self.item_options_frame, text = "Size:")
        size_select_prompt.pack(side = TOP, padx = (0, 150))
        size_select_prompt.config(bg = self.color)
        options_list = ["Small", "Medium", "Large", "XLarge", "XXLarge"]
        size_selected = StringVar(self.root)
        size_selected.set("Select")
        size_selection = OptionMenu(self.item_options_frame, size_selected, *options_list)
        size_selection.pack(side = LEFT)
        size_selection.config(bg = self.color)
        
        self.order_button = Button(self.item_options_frame, text= "Add to cart", command = lambda: [self.order_receipt(name = self.name, price = self.price, size = size_selected.get()), self.update_order()])

        self.order_button.pack(side = RIGHT, pady = (0, 3))
        self.order_button.config(bg = self.color)

# ******** CHECKOUT - ORDER FRAME ******** 
class order_frame:
    def __init__(self, root):
        print(config.receipt)
        self.root = root
        self.master = Frame(root)
        self.frame = Frame(self.master, bg = "#edeff1", highlightbackground = "#023474" , highlightthickness = 2)
        self.shopping_cart_frame = Frame(self.frame, bg = "#edeff1")
        self.order_item_frame = Frame(self.frame, bg = "#edeff1")
        self.shopping_cart()
        self.order_item_display(self.order_item_frame)
        self.buttons()
        self.master.pack(side = RIGHT, pady = (35, 0))
        self.confirm_button_presses = 0

    def shopping_cart(self):   
        number_of_items = len(config.receipt)
        noi_str = str(number_of_items)
        global noi_display
        noi_display = Label(self.shopping_cart_frame, text = "Number of items in cart: " + noi_str)
        noi_display.pack(side = TOP, pady = (10, 0))
        
        global order_cost_display
        order_cost_display = Label(self.shopping_cart_frame, text = "Order cost: $" + str(config.order_cost) + ".00")
        
        order_cost_display.pack(side = TOP, pady = (0, 10))
        print("egydewdyedygweydweyyd")

        self.shopping_cart_frame.pack(side = TOP)
        self.frame.pack()
    
    def order_item_display(self, root):
        yScroll = Scrollbar(root, orient = VERTICAL)
        global receipt
        receipt = Text(root, height = 30, width = 30, wrap = WORD)
        receipt.pack(side = TOP, padx = 10, pady = 10)
        receipt.config(yscrollcommand = yScroll.set, state = DISABLED)
        yScroll.config(command = receipt.yview)
        root.pack()
    
    def buttons(self):
        button_text = font.Font(size = 30)
        
        reset = Button(self.order_item_frame, text = '  Reset Order  ', bg = "#9c8249", fg = "#053374", command = lambda: [self.reset_receipt()])
        reset["font"] = button_text
        reset.pack(pady = (10, 0))
        
        confirm = Button(self.order_item_frame, text = 'Confirm Order', bg = "#9c8249", fg = "#053374", command = lambda: [self.order_confirmation_gui()])
        confirm["font"] = button_text
        confirm.pack(pady = (0, 10))

    def order_confirmation_gui(self):
        if config.confirm_button_press == True:
            print("YUUUUUUUUUUP")
            print(config.confirm_button_press)
            error_popup(self.root, "window", None)
            return

        padding = 5
        
        color = "#edeff1"
        root = Toplevel(self.root, bg = color)
        root.resizable(0, 0)
        root.geometry("400x850")
        root.title("Order Checkout")
        
        final_order_label = Label(root, text = "Final order receipt: ")
        final_order_label.pack()

        yScroll = Scrollbar(root, orient = VERTICAL)
        final_receipt = Text(root, height = 30, width = 30, wrap = WORD)
        final_receipt.pack(side = TOP, padx = 10, pady = 10)
        
        final_receipt_str = receipt.get("1.0", END)
        
        print("202 FINAL :", final_receipt_str)
        print("203: ", final_receipt_str.split())
        print(len(final_receipt_str))

        if len(final_receipt_str) == 1:
            print("JIIJEFJIEIJFJEFIE")
            error_popup(self.root, "receipt", None)
            root.destroy()
            return

            # "return" ends current function, thus ending the order_confirmation popup from appearing once this error occurs
        final_receipt.insert(END, final_receipt_str)
        
        no_item = Label(root, text = "Items to checkout: " + str(len(config.receipt)))
        no_item.pack()
        
        price = Label(root, text = "Total cost: $" + str(config.order_cost) + ".00")
        price.pack()
        
        warning_font = font.Font(size = 7)
        warning_display1 = Label(root, text = "PRESS 'ENTER' AFTER ENTERING INPUT TO SAVE IT")
        warning_display2 = Label(root, text = "ONCE ALL FIELDS ARE COMPLETE, PRESS 'SAVE' TO CONFIRM ORDER")
        warning_display1["font"] = warning_font
        warning_display2["font"] = warning_font
        warning_display1.pack(side = TOP)
        warning_display2.pack(side = TOP)
        
        # Full Name
        Label(root, text = "Full Name", bg = color).pack(pady = (padding, 0))
        name = StringVar()
        name_entry = Entry(root,  textvariable = name)
        name_entry.pack()

        # Address
        Label(root, text = "Address", bg = color).pack(pady = (padding, 0))
        address = StringVar()
        address_entry = Entry(root, textvariable = address)
        address_entry.pack()
        
        # Province
        Label(root, text = "Province", bg = color).pack(pady = (padding, 0))
        options = self.read_province("provinces.txt")
        province = StringVar()
        province.set("Select")
        province_entry = OptionMenu(root, province, *options)
        province_entry.pack()
        
        # City
        Label(root, text = "City", bg = color).pack(pady = (padding, 0))
        city = StringVar()
        city_entry = Entry(root, textvariable = city)
        city_entry.pack()
        
        # Email
        Label(root, text = "Email", bg = color).pack(pady = (padding, 0))
        email = StringVar()
        email_entry = Entry(root, textvariable = email)
        email_entry.pack()
        
        # Save order
        button_text = font.Font(size = 30)
        
        save = Button(root, text = 'Save  Order', bg = "#9c8249", fg = "#053374", command = lambda: [self.save_data(name, address, province, city, email, root, self.root)])
        save["font"] = button_text
        save.pack()
        
        config.confirm_button_press = True
        root.protocol("WM_DELETE_WINDOW", self.close())

    def reset_receipt(self):
        print("RESET")
        receipt.config(state = NORMAL)
        receipt.delete("1.0", END)
        config.receipt = []
        config.order_cost = 0
        noi_display["text"] = "Number of items in cart: 0"
        order_cost_display["text"] = "Order cost: $0.00"
        receipt.config(state = DISABLED)
    
    def close(self):
        print("CLLLOOOOOSSEEED")
        config.confirm_button_press = False
        print(config.confirm_button_press)
    
    def save_data(self, name, address, province, city, email, local_root, global_root):
        print("WOOOOOOOPOOOOOAHHHHHHH")
        fileD = open('orders.txt','a', encoding = "UTF-8")
        fileD.write(f"***** ORDER {config.number_of_orders} ***** \n")
        
        print("292: ", config.receipt)
    
        username = name.get()
        useraddress = address.get()
        userprov = province.get()
        usercity = city.get()
        useremail = email.get()
    
        if (len(username) == 0) or (len(useraddress) == 0) or (len(userprov) == 0) or (len(usercity) == 0) or (len(useremail) == 0):
            error_popup(local_root, "fields", None)
            return

        fileD.write(f'Full name: {username} |  ')
        fileD.write(f'Address: {useraddress} | ')
        fileD.write(f'Province: {userprov} | ')
        fileD.write(f'City: {usercity} | ')
        fileD.write(f'Email: {useremail} \n')
        fileD.write("\nITEMS ORDERED: \n\n")
        
        for order in config.receipt:
            fileD.write(str(order) + "\n")
    
        number_of_items = str(len(config.receipt))
        fileD.write(f"\n^^^ # OF ITEMS ORDERED ^^^: {number_of_items} \n")
        fileD.write(f"^^^ ORDER TOTAL ^^^: ${config.order_cost}.00 \n\n")
    
        fileD.close()
    
        self.order_success(global_root, username)
        config.receipt = []
        config.order_cost = 0
        config.confirm_button_press = False
        local_root.destroy()
        config.number_of_orders += 1
    

    def read_province(self, file):
        depots = []
        depots_f=open(file)
        for line in depots_f:
            depots.append(line.rstrip())
        return depots

    def order_success(self, root, name):
        total_cost = config.order_cost
        no_items = str(len(config.receipt))
        popup = Toplevel(root, bg = "white")
        popup.resizable(0, 0)
        popup.geometry("350x100")
        
        success_image = Image.open("winner.png")
        resized = success_image.resize((80, 80))
        image_display = ImageTk.PhotoImage(resized)
        image_widget = Label(popup, bg = "white", image = image_display)
        image_widget.image = image_display
        image_widget.pack(side = LEFT, padx = (0, 10))
        
        popup.title("Succesful Order, " + name + f": ORDER #{config.number_of_orders}")
        success_text = Text(popup, height = 2, bg = "white", highlightthickness = 0, font = ("Calibri", 12), wrap = WORD)
        success_text.insert("1.0", f"Your order was successful, {name}. \n" + f"You are ORDER #{config.number_of_orders}. \n" + "ORDER COST: {total_cost} \n", "# OF ITEMS ORDERED: {no_items}")
        success_text.config(state = DISABLED)
        success_text.pack(side = RIGHT, pady = (7, 0))
        self.reset_receipt()


def test():
    print("*****TEST******")
    
def error_popup(root, call, item):
    popup = Toplevel(root, bg = "white")
    popup.resizable(0, 0)
    popup.geometry("350x100")
        
    error_image = Image.open("nospurs.png")
    resized = error_image.resize((60, 60))
    image_display = ImageTk.PhotoImage(resized)
    image_widget = Label(popup, bg = "white", image = image_display)
    image_widget.image = image_display
    image_widget.pack(side = LEFT, padx = (0, 10))
        
    if call == "store":
        popup.title("Error ordering " + item)
        error_text = Text(popup, height = 2, bg = "white", highlightthickness = 0, font = ("Calibri", 12), wrap = WORD)
        error_text.insert("1.0", "Select a valid size before adding item to cart.")
        error_text.config(state = DISABLED)
        error_text.pack(side = RIGHT, pady = (7, 0))
        
    if call == "receipt":
        popup.title("Error: Empty receipt ")
        error_text = Text(popup, height = 2, bg = "white", highlightthickness = 0, font = ("Calibri", 12), wrap = WORD)
        error_text.insert("1.0", "Your receipt is empty. Please select an item before proceeding to checkout")
        error_text.config(state = DISABLED)
        error_text.pack(side = RIGHT, pady = (7, 0))

    if call == "window":
        popup.title("Error: Window already open")
        error_text = Text(popup, height = 2, bg = "white", highlightthickness = 0, font = ("Calibri", 12), wrap = WORD)
        error_text.insert("1.0", "This window is already open. Close the current order window to open a new one.")
        error_text.config(state = DISABLED)
        error_text.pack(side = RIGHT, pady = (7, 0))
    
    if call == "fields":
        popup.title("Error: Some fields empty")
        error_text = Text(popup, height = 2, bg = "white", highlightthickness = 0, font = ("Calibri", 12), wrap = WORD)
        error_text.insert("1.0", "Please fill out all input fields before confirming your order.")
        error_text.config(state = DISABLED)
        error_text.pack(side = RIGHT, pady = (7, 0))