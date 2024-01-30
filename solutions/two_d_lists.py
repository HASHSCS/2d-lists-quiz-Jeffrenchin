# TODO: Implement a function that takes a two-dimensional list and returns the sum of each row
def sum_each_row(two_d_list):
    row_sums = []
    for row in two_d_list:
        row_sum = sum(row)
        row_sums.append(row_sum)
    return row_sums

# TODO: Implement a function that counts the number of non-zero elements in a two-dimensional list
def count_non_zero(two_d_list):
    count_number = 0
    for row in two_d_list:
        for col in row:
            if col > 0:
                count_number += 1
    return count_number
                

# TODO: Implement a function that extracts and returns the last element of each row in a two-dimensional list
def last_elements(two_d_list):
    i = []
    for row in two_d_list:
        if row:
            i.append(row[len(row)-1])            
    return i
    

    

# TODO: Implement a function that counts the number of times a given value appears in a two-dimensional list
def count_occurrences(two_d_list, value):
    value_appears = 0
    for row in two_d_list:
        for col in row:
            if value == col:
                value_appears += 1
    return value_appears
