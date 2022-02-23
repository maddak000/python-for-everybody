rawstr = input('Enter an positive number: ')
try:
    my_val = int(rawstr)
except:
    my_val = -1

print('Nice work' if my_val > 0 else 'Not a positive number')
