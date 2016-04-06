'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640. Find the difference
between the sum of the squares of the first one hundred natural numbers and
the square of the sum.
'''

def sum_of_squares(n):
    '''
    Square each number and then add to total.
    Return total.
    '''
    total = 0
    for i in range(n+1):
        total += (i*i)
    return total

def square_of_sums(n):
    '''
    Add numbers in range and then square.
    Return total.
    '''
    total = 0
    for i in range(n+1):
        total += i
    return total*total

def difference(n):
    return square_of_sums(n) - sum_of_squares(n)

print difference(100)
