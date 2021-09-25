def print_odd(test_list) :
	for i in test_list:
		if i % 2 != 0:
			yield i

# initializing list
test_list = [1, 4, 5, 6, 7]

# printing initial list
print ("The original list is : " + str(test_list))

# printing odd numbers
print ("The odd numbers in list are : ", end = " ")
for j in print_odd(test_list):
	print (j, end = " ")
