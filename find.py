txt = "Hello, welcome to my world."

# find first finded index or the word
x = txt.find("welcome")

print(x)


print('\n how find all index of mohammad in the text ? ')

text = 'mohammad, how are your? name mohammad is so popular name in the world did you know?'

# how find all index of mohammad in the text
temp_word=''
mohammad_start_indexes = list()
for index,char in enumerate(text):
    if(temp_word=='mohammad'):
        mohammad_start_indexes.append(index)
    temp_word +=char
    if(char==' '):
        temp_word=''
    
# test is it true?
for start in mohammad_start_indexes:
    print(text[start-8:start])

# remove all name "mohammad" in the text
print(text.replace('mohammad','"your name" '))