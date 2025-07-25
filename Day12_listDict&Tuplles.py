keys = ['name', 'age', 'job']
values = ['Alice', 30, 'Engineer']

person_dict = dict(zip(keys, values))
print("Dictionary:", person_dict)
print()

keys_tuple = tuple(keys)
values_tuple = tuple(values)

print("Keys Tuple:", keys_tuple)
print("Values Tuple:", values_tuple)
print()

person_dict['country'] = 'USA'
person_dict['age'] = 31
removed_job = person_dict.pop('job')

print("Updated Dictionary:", person_dict)
print("Removed Job:", removed_job)
print()

keys.append('country')
values.append('USA')
values.remove(30)

print("Updated Keys List:", keys)
print("Updated Values List:", values)
print()

print("Index of 'Alice' in values_tuple:", values_tuple.index('Alice'))
print("Count of 'Engineer' in values_tuple:", values_tuple.count('Engineer'))
print()