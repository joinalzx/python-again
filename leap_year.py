year = input("Enter year ")
year = int (year)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
else:
    print("No")

print(year, "is leap year")