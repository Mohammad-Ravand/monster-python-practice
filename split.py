title= 'learning python with practice and internet is so cool.'

words = title.split(' ')

print(type(words)) # the type of result is list
# show each word
# for word in words:
#     print(word)

# print word counts in title
print('title has '+str(len(words))+ ' words')

it_list = ['python','internet','nodejs','vuejs','devops','programming']
# get list of words in title that is sub list of it list
my_founded_list_it_words = list()
for word in words:
    if(word in it_list):
        my_founded_list_it_words.append(word)


print('my founded words is: '+str(my_founded_list_it_words))