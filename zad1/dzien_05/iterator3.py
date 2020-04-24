class Ciag:
    def __init__(self,limit):
        self.a =0
        self.b= 1
        self.limit = limit

    def __next__(self):
        if self.a >= self.limit:
            raise StopIteration
        #temp = self.b
        self.b = self.b + self.a
        self.a = temp
        #2 sposob
        #self.a, self.b = self.b, self.a + self.b

        return self.a
    def __iter__(self):
        return self.a
ciag = Ciag(100)

for x in ciag:
    print(x)