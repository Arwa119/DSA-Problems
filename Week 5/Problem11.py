
students = ["Ali", "Muhammad", "Fatima", "Maryam", "Ahsan"]

def search_student(name):
    if name in students:
        index = students.index(name)
        print(f"{name} -> found at index {index}.")
    else:
        print(f"{name} -> not found in list.")

if __name__ == "__main__":
    search_student("Fatima") 
    search_student("Muntaha") 