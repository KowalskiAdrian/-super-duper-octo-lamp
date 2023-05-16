def my_generator():
    for num in range(50):
        yield num ** num
        
# all_numbers = list(my_generator())
# print(all_numbers)

# for big_num in my_generator():
#     print(big_num)

# total = list(range(50))
# print(total)

my_var_gen = my_generator()
all_numbers = list(my_var_gen)
print(all_numbers)

for big_num in my_generator():
    print(big_num)