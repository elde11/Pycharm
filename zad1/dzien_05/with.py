#with open("blabla.txt") as f:
 #   read_file = f.read()
#    print(read_file)
    ##
#print(f.read())


class OurWith:
    def __enter__(self):
        print('Im enter')


    def __exit__(self, _,_1,_2):
        print("I'm Exit")

with OurWith():
    print("Im inside with")

f1 = open("blabla.txt")
f2 = open("blabla.txt")
print(f1.read())
print(f2.read())