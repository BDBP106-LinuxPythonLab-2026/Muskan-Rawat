from utils.math_utils import add_func
from utils.math_utils import sub_func
from utils.math_utils import multiplication_func
from utils.string_utils import upper_case_func
from utils.string_utils import lower_case_func
from utils.string_utils import concatenate_func

math_add= add_func(34,45)
math_sub= sub_func(34,45)
math_multi= multiplication_func(34, 45)

words= "BdBh"
input_something = ["BDBH", "101"]
str_upper = upper_case_func(words)
str_lower = lower_case_func(words)
str_con = concatenate_func(input_something)

print('add:',math_add)
print('sub:', math_sub)
print('multiplication:', math_multi)
print('upper case:', str_upper)
print('lower case:', str_lower)
print('concatenate:', str_con)