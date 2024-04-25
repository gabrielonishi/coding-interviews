'''
Question 5.7 - Cracking the Coding Interview

Pairwise Swap

Write a program to swap odd and even bits in an integer with as few instructions as possible 
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).
'''

def swap_odd_even_bits(x: int) -> int:
    even_bits = x & 0b10101010101010101010101010101010
    odd_bits = x & 0b01010101010101010101010101010101
    even_bits >>= 1
    odd_bits <<= 1
    
    return even_bits | odd_bits