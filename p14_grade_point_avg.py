#5 grades point average and more

grades= []
print("Grades 0-100")
grade_number =  int(input("How many grades do you want to enter: "))  

def grade_collect(n):
    for i in range(n):
        grade_entered = int(input("Enter Grade: "))
        if(grade_entered == 0 or grade_entered >100):
            print("Error! Incorrect Value. Try again")
            grade_entered = int(input("Enter Grade: "))
        grades.append(grade_entered)
    
def grade_avg(grades_lst):
    sum = 0
    for i in range(len(grades_lst)):
        sum = sum + grades_lst[i]
    return(sum/len(grades_lst))

def print_sorted_grade(grades_lst):
    sorted_g = sorted(grades_lst,reverse=True)
    print("Sorted Grades are: ")
    for i in sorted_g:
        print("        ",i)

def summary_grd(grades_lst):
    print("General Summary: ")
    print("Total number of grades:  ",len(grades_lst))
    print("The highest grade is:    ",max(grades_lst))
    print("The lowest grade is:     ",min(grades_lst))
    print("The Average is:          ",grade_avg(grades_lst))

def next_grade_toget_avg(grades):
    print("Your current avg is: ",sum(grades)/len(grades))
    to_avg = int(input("What is your desired avg? "))
    nxt_grade_req = (to_avg *2)-sum(grades)/len(grades)
    while(nxt_grade_req > 100):
        print("Unacheivable Average. Choose again.")
        to_avg = int(input("What is your desired avg? "))
        nxt_grade_req = (to_avg *2)-sum(grades)/len(grades)
    print('\n')
    print("You have to get atleast {} for your next grade to get the desired average".format(nxt_grade_req))

def change_grade(grades):
    print("You can change one grade.")
    chnge_grd = int(input("Which grade to change? "))
    chnge_grd_with = int(input("Change grade with what? "))
    grades[grades.index(chnge_grd)]=chnge_grd_with
    



grade_collect(grade_number)
print_sorted_grade(grades)
summary_grd(grades)
print('\n')
next_grade_toget_avg(grades)
change_grade(grades)
summary_grd(grades)
