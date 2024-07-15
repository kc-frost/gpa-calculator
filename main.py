# global variable for easier access
# keys: semesters
# values: courses as dictionaries held in a list (list of dictionaries)
user_grades = {}

def main():
    semester_count = int(input("Amount of Semesters: "))

    for s in range(semester_count):
        semester_name = input("Semester Name: ").upper()
        course_as_list = []

        print()

        course_name = input(f"Course #1: ").upper()
        course_num = 2

        while course_name != "":
            course_grade = input("Grade: ").upper()

            while not course_grade:
                course_grade = input("Grade: ").upper()
            
            if course_grade.isdigit():
                course_grade = int(course_grade)

            course_credits = input("Credit Hours: ")
            letter_grade, course_points = grade_to_points(course_grade, float(course_credits))

            course_info = (course_name, letter_grade, course_points, course_credits)

            course_as_list.append(enter_course_info(semester_name, course_info))
            
            print("\n[Enter] to stop")
            course_name = input(f"Course {course_num}: ").upper()
            course_num += 1
        
        user_grades[semester_name] = course_as_list
    
    print()
    print_user_grades()
    
def enter_course_info(semester_name, course_info):
    course_titles = ("Name", "Letter Grade", "Points", "Credit Hours")
    course_as_dict = {}

    for title, info in zip(course_titles, course_info):
        course_as_dict[title] = info

    return course_as_dict

def grade_to_points(course_grade, course_credits):
    grade_thresholds = {"A+" : 97.00, "A" : 93.00, "A-" : 90.00,
                        "B+" : 87.00, "B" : 83.00, "B-" : 80.00,
                        "C+" : 77.00, "C" : 73.00,
                        "D" : 65.00, "F" : 0}

    conversion_dict = {"A+" : 4.00, "A"  : 4.00, "A-" : 3.67,
                       "B+" : 3.33, "B"  : 3.00, "B-" : 2.67,
                       "C+" : 2.33, "C"  : 2.00,
                       "D"  : 1.00, "F"  : 0.00}
    
    # converts course_grade into a letter if it was originally an integer
    if isinstance(course_grade, int):
        for letter, threshold in grade_thresholds.items():
            if course_grade >= threshold:
                return letter, conversion_dict[letter] * course_credits
            
    else:
        return course_grade, conversion_dict[course_grade] * course_credits

def calculate_gpa():
    gpas_dict = {}

    total_hours = 0
    total_points = 0

    # calculates gpa of each semester and adds their totals
    # to total_hours and total_points for cumulative gpa calculation
    for semester, list_of_courses in user_grades.items():
        semester_hours = 0
        semester_points = 0

        for info in list_of_courses:
            semester_hours += int(info.get("Credit Hours", 0))
            semester_points += int(info.get("Points", 0))
            
        if semester_hours > 0:
            semester_gpa = round(semester_points/semester_hours, 2)
        else:
            semester_gpa = 0
        
        gpas_dict[semester] = semester_gpa

        total_hours += semester_hours
        total_points += semester_points

    # avoids division by 0
    if total_hours == 0:
        return 0
    
    cumulative_gpa = round(total_points / total_hours, 2)
    gpas_dict["Cumulative"] = cumulative_gpa

    return gpas_dict

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
            print_user_gpas()
        if i < (total_semesters - 1):
            i += 1
            input("[Enter] to continue")
            print()
            
def print_user_gpas():
    gpas_dict = calculate_gpa()

    for time, gpa in gpas_dict.items():
        print(f"{time}: {gpa}")


if __name__ == "__main__":
    main()
