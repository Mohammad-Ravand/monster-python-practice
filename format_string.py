def br(section='next'):
    print('\n-----{} section-----'.format(section))

age = 36
txt = "My name is John, I am " + str(age)
print(txt)


# using format method
br('format')

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


#format with index
br('index')
quantity = 3
item_number = 567
price = 49.95
member_order = "I want to pay {2} dollars for {0} pieces of item {1}."
print(member_order.format(quantity, item_number, price))



print('--------------')
name='mohammad'
age=26.5

text = 'my name is {name} i am {age} years old'
print(text.format(name=name,age=age))


print('--------------')
txt = "We have {:d} chickens."
print(txt.format(0b101))
