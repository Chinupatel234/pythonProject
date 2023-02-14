m = input("What type of email you want to create(google/yahoo):").strip().lower()
if m == "google":
    n = input("Enter your email id: ")
    while "@gmail.com" not in n:
        print("Invalid email id...")
        n = input("Enter your email again: ")
    else:
        print(n)
        print("Your email is taken...thank you!!!")
elif m == "yahoo":
    n = input("Enter your email id: ")
    while "@yahoo.com" not in n:
        print("Invalid email id...")
        n = input("Enter your email again: ")
    else:
        print(n)
        print("Your email is taken...thank you!!!")
