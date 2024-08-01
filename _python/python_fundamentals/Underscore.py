class Underscore:

    def map(self, iterable, callback):
        return [callback(x) for x in iterable]

    
    def find(self, iterable, callback):
        for x in iterable:
            if callback(x):
                return x
        return None

    
    def filter(self, iterable, callback):
        return [x for x in iterable if callback(x)]

    
    def reject(self, iterable, callback):
        return [x for x in iterable if not callback(x)]
    

_ = Underscore()


evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens) 

mapped = _.map([1, 2, 3], lambda x: x * 2)
print(mapped) 

found = _.find([1, 2, 3, 4, 5, 6], lambda x: x > 4)
print(found) 

rejected = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(rejected) 

