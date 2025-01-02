from tkinter import *
from store_options import store_option, clothes, order_frame
from page_banner import banner
import config

class self(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x800")
        self.resizable(0, 0)
        self.title("Arsenal FC Merchandise")
        header = banner(self, "merch_banner.png", 0, True, TOP)

        #marketplace section
        marketplace = Frame(self, bg = "white")

        # first row
        store_row1 = Frame(marketplace)
        self.home = clothes(store_row1, "Arsenal Home Kit 2022-2023", "home.png", "$75.00", self)
        self.away = clothes(store_row1, "Arsenal Away Kit 2022-2023", "away.png", "$70.00", self)
        self.third = clothes(store_row1, "Arsenal Third Kit 2022-2023", "third.png", "$70.00", self)
        self.champ = clothes(store_row1, "Arsenal Champions League Final '05-'06", "champ.png", "$70.00", self)
        self.henry = clothes(store_row1, "Arsenal Henry Invicibles '05-'06", "henry.png", "$100.00", self)
        store_row1.pack(side = TOP, padx = (15, 0))
        store_row1.config(bg = "white")

        # second row
        store_row2 = Frame(marketplace)
        self.kit = clothes(store_row2, "Arsenal Full Tracksuit Kit", "kit.png", "$100.00", self)
        self.socks = clothes(store_row2, "Arsenal Home Socks 2022-2023", "socks.png", "$50.00", self)
        self.wb = store_option(store_row2, "Arsenal x ADIDAS 24oz Water Bottle", "bottle.png", "$20.00", self)
        self.bp = store_option(store_row2, "Arsenal x ADIDAS Training Backpack", "backpack.png", "$30.00", self)
        self.prime = store_option(store_row2, "Arsenal x PRIME Energy Drink", "prime.png", "$20.00", self)
        store_row2.pack(side = TOP, padx = (15, 0))
        store_row2.config(bg = "white")
        
        footer = banner(marketplace, "footer.png", 0, False, BOTTOM)

        marketplace.pack(side = LEFT)
        marketplace.config(highlightthickness = 0)

        #receipt
        # config.receipt = [self.home.receipt + self.away.receipt + self.third.receipt + self.champ.receipt + self.henry.receipt + self.kit.receipt + self.socks.receipt + self.wb.receipt + self.bp.receipt + self.prime.receipt]
        # self.order_cost = sum([self.home.total_cost + self.away.total_cost + self.third.total_cost + self.champ.total_cost + self.henry.total_cost + self.kit.total_cost + self.socks.total_cost + self.wb.total_cost + self.bp.total_cost + self.prime.total_cost])
        order_frame(self)

        # test = Label(text = "HELLO")
        # test.pack()
        # store_option(self, "Arsenal Away Kit 2022-2023", "away.png", "$70.00")
        # store_option(self, "Arsenal Third Kit 2022-2023", "third.png", "$65.00")
        
        # self.after(1000, self.update)

        self.configure(background = "white")
        

if __name__ == "__main__":
    self = self()
    self.mainloop()