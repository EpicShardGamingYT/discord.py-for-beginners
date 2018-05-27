'''Hey! today we will discuss about loops and this time, it will be the while loop
while loop is basically a "loop" as decribed to loop a specific statement like in the if but it does it on loop!
the syntax is:'''
while condition:
    #do these tasks

'''now you can tell by the syntax, its the same as if statements, but this one is a loop
now lets give some demos about it(aka examples):'''
#a simple loop that will print numbers 6 times
i = 1
while i <=6:
    print(i)
    i += 1

#an infinite loop (its simple as it is)
while True: #or you can use values that make it true
    print("an infinite loop")

'''now were going to exaplin about break
break is a syntax that allows you to 'break'(stop) a loop by a statement
lets take this example'''
d = 0
while True:
    print(d)
    d = d + 1
    if d == 5:
        break #the break is where we make it to stop

#now if you try this code, this will do almost same thing as first, but it does it on a diffrent task

'''now lets get into the continue, what this does is that allows you to timeout a code, then continue it!
take this example:'''
a = 0
while True:
    a = a + 1
    if a == 3:
        print("on 3")
        continue
    if a == 5:
        break

#this will output a loop then if a reaches to 3, it will print "on 3" instead and continue untill the 5th number

#in the next one we will discuss about lists, this is where we sort words into python!