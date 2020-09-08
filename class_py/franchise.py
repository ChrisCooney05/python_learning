from menu import Menu


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def available_menus(self, time):
        for menu in self.menus:
            if menu.start_time <= time and menu.end_time >= time:
                print(menu)

    def __str__(self):
        return 'Address of Franchise is {address}'.format(address=self.address)
