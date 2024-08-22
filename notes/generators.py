'''
Generators are special objects that return values in a "lazy" way.
They are used to generate values on the fly, and are useful when
you don't need to store all values in memory.
'''

def fibo_gen():
    yield 1
    yield 1
    last, this = 1, 1
    while True:
        yield last + this
        temp = this
        this += last
        last = temp
        
gen = fibo_gen()

for i in range(30):
    print(next(gen))