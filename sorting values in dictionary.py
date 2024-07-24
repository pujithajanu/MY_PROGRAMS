my_dict={'Ram':1, 'Bheem':2, 'seetha':3}
my_keys=sorted(my_dict.keys())
sorted_dict={i:my_dict[i] for i in my_keys}
print(sorted_dict)
