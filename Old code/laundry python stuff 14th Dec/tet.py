class MyFirst:
    i = 12345
    
    def f(self):
        print("hello")
    
    def __init__(self):
        self.data = [2]
        print(self.data)

instance = MyFirst()
instance.f()