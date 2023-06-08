title = 'Learning docker with Docker Book'

# show just word one from title
#- the node in is here is that, last position is ignored.
print(title[0:8])

# show second word
print(title[9:15])

# show length string
print(len(title[9:15]))

# show all word except two first word in title
print(title[15:])

# show last word
# - note: we cant to get last word
print(title[-4:-1]) # we get boo without k character

print(title[(len(title)-4):]) # this solution is working :)

# this solve out problem for get last word from title
print(title.split()[-1])

# show last two word
print(title[(len(title)-11):])

# get word that is center in the title
# we have to get start and end postion
start_postion=16
end_position=20
print(title[start_postion:end_position])
