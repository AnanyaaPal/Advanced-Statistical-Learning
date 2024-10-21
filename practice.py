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
# Assuming that a password should contain atleast 8 characters
# Assumung that it should contain at least one capital letter, one small letter, one special character @ , . / ! 

#def _check_password_strength(password):

# *args is used for non-keyworded variable length argument list 

def test_var_args(f_arg, *argv):
    print('first normal arg', f_arg)
    for arg in argv:
        print('another arg through *argv', arg)
test_var_args('lol','hello','there','how','are','you') 

def ML_models(par1, *otherparameters):
    print('first must have parameter',par1)
    for par in otherparameters:
        print('other parameters for the ML model include *otherparameters', par)
ML_models('MAPE','iloc','ts_index')

import pandas as pd
class TimeSeries:
    def __init__(self, data= None, file_path=None, sheet_name=None):
        """
        Initialize the TimeSeries object with either CSV/ excel.
        """
        self.data = None

        if isinstance(data , str):
            if data.endswith('.csv'):
                self.data = self._convert_to_dataframe(data)
        elif isinstance(data, pd.DataFrame):
            self.data = data

def test_debug(word: str):

    print('Hello', word)

test_debug(21)


        

