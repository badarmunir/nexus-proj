class rectnagle:

    def acceptdetails(self):
        self.length = 2.1
        self.width = 8.0

    def getArea(self):
        return self.length * self.width

    def display(self):
        print("length : {0}", self.length)
        print("Width : {0}", self.width)
        print("Area : {0}", self.getArea())


class ExecuteRectnagle:
    if __name__ == '__main__':
        obj = rectnagle()
        obj.acceptdetails()
        obj.display()
