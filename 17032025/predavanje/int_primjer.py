str_num = "10"
int_num = int(str_num)
print(int_num, type(int_num))


float_num = 10.5
int_num_from_float = int(float_num)
print(int_num_from_float, type(int_num_from_float))


bool_val = True
bool_int = int(bool_val)
print(bool_int, type(bool_int))


bool_val = False
bool_int = int(bool_val)
print(bool_int, type(bool_int))


str_val = "345353a312"  # javlja gresku
str_val_to_int = int(str_val)
print(str_val_to_int, type(str_val_to_int))
