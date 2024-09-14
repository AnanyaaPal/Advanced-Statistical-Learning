# Check if a number is a multiple of both 3 AND 5
def _check_number_(num):
    if num % 3 == 0 and num % 5 == 0:
        return(f'The number {num} is divisible by both 3 and 5.')
    else:
        return(f'The number {num} is not divisible by both 3 and 5 and may be divisible by either one.')

_check_number_(11)

# Compare two numbers and print which is larger.
def _compare_numbers_(a,b):

    if a > b :
        return(f'{a} is larger than {b}')
    else:
        return(f'{b} is larger than {a}')

_compare_numbers_(10,20)

# Check if a person is eligible to vote based on age

def _check_eligibility(age: int):
    if age > 18:
        return(f'Person of age {age} is eligible to vote.')
    else:
        return(f'Person of age{age} is not eligible to vote.')
    
_check_eligibility(11)

# Check if a password is strong 



