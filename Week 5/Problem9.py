students = []

def Remove_std(name):
    if name in students:
        students.remove(name)
    else:
        print(f"{name} is not in the list.")

def Display_std():
    if students:
        print("Students in the class are:")
        for student in students:
            print(student)
    else:
        print("No students in the list.")


def Add_std(name):
    students.append(name)

if __name__ == "__main__":
    Add_std("Ali")
    Add_std("Muhammad")
    Display_std()
    Remove_std("Ali")
    Display_std()
