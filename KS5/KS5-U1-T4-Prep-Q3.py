school = ["AAAA", "BBBB", "CCCC", "DDDD"]
medal = [4,7,1,3]

school_num = int(input("Enter Number 1 to 4, -1 to exit: "))

while school_num != -1:
    
    while (school_num < 1 or school_num > 4):
        print("Invalid Number, try again: ")
        school_num = int(input("Enter the School Number (-1 to exit): "))

    if school_num != -1:
        medal[school_num-1] = medal[school_num-1] + 1
        school_num = int(input("Enter Number 1 to 4, -1 to exit: "))

for line in range(len(school)):
    print(f"School number {line +1} School Name {school[line]} Number of medals {medal[line]}")
