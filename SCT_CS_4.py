print("=================================")
print("        KEY LOGGER TOOL")
print("=================================")
choice = "y"
while choice == "y":

    text = input("\nEnter Text : ")

    file = open("keylog.txt", "a")

    file.write(text + "\n")

    file.close()

    print("Data Logged Successfully!")

    choice = input("Do you want to continue? (y/n) : ")
print("\n=================================")
print("Data Saved in keylog.txt")
print("Program Closed Successfully!")
print("=================================")