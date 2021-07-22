"""
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "$" character.

What is the length of the shortest reference string S possible that encodes the given words?

In the input:  - array of strings
На выходе: integer

Example:

Input: words = ["lime", "me", "salt"]
Output: 10
Explanation: S = "lime$salt$" and indexes = [0, 2, 5].

Note:
Each word has only lowercase letters.
"""

def short_encoding(words):
    # Write your code here...
