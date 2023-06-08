title = 'Learning docker with Docker Book'

# find all Camel case word in the title
camel_case_chars = ''
for char in title:
    if(char == char.upper()):
        camel_case_chars += char

print(camel_case_chars)
print('\n--------first approch-------------')

# count all words in title
word_count = 0
index=0
for char in title:
    index+=1
    if(char==' '):
        word_count+=1
    elif(index==len(title)):
        word_count+=1

print('title word count is: '+str(word_count))

print('\n--------second approch-------------')
# count all words in title
word_count = 0
for index,char in enumerate(title):
    if(char==' '):
        word_count+=1
    elif(index==len(title)-1):
        word_count+=1

print('title word count is: '+str(word_count))