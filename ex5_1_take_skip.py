# Create a class called take_skip. Upon initialization it should 
# receive a step(number) and a count(number). Implement the 
# __iter__and __next__ functions. The iterator should return the 
# count amount of numbers (starting from 0) and with the given 
# step.

class take_skip():

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):       
        if self.counter < self.count:
            nxt_val = self.step * self.counter 
            self.counter += 1
            return nxt_val
        else:
            raise StopIteration()


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

print()
numbers = take_skip(10, 5)
for number in numbers:
    print(number)