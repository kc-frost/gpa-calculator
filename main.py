user_grades = {}

def main():
    semester_count = int(input("Amount of Semesters: "))

    for s in range(semester_count):
        semester_name = input("Semester Name: ").upper()
        course_list = []

        print()

        course_name = input(f"Course #1: ").upper()
        course_num = 2

        while course_name != "":
            course_letter_grade = input("Grade (Letter ONLY): ").upper()

            while not course_letter_grade or course_letter_grade.isnumeric == False:
                course_letter_grade = input("Grade (Letter ONLY): ").upper()
            
            course_credits = int(input("Credit Hours: "))
            course_points = letter_to_points(course_letter_grade, float(course_credits))

            course_info = (course_name, course_letter_grade, course_points, course_credits)

            course_list.append(enter_course_info(semester_name, course_info))
            
            print("\n[Enter] to stop")
            course_name = input(f"Course {course_num}: ").upper()
            course_num += 1
        
        user_grades[semester_name] = course_list
    
    print_user_grades()

def enter_course_info(semester_name, course_info):
    course_titles = ("Name", "Letter Grade", "Points", "Credit Hours")
    course_as_dict = {}

    for title, info in zip(course_titles, course_info):
        course_as_dict[title] = info

    return course_as_dict

def letter_to_points(course_grade, course_credits):
    conversion_dict = {"A+" : 4.00, 
                       "A"  : 4.00,
                       "A-" : 3.67,
                       "B+" : 3.33,
                       "B"  : 3.00,
                       "B-" : 2.67,
                       "C+" : 2.33,
                       "C"  : 2.00,
                       "D"  : 1.00,
                       "F"  : 0.00}
    
    return conversion_dict[course_grade] * course_credits

def calculate_gpa():
    credit_hours = 0
    credit_points = 0

    for list_courses in user_grades.values():
        for info in list_courses:
            credit_hours += info.get("Credit Hours", 0)
            credit_points += info.get("Points", 0)

    if credit_hours == 0:
        return 0
    
    return round(credit_points / credit_hours, 2)

def print_user_grades():
    total_semesters = len(user_grades)
    i = 0

    for semester, list_courses in user_grades.items():
        print(f"{semester} Semester")
        for info in list_courses:
            for title, value in info.items():
                if title == "Name":
                    print(value)
                
                else:
                    print(f"{title}: {value}")
            print()
        if i < (total_semesters - 1):
            i += 1
            input("[Enter] to continue")
            print()
            

if __name__ == "__main__":
    main()
