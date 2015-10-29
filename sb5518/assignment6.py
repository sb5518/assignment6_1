__author__ = 'sb5518'



"""

This program requests input from user. First, user should input a list of comma separated intervals. Intervals can have closed or open bounds. Some examples of intervals would be:

[1,4] represents the numbers 1 through 4
(2,5] represents the numbers 3 through 5
[4,8) represents the numbers 4 through 7
(3,9) represents the numbers 4 through 8.

Any input that is not a list of intervals would be considered invalid, and the program will request input again until a valid list of intervals is introduced.

Afterwards, the program will request the user to input a new interval. If input is invalid, the program will again ask for input. A valid interval followed by any
other character will be considered valid input and the program will consider only the first part of the input as an interval.

Finally, the program will try to merge all the intervals and provide a new list of intervals as merged as possible.

It is important to clarify that if some intervals are merged, the resulting interval will be a valid representation of an open bounds interval.

The only way to exit the program is by writing "quit"

Thanks!

"""



from interval import interval
import sys

print "\n"
is_interval_list_valid = False

while is_interval_list_valid == False:    #Loop until we get a valid list of intervals
    try:
        user_list_input = raw_input("List of intervals? ")
    except: (KeyboardInterrupt, EOFError)  #avoid interrupting the program

    user_list_input = user_list_input.replace(" ","")
    my_string_list = user_list_input.split(",")
    my_intervals_list = []
    for i in range(0,len(my_string_list),2):
        try:
            new_string_interval = my_string_list[i] + "," + my_string_list[i+1]
            new_interval = interval(new_string_interval)
            my_intervals_list.append(new_interval)
            is_interval_list_valid = True
        except:   #If one of the errors of the class is raised, then the user input is invalid.
            "\n"
            print "Invalid List of Intervals. Please correct it"
            is_interval_list_valid = False
            break


user_interval_input = "hey"

while user_interval_input <> "quit":    #Introducing the word "quit" is the way to exit the program
    try:
        user_interval_input = raw_input("Interval? ")
    except: (KeyboardInterrupt, EOFError)  #avoid interrupting the program

    user_interval_input = user_interval_input.replace(" ","")

    try:
        new_interval = interval(user_interval_input)
        my_intervals_list = interval.insert(my_intervals_list, new_interval)
        new_list_string = ""
        for i in my_intervals_list:
            new_list_string += str(i)
            new_list_string += ", "
        new_list_string = new_list_string[:-2]
        print new_list_string

    except:   #If one of the errors of the class is raised, then the user input is invalid.
        "\n"
        if user_interval_input <> "quit":
            print "Invalid interval"
        is_interval_list_valid = False
        continue


print "Bye Bye!"
sys.exit()

