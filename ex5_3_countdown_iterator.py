# Create a class called countdown_iterator. Upon initialization 
# it should receive a count. Implement the iterator, so it returns 
# each number of the countdown (from count to 0 inclusive).

class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.iterator = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator >= 0:
            iterator = self.iterator
            self.iterator -= 1
            return iterator
        else:
           raise StopIteration()

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
