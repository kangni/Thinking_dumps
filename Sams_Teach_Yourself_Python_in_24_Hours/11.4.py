class MenuItem(object):
    def __init__(self, title, cost, long_desc = '', short_desc = '', item_type = 'main'):
        self.title = title
        self.cost = cost
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type

    def change_item_type(self, item_type):
        self.item_type = item_type

    def change_cost(self, cost):
        self.cost = cost

    def change_description(self, long_desc='', short_desc=''):
        if long_desc:
            self.long_desc = long_desc
        if short_desc:
            self.short_desc = short_desc

    def change_title(self, title):
        self.title = title

    def print_item(self, desc_type='short'):
        print "{title} ... ${cost}".format(title=self.title, cost=self.cost)
        if desc_type == 'short':
            print self.short_desc
        elif desc_type == 'long':
            print self.long_desc

