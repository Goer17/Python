def sum_nums(*args):
    sum_total = 0;
    for item in args:
        sum_total += item;
    
    return sum_total;


print(sum_nums(1,2,3,4,5));