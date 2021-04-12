# Create a class called dictionary_iter. Upon initialization it 
# should receive a dictionary object. Implement the iterator, so 
# it returns each key-value pair of the dictionary as a tuple of 
# two elements (the key and the value).

class dictionary_iter:

    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.i = 1  # dictionaries aren't lists, count from first tuple

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= len(self.dictionary):
            pair = (self.i,  self.dictionary.get(self.i))
            self.i += 1
            return pair
        else:
            raise StopIteration()

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
