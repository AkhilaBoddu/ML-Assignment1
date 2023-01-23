dog={}
dog['name'] = 'rocky'
dog['colour'] = 'black'
dog['breed'] = 'rottweiler'  # added items to the dog dictionary
dog['legs'] = 'normal'
dog['age'] = '1year'
student = {
    'first_name': 'Akhila',
    'last_name': 'Boddu',
    'Gender': 'Female',             # created student dictionary
    'age': 22,
    'marital status': 'single',
    'skills': ['Java', 'C', 'Python'],
    'country': 'INDIA',
    'address': 'HELLO street',
    'City': 'Warangal',
}
print("the length of student dictionary", len(student))   # Get the length of the student dictionary
print("the skills of student", student.get('skills'))     # to get the value of skills
print(type(['skills']))                                     # for datatype
student['skills'].append('HTML')  # two skills added
student['skills'].append('c++')
print("ATER UPDATING skills",student)
key = student.keys()              # for keys as list
print(key)
val = student.values()           # for values as list
print(val)