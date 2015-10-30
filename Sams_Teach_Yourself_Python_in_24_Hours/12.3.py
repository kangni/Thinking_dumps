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
        else:
            print self.long_desc


class CateringItem(MenuItem):
    def __init__(self, title, cost, number_serves, special_instr='', long_desc='', short_desc='', item_type='main'):
        super(MenuItem, self).__init__()
        self.title = title
        self.special_instr = special_instr
        self.long_desc = long_desc
        self.short_desc = short_desc
        self.item_type = item_type
        self.number_serves = number_serves

    def print_item(self, desc_type='short'):
        print "{title} ... ${cost}".format(title=self.title, cost=self.cost)
        print "Serves: ", self.number_serves
        if desc_type == 'short':
            print self.short_desc
        elif desc_typr == 'long':
            print self.long_desc
        if self.special_instr:
            print "Special instructions: ", self.special_instr
