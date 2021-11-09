a = ['CodewithHarry', 'T Series', 'Mixer Grinder', 'Pen']

#Task: print the channels which are at index 2
# i = 0
# for item in a:
#     i= i+1
#     if i%2 == 0:
#         print(item)

#Using Enumerate to perform the above task
for i, item in enumerate(a):
    if(i+1)%2 == 0:
        print(item)
