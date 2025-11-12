def main():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    student_status = bool(input("Are you a student (True/False): "))
    hobbies = input("Enter your hobbies(comma seperated): ").split(",")
    skills = input("Enter your skills with experience (skill:years format): ")
    skills_dict = {skill.strip():int(year) for skill, year in (item.split(":") for item in skills.split(","))}

    print("Name: ", name)
    print(f"age: {age} years")
    print("Height: ", height, " m")
    print("Student status: ", student_status)
    print("Hobbies: ", hobbies)
    print("Skills: ", skills_dict)

    pass

if __name__ == "__main__":
    main()