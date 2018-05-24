#1 DONE

def get_group():
	group = input("Group: ")
	member = input("Member Name: ")

	info = {}
	info[group] = [member]

	again = True
	again2 = True
	while again == True:
		response = input("Would you like to add a new member in your group? (Y or N) ").lower()

		if response == 'y':
			member = input("Who are your new members? ")
			info[group].append(member)

		elif response == 'n':
			while again2 == True:
				response2 = input("Would you like to add a new group? (Y or N) ").lower()
				if response2 == 'y':
					group = input("Group: ")
					member = input("Member Name: ")
					container = {}
					container[group] = [member]
					info.update(container)
					break


				elif response2 == 'n':
					again = False
					again2 = False


	print(info)

get_group()


#2 DONE

def insert_data(list1, input1):

	input1 = [input1]
	new_list = list1 + input1


	return new_list

sample_list = [1,2,3,4,5]
print(insert_data(sample_list,6))


#3 DONE

def return_odd(list1):

	new_list = []

	for i in list1:
		if i % 2 != 0:
			new_list.append(i)

	return new_list

sample_list = [1,2,3,4,5]
print(return_odd(sample_list))

#4 DONE

def list_into_integer(list1):

	result = "".join(str(i) for i in list1)
	return int(result)

sample_list = [1,2,3]
print(list_into_integer(sample_list))

#5 DONE

def sort(list1):
	list1.sort()
	return list1


sample_list = [9,7,4,6,11,15,8]
print(sort(sample_list))

#6 DONE

def is_empty(list1):
	if not list1:
		return True
	else:
		return False


sample_list = [9,7,4,6,11,15,8]
print(is_empty(sample_list))

#7 DONE

def array_into_dict(list1,list2):

	new_dict = {}
	count = 0
	for i in list1:

		for y in list2:
			new_dict[i] = list2[count]

			break
		count += 1
	return new_dict

list1 = ['moe', 'larry', 'curly']
list2 = [30, 40, 50]
print(array_into_dict(list1,list2))


#8 DONE

def remove_duplicate(sample_list):

	unique_list = []
	for i in sample_list:
		if i not in unique_list:
			unique_list.append(i)
	return unique_list


sample_list = [1,2,3,3,1,2,6,5]
print(remove_duplicate(sample_list))


#9 DONE

def get_unique(list1):

	new_list = []
	another_list = []

	for i in list1:
		if i not in new_list:		
			new_list.append(i)
		else:
			another_list.append(i)
	
	new_list = [i for i in new_list if i not in another_list ] 

	return new_list


sample_list = [1,2,3,1,3]
print(get_unique(sample_list))



#10 DONE

def get_index(list1, input1):

	count = 0
	for i in list1:
		if input1 == list1[count]:
			return count
		elif input1 not in list1:
			return ("Not in list")
		count += 1

sample_list = [1,3,4]
print(get_index(sample_list, 4))

#11 DONE

def key_value(list1,input_dict):

	for i in list1:

		for i_key, i_value in i.items():

			for input_key, input_value in input_dict.items():

				if input_value == i_value:
					return i

sample_list = [{1: 'one', 'index': 0 }, {2: 'two', 'index': 1},{3: 'three', 'index': 2}] 
print(key_value(sample_list, {'index': 1}))

#12 DONE

def is_present(list1,input1):

	for i in list1:
		if input1 in list1:
			return True
		elif input1 not in list1:
			return False

			
sample_list = [1,2,3,3,1,2,6,5]
print(is_present(sample_list, 3))


#13 DONE

def return_not_present(list1, list2):

	new_list = []

	for i in list1:
		for y in list2:
			if i not in list2:
				if i not in new_list:
					new_list.append(i)


	return new_list
list1 = [1,3,6,7,8,9]
list2 = [1,3,6]

print(return_not_present(list1,list2))

#14 DONE

def if_not_int(list1):
	new_list = []
	for i in list1:
		if type(i) == int:
			new_list.append(i)

	return new_list

			
sample_list = [2,'a', '2', {1: 'one'}]
print(if_not_int(sample_list))


#15 DONE

def display_lists(list1,list2):

	count = 0
	for i in list1:

		print (i, end = " ")

		for y in list2:
			print (list2[count])
			break
		count += 1

list1 = ['a', 'b', 'c']
list2 = ['x', 'y', 'z']
display_lists(list1,list2)


#16 DONE

sample_string = "2535"

new_list = [int(i) for i in sample_string]

print(new_list)
