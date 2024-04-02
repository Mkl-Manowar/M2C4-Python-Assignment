import math
from decimal import Decimal

#1
list_one = ["1","carrot","onion","tomato",]
tuple_one = (1,2,3,4,5)
float_one = 2.2
integer_one = 7
decimal_one = 1.264365
decimal_one = Decimal(decimal_one)
dictionary_one = {"one":1, "two":2, "three":3}

#2
rounded_float_one = math.ceil(float_one)

#3
square_root = math.sqrt(rounded_float_one)

#4
first_element = dictionary_one["one"]

#5
second_element = tuple_one[1]

#6
list_one.append("celery")

#7
list_one[0] = "potato"

#8
list_one.sort()

#9
tuple_one += (6,)



print(list_one)





