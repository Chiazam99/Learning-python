# Process of responding to exceptions in a cuustom way during the execution of a program
# Try: code 
#except: error message why code isn't running 

try: 
    numerator = int(input('Enter numerator:'))
    denominator = int(input('Enter denominator:'))

    result = numerator/denominator  
    print(result)

    example_list = [2,5,6,7,8,9]
    i = int(input('Enter index'))
    print(example_list[i])
except ValueError:
    print('You entered a float or string')
except ZeroDivisionError:
    print('Zero can\'t divide a number')
except IndexError:
    print('Index isn\'t within list range')
