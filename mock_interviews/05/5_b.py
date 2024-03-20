'''
Question 5.7 - Cracking the Coding Interview

Pairwise Swap

Write a program to swap odd and even bits in an integer with as few instructions as possible 
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''

def swap_odd_even_bits(x: int) -> int:
    right_shift = x >> 1
    left_shift = x << 1
    
    odd_bit_mask = 0x01010101010101010101010101010101
    even_bit_mask = 0x10101010101010101010101010101010
    
    return (right_shift & odd_bit_mask) + (left_shift & even_bit_mask)