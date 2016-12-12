# list = []
# n = 0
# while n <= 10:
#     food = input("Please name a food ")
#     list.append(food)
#     n += 1

# for n in range(0,10):
#     print(n, ".", food)
#     n+=1
    
file = open('mylist.txt', 'w')
 
#add items to list with for loop
for n in range(10):
    file.write(str(n + 1) + "." + input("Food! ") + '\n')

#close the file
file.close()
    