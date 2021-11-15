import datetime, pickle

# Class1, Class2, Class3, Class4.
# Calc, CS, Span, Gov
# First 4 are Monday, next 4 are Tuesday, etc. until Friday
class_times=[100,50,10,0,
            100,110,10,10,
            100,50,10,0,
            100,110,10,10,
            150,50,10,10]
class1_name = "Calculus"
class1_time = 0
class2_name = "Computer Science"
class2_time = 0
class3_name = "Spanish"
class3_time = 0
class4_name = "American Government"
class4_time = 0


today = datetime.datetime.today().weekday()
# Monday is 0, Sunday is 6.
if today == 0:
    today = "Monday"
    class1_time = class_times[0]
    class2_time = class_times[1]
    class3_time = class_times[2]
    class4_time = class_times[3]
elif today == 1:
    today = "Tuesday"
    class1_time = class_times[0+4]
    class2_time = class_times[1+4]
    class3_time = class_times[2+4]
    class4_time = class_times[3+4]
elif today == 2:
    today = "Wednesday"
    class1_time = class_times[0+8]
    class2_time = class_times[1+8]
    class3_time = class_times[2+8]
    class4_time = class_times[3+8]
elif today == 3:
    today = "Thursday"
    class1_time = class_times[0+12]
    class2_time = class_times[1+12]
    class3_time = class_times[2+12]
    class4_time = class_times[3+12]
elif today == 4:
    today = "Friday"
    class1_time = class_times[0+16]
    class2_time = class_times[1+16]
    class3_time = class_times[2+16]
    class4_time = class_times[3+16]
elif today == 5:
    today = "Saturday"
elif today == 6:
    today = "Sunday"
else:
    print("Something is broken in the datetime day checking loop.")

def todays_schedule():
    print(f"Today is",today+", and your schedule for today is:\n"
    +str(class1_name)+":",str(class1_time)+" minutes.\n"
    +str(class2_name)+":",str(class2_time)+" minutes.\n"
    +str(class3_name)+":",str(class3_time)+" minutes.\n"
    +str(class4_name)+":",str(class4_time)+" minutes.\n"
    )
def first_check(a, c1, c2, c3, c4):
    if a == "y" or a =="yes" or a =="ye":
        print("Let's get our day started!\n")
        filehandler = open("Study Schedule.sav","wb")
        pickle.dump(c1, filehandler)
        pickle.dump(c2, filehandler)
        pickle.dump(c3, filehandler)
        pickle.dump(c4, filehandler)
        filehandler.close()
        return(0, c1, c2, c3, c4)
    else:
        print("Welcome back.")
        filehandler = open("Study Schedule.sav","rb")
        c1 = pickle.load(filehandler)
        c2 = pickle.load(filehandler)
        c3 = pickle.load(filehandler)
        c4 = pickle.load(filehandler)
        filehandler.close()
        return(0, c1, c2, c3, c4)
        
def quicksave():
            filehandler = open("Study Schedule.sav","wb")
            c1 = class1_time
            pickle.dump(c1, filehandler)
            c2 = class2_time
            pickle.dump(c2, filehandler)
            c3 = class3_time
            pickle.dump(c3, filehandler)
            c4 = class4_time
            pickle.dump(c4, filehandler)
            filehandler.close()

# Main algorithm
a = input("Is this the first time you're checking your schedule today? y = yes: ").strip().lower()
a, class1_time, class2_time, class3_time, class4_time = first_check(a, class1_time, class2_time, class3_time, class4_time)
todays_schedule()

i = 1
while i > 0:
    print("Directory: \n0: Check Schedule.\n1: Subtract Time\nt: Terminate script")
    a = input()
    if a == str("0"):
        print('\n')
        todays_schedule()
    if a == str("1"):
        b = input("Subtract time from which class?\n1 = "+class1_name+"\n"+
        "2 = "+class2_name+"\n"+
        "3 = "+class3_name+"\n"+
        "4 = "+class4_name+"\n"
        )
        if b == "1":
            class1_time -= int(input("Time Spent (in minutes): "))
            quicksave()
        elif b == "2":
            class2_time -= int(input("Time Spent (in minutes): "))    
            quicksave()
        elif b == "3":
            class3_time -= int(input("Time Spent (in minutes): "))
            quicksave()
        elif b == "4":
            class4_time -= int(input("Time Spent (in minutes): "))
            quicksave()
        else:
            print("\n")

    elif a == "t":
        i = 0

input("Finished Running. Press enter to termiate program.")