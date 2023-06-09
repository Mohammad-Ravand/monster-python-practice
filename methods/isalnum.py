txt = "my name is what i want to have in here for learning any think that i love and have time to do it 1"

x = txt.isalnum()

print(x) # text and title does not alqhanum

print('---sectoin two---')
txt = "myNameP1"

x = txt.isalnum() #words with number are alghanums without space

print(x)
print('---sectoin three---')
txt = "myNameP1 f"

x = txt.isalnum() #words with space does not alghanum

print(x)