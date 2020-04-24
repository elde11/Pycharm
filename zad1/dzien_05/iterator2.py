class OurRange:
    def __init__(self):
        self.start = 0
        self.stop = 10

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1

        if self.start > self. stop:
            raise StopIteration

        return self.start

ourRange = OurRange()

for x in OurRange():
    print(x)