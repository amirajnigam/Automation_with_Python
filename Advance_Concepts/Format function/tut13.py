users = ['amiraj', 'rohan', 'hari', 'jay']

computer = ['raspberry pi', 'Android', 'windows', 'iphone']

# for i in range(0, len(users)):
#     print("Computer used by", users[i], "is", computer[i])


#Alternate way
for i in range(0, len(users)):
    template = "Computer used by {} is {}"
    print(template.format(users[i], computer[i]))

#Why it is useful -> we can reverse the pattern, by default the value start with 0 i nthecurly bracket
for i in range(0, len(users)):
    template = "Computer used by {1} is {0}"
    print(template.format(users[i], computer[i]))

