

cat = {'name' : 'zophie', 'age' : 7, 'color': 'grey'}

#We can also have a list of this dict

allcats =[]

allcats.append({'name' : 'zophie', 'age' : 7, 'color': 'grey'})
allcats.append({'name' : 'pixel', 'age' : 8, 'color': 'black'})
allcats.append({'name' : 'silky', 'age' : 1, 'color': 'white'})
allcats.append({'name' : 'sweetie', 'age' : 1, 'color': 'grey'})

#print(allcats)


##############################################################################################################

#Tic Tac Toe game

theBoard = {'top-L': ' ', 'top-M' : ' ', 'top-R' : ' ', 'mid-L': ' ', 'mid-M' : ' ', 'mid-R' : ' ', 'low-L': ' ', 'low-M' : ' ', 'low-R' : ' ' }
import pprint
#pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'
theBoard['mid-L'] = 'O'
theBoard['mid-R'] = 'X'
theBoard['low-M'] = 'O'
pprint.pprint(theBoard)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('-----')

printBoard(theBoard)

###############################################################################################################

#type function

print(type(42))
print(type(3.14))
print(type(theBoard))
print(type(theBoard['top-R']))



