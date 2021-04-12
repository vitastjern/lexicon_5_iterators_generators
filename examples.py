'''
x = iter([1,2,3])

print(next(x))
print(next(x))
print(next(x))
# an additional print will raise an exception
'''
'''
class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

y = yrange(3)
print(next(y))
print(next(y))
print(next(y))
# print(next(y))  # raises a StopIteration exception
'''

def yrange(n):
    i = 0
    while i < n:
        yield i     # yields a new i value
        i += 1

y = yrange(3)

print(next(y))
print(next(y))
print(next(y))
