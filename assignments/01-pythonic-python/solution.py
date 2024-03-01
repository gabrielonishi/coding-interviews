def print_indices_and_elements(elements) -> None:
    for i, j in enumerate(elements):
        print(i, j)
    pass


def get_even_numbers_between(start: int, end: int) -> list[int]:
    return [i for i in range(start, end + 1) if i%2 == 0]


def get_char_set_from(s: str) -> set[str]:
    return {i for i in s}


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {i : i ** 0.5 for i in range(start, end + 1) if i**0.5 == int(i**0.5)}


def filter_even_from(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i%2 == 0]


def get_number_or_minus_one(n: int) -> int:
    return n if n%2 == 0 else -1


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return [i if i%2 == 0 else -1 for i in numbers if i%5 == 0]


def str_lengths(strings: list[str]) -> list[int]:
    return [len(i) for i in strings]


def get_fibonacci_type(version: int) -> str:
    return 'generator' if version == 1 else 'list'


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return '''Fibonnaci 1 uses a generator, while fibonacci 2 saves the elements calculate d on a list. Fibonacci 1 uses
              less memory, but takes more time to return a certain value'''


class SkipIterator:
    def __init__(self, elements):
        
        self.elements = elements
        
        if elements is not None: 
            self.next_position = 0
        # You can add more code here if you need
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.next_position < len(self.elements):
            retval = self.elements[self.next_position]
            self.next_position += 2
            return retval
        
        raise StopIteration()


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    sum = e1 + e2
    elements = 2
    
    for element in others:
        sum += element
        elements += 1
        
    return sum/elements


def keys_with_different_value() -> list[int]:
    a = dict(zip(range(10), range(10)))
    b = dict(zip(range(5, 15), range(15, 25)))
    
    c_original = {**a, **b}
    c_reversed = {**b, **a}
        
    return [key for key in c_original if c_original[key] != c_reversed[key]]



def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        start, *inner, end = numbers
        numbers = inner
        print(start, end)
        
    if numbers:
        print(numbers[0])


def append_range(start: int, end: int, step: int=1, to: list[int]=None):
    
    # You may add code here
    if to is None:
        to = list()

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None
