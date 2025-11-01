import time
import random
import os
a = 0
for x in range(5):
    while True:
        # Number Generation
        seed_number = random.randint(1111111, 9999999)
        random.seed(seed_number)
        randd = random.randrange(999, 100000, 2)
        # Created file
        if os.path.exists("counter.txt"):
            with open ("counter.txt", "a+") as file:
                file.seek(0)
                content = file.read() 
                if str(seed_number) in content and str(randd) in content:
                    continue
                else:
                    file.write(f"The seed Number: {seed_number} \nThe Random number is: {randd}\n")
                    file.write("Uploaded\n")
                    time.sleep(0.5)
                    print(f"The seed Number: {seed_number} \nThe Random number is: {randd}")
                    print("New Data Append Successfully\n")
        # New file creation
        else:
            if not os.path.exists("counter.txt"):
                with open ("counter.txt", "a+") as file:
                    file.write(f"The seed Number: {seed_number} \nThe Random number is: {randd}\n")
                    print("New File Created")
                    print(f"The seed Number: {seed_number} \nThe Random number is: {randd}")
        User_Input = input("Any seed Number: ")
        # Search in the file
        count = len(User_Input)
        if User_Input == "":
            pass
        elif count < 7 and count > 7:
            with open("counter.txt", "r") as f:
                f.seek(0)
                cont = f.read()
                if f"The seed Number: {User_Input}" in cont:
                    print("Data Found...")
                    lines = cont.splitlines()
                    for i, line in enumerate(lines):
                        if f"The seed Number: {User_Input}" in line:
                            print(line)
                            if i + 1 < len(lines):
                                print(lines[i + 1],"\nOld data Fetched")
            
        else:
            print("please use the exact number")
        a += 1
        if a == 5:
            break
    # Break
    user = input("Press Enter to Continue....\nPress 'q' to Quit: ")
    if user.lower() == "q":
        break
    else:
        pass
          


         
