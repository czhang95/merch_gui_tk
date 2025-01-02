from tkinter import *
from store_options import StoreItem, clothesItem, orderFrame
from page_banner import banner
import config

class Main(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x960")
        self.resizable(0, 0)
        self.title("Arsenal FC Merchandise")
        self.configure(bg= "white")
        header = banner(self, "assets/merch_banner.png", 0, True, TOP)

        #marketplace section
        marketplace = Frame(self, bg = "white")

        # first row
        # store_row1 = Frame(marketplace)
        # clothesItem(store_row1, "Arsenal Home Kit '22-'23", "assets/home.png", "$75.00", 12)
        # clothesItem(store_row1, "Arsenal   Away Kit '22-'23", "assets/away.png", "$70.00", 12)
        # clothesItem(store_row1, "Arsenal  Third Kit '22-'23", "assets/third.png", "$70.00", 12)
        # clothesItem(store_row1, "Arsenal Champions League Final '05-'06", "assets/champ.png", "$70.00", 8)
        # clothesItem(store_row1, "Arsenal Henry Invicibles '05-'06", "assets/henry.png", "$100.00", 11)
        
        # store_row1.pack(side = TOP, padx = (15, 0))
        # store_row1.config(bg = "white")

        # second row
        store_row2 = Frame(marketplace)

        tracksuit = clothesItem(store_row2, "Arsenal     Full Tracksuit Kit '15-'16", "assets/kit.png", "$100.00", 12)
        self.configure_item(tracksuit)
        
        # tracksuit.config(bg = "#edeff1", highlightbackground = "#9c8249", highlightthickness = 2, width = 200, height = 300)
        # tracksuit.pack(side = LEFT)
        # tracksuit.pack_propagate(0)

        socks = clothesItem(store_row2, "Arsenal Home Socks '22-'23", "assets/socks.png", "$50.00", 12)
        self.configure_item(socks)
        
        bottle = StoreItem(store_row2, "Arsenal x ADIDAS   24oz Bottle", "assets/bottle.png", "$20.00", 12)
        self.configure_item(bottle)

        backpack = StoreItem(store_row2, "Arsenal x ADIDAS Backpack", "assets/backpack.png", "$30.00", 12)
        self.configure_item(backpack)

        prime = StoreItem(store_row2, "Arsenal x PRIME Energy Drink", "assets/prime.png", "$20.00", 12)
        self.configure_item(prime)
        
        store_row2.pack(side = TOP, padx = (15, 0))
        store_row2.config(bg = "white")
        
        
        footer = banner(self, "assets/footer.png", 0, True, BOTTOM)

        marketplace.pack(side = LEFT)
        marketplace.config(highlightthickness = 0)

        orderFrame(self)

        # self.configure(background = "white")
        
    def configure_item(self, item):
        item.config(bg = "#edeff1", highlightbackground = "#9c8249", highlightthickness = 2, width = 200, height = 300)
        item.pack(side = LEFT)
        item.pack_propagate(0)
        

if __name__ == "__main__":
    main = Main()
    main.mainloop()