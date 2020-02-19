class Parent(object):
    def __init__(self):
        self.value = 4

    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1


c = Child()
c.get_value()
