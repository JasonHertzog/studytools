import datetime, pickle

# Class1, Class2, Class3, Class4.
# Calc, CS, Span, Gov
# First 4 are Monday, next 4 are Tuesday, etc. until Friday
# These are the weight percentages for each day of the week.
class_times=[.19,.10,.20,.0,
            .19,.35,.20,.33,
            .19,.10,.20,.0,
            .19,.35,.20,.34,
            .24,.10,.20,.33,
            1.00,1.00,1.00,1.00,
            1.00,1.00,1.00,1.00]
class1_name = "Calculus"
class1_total = 550
class1_time = 0
class1_today = 0
class2_name = "Computer Science"
class2_total = 370
class2_time = 0
class2_today = 0
class3_name = "Spanish"
class3_total = 50
class3_time = 0
class3_today = 0
class4_name = "American Government"
class4_total = 30
class4_time = 0
class4_today = 0

 # Used to determine if it is a different day.
last_save = datetime.datetime.today().weekday()


def get_time(c1, c2, c3, c4):
    today = datetime.datetime.today().weekday()
    # Monday is 0, Sunday is 6.
    print(c1)
    print(class1_total)
    input("!!")
    if today == 0:
        today = "Monday"
        c1 = (class1_total * class_times[0]) - class1_today
        c2 = (class2_total * class_times[1]) - class2_today
        c3 = (class3_total * class_times[2]) - class3_today
        c4 = (class4_total * class_times[3]) - class4_today
    elif today == 1:
        today = "Tuesday"
        c1 = (class1_total * (class_times[0] + class_times[0+4])) - class1_today
        c2 = (class2_total * class_times[1+4]) - class2_today
        c3 = (class3_total * class_times[2+4]) - class3_today
        c4 = (class4_total * class_times[3+4]) - class4_today
    elif today == 2:
        today = "Wednesday"
        c1 = ((class_times[0] + class_times[0+4] + class_times[0+8]) * class1_total) - class1_today
        c2 = (class_times[1+8] * class2_total) - class2_today
        c3 = (class_times[2+8] * class3_total) - class3_today
        c4 = (class_times[3+8] * class4_total) - class4_today
    elif today == 3:
        today = "Thursday"
        c1 = (class1_total * class_times[0+12]) - class1_today
        c2 = (class2_total * class_times[1+12]) - class2_today
        c3 = (class3_total * class_times[2+12]) - class3_today
        c4 = (class4_total * class_times[3+12]) - class4_today
    elif today == 4:
        today = "Friday"
        c1 = (class1_total * class_times[0+16]) - class1_today
        c2 = (class2_total * class_times[1+16]) - class2_today
        c3 = (class3_total * class_times[2+16]) - class3_today
        c4 = (class4_total * class_times[3+16]) - class4_today
    elif today == 5:
        today = "Saturday"
        c1 = (class1_total * class_times[0+20]) - class1_today
        c2 = (class2_total * class_times[1+20]) - class2_today
        c3 = (class3_total * class_times[2+20]) - class3_today
        c4 = (class4_total * class_times[3+20])  - class4_today
    elif today == 6:
        today = "Sunday"
        c1 = (class1_total * class_times[0+24]) - class1_today
        c2 = (class2_total * class_times[1+24]) - class2_today
        c3 = (class3_total * class_times[2+24]) - class3_today
        c4 = (class4_total * class_times[3+24]) - class4_today
    else:
        print("Something is broken in the datetime day checking loop.")
    return(c1, c2, c3, c4)


def todays_schedule():
    print(f"Your schedule for today is:\n"
    +str(class1_name)+":",str(class1_time)+" minutes.\n"
    +str(class2_name)+":",str(class2_time)+" minutes.\n"
    +str(class3_name)+":",str(class3_time)+" minutes.\n"
    +str(class4_name)+":",str(class4_time)+" minutes.\n"
    )
    print(f"Your total remaining time for this week:\n"
    +str(class1_name)+":",str(class1_total)+" minutes.\n"
    +str(class2_name)+":",str(class2_total)+" minutes.\n"
    +str(class3_name)+":",str(class3_total)+" minutes.\n"
    +str(class4_name)+":",str(class4_total)+" minutes.\n"
    )
def first_check(a, c1, c2, c3, c4, d1, d2, d3, d4, last_save):
    if a == "y" or a =="yes" or a =="ye":
        e1, e2, e3, e4 = 0, 0, 0, 0
        print("Let's get our day started!\n")
        filehandler = open("Study Schedule.sav","wb")
        pickle.dump(c1, filehandler)
        pickle.dump(c2, filehandler)
        pickle.dump(c3, filehandler)
        pickle.dump(c4, filehandler)
        pickle.dump(d1, filehandler)
        pickle.dump(d2, filehandler)
        pickle.dump(d3, filehandler)
        pickle.dump(d4, filehandler)
        pickle.dump(e1, filehandler)
        pickle.dump(e2, filehandler)
        pickle.dump(e3, filehandler)
        pickle.dump(e4, filehandler)
        pickle.dump(last_save, filehandler)
        filehandler.close()
        return(0, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4, last_save)
    else:
        print("Welcome back.")
        filehandler = open("Study Schedule.sav","rb")
        c1 = pickle.load(filehandler)
        c2 = pickle.load(filehandler)
        c3 = pickle.load(filehandler)
        c4 = pickle.load(filehandler)
        d1 = pickle.load(filehandler)
        d2 = pickle.load(filehandler)
        d3 = pickle.load(filehandler)
        d4 = pickle.load(filehandler)
        e1 = pickle.load(filehandler)
        e2 = pickle.load(filehandler)
        e3 = pickle.load(filehandler)
        e4 = pickle.load(filehandler)
        last_save = pickle.load(filehandler)
        filehandler.close()
        return(0, c1, c2, c3, c4, d1, d2, d3, d4, e1, e2, e3, e4, last_save)
        
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
            d1 = class1_total
            pickle.dump(d1, filehandler)
            d2 = class2_total
            pickle.dump(d2, filehandler)
            d3 = class3_total
            pickle.dump(d3, filehandler)
            d4 = class4_total
            pickle.dump(d4, filehandler)
            e1 = class1_today
            pickle.dump(e1, filehandler)
            e2 = class2_today
            pickle.dump(e2, filehandler)
            e3 = class3_today
            pickle.dump(e3, filehandler)
            e4 = class4_today
            pickle.dump(e4, filehandler)
            pickle.dump(last_save, filehandler)
            filehandler.close()

# Main algorithm
a = input("Is this the first time you're checking your schedule today? y = yes: ").strip().lower()
a, class1_time, class2_time, class3_time, class4_time, class1_total, class2_total, class3_total, class4_total, class1_today, class2_today, class3_today, class4_today, last_save = first_check(a, class1_time, class2_time, class3_time, class4_time, class1_total, class2_total, class3_total, class4_total, last_save)
class1_time, class2_time, class3_time, class4_time = get_time(class1_total, class2_total, class3_total, class4_total)
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
            temp = int(input("Time Spent (in minutes): "))
            class1_time -= temp
            class1_total -= temp
            class1_today += temp
            quicksave()
        elif b == "2":
            temp = int(input("Time Spent (in minutes): "))
            class2_time -= temp
            class2_total -= temp  
            class2_today += temp 
            quicksave()
        elif b == "3":
            temp = int(input("Time Spent (in minutes): "))
            class3_time -= temp
            class3_total -= temp
            class3_today += temp
            quicksave()
        elif b == "4":
            temp = int(input("Time Spent (in minutes): "))
            class4_time -= temp
            class4_total -= temp
            class4_today += temp
            quicksave()
        else:
            print("\n")

    elif a == "t":
        i = 0

input("Finished Running. Press enter to termiate program.")