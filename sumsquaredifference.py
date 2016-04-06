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
