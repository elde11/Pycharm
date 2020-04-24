x = [1, 2, 3, 4]

iter_x = iter(x)

print(next(iter_x))
print(next(iter_x))
print(next(iter_x))
print(next(iter_x))

def our_for (function,iterable):
    iter_x_2 = iter(iterable)
    while True:
        try:
            function(next(iter_x_2))
        except StopIteration:
            break


our_for (lambda element: print(element),x)

#for element in x:
#    print(element)
