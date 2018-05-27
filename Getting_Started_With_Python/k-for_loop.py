'''Hey as always.. Today will talk about for loop
for loop is simmiliar with while but it acts diffrent than the while loop
the syntax is:'''
for name_var in name_var2: #or range in order to define range, see examples for more infos and for the 2 name_vars
    #do these

#now lets take the following examples to see how the for loop works:
words = ["Word 1", 2, "Word 3", 4, "Word 5", 6]
for word in words:
    print(word)

'''this will output:
Word 1
2
Word 3
4
Word 5
6
====================
you see the for loop took the words into our list and print each one of them'''

#we can also use the range method in order to tell the for loop to how much times we should print
for i in range(4):
    print("this will print 4 times")

'''this will output:
this will print 4 times!
this will print 4 times!
this will print 4 times!
this will print 4 times!'''

#so now you got what for loops does, we will move into using a function to python!