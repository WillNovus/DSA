class MyInt:
    def __init__(self, value):
        self.value = 0

    def increment(self, value):
        self.value +=1
    

    def main(self):
        var = MyInt()
        print("Value before increment", var.value)
        self.increment(var)
        print("Value after increment", var.value)


if __name__ == "main":
    import sys
    print("Hello World")
    MyInt.main(sys.argv)

