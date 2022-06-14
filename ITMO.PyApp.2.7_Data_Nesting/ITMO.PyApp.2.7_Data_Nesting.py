print("Practice 2. Data processing")
print("Data nesting")
print('')

rec = {'name': {'firstname': 'Bob', 'lastname': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 25}

print(rec['name']['firstname'], rec['name']['lastname'], " - First name and last name")
print(rec['name']['firstname'], " - Only first name")
rec['job'].append('janitor'),
print(rec['job'], " - Updated positions list with position janitor")
print('')

print(rec['name']['firstname'], rec['name']['lastname'], rec['job'], rec['age'])