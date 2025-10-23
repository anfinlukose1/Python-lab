my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
print("Original:", my_dict)

asc = dict(sorted(my_dict.items()))
print("Ascending:", asc)

desc = dict(sorted(my_dict.items(), reverse=True))
print("Descending:", desc)
