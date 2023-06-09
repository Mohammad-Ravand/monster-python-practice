person = {'name': 'John', 'age': 25, 'country': 'USA'}

# the type of person is dict
print(type(person))

# Define a string template with placeholders
template = "My name is '{name}', I am '{age}' years old, and I live in '{country}'."

# Use format_map() to substitute the placeholders with values from the mapping object
formatted_string = template.format_map(person)

print(formatted_string)
