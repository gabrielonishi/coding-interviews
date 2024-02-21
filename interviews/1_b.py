'''
Problem 1.5 - Cracking the Coding Interview
Given two strings, write a function that checks if they are one (or zero) edit away from each other.

Definitions

    Edit: there are three types of edit operations - insert, remove, or replace a character;

Additional information

    Uppercase and lowercase letters must be considered different;
    Strings may contain any valid character.

Examples

    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false

'''
class Solution:
    def isOneEditAway(self, s1: str, s2: str) -> bool:
        i = 0 # referente a s1
        j = 0 # referente a s2

        edited = False

        while True:
            if i == len(s1) and len(s2) == j:
                return True
            elif i == len(s1) or len(s2) == j:
                if edited: return False
                return True
                
            if s1[i] != s2[j]:
                if edited: return False

                edited = True
                
                if len(s1) > len(s2):
                    i += 1
                elif len(s2) > len(s1):
                    j += 1
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1