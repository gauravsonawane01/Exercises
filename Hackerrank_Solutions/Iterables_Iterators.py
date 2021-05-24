'''
You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

Find the probability that at least one of the  indices selected will contain the letter: ''.

Input Format

The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer , denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

Note: The answer must be correct up to 3 decimal places.

Constraints



All the letters in the list are lowercase English letters.

Sample Input

4
a a c d
2
Sample Output

0.8333

'''

from itertools import combinations

N = int(input())
char = input().split()
K = int(input())

count = 0;
total = 0;

for i in combinations(char, K):
    count += 'a' in i
    total += 1

print(count / total)