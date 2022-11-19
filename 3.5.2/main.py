month = input("Enter month: ")
if (month == "January" or month == "March" or month == "May"
    or month == "July" or month == "August"  or month == "October"
    or month == "December"):
    print("31")
elif (month == "April" or month == "June" or month == "September"
      or month == "November"):
    print("30")
elif (month == "February"):
    print("28/29")
else:
    print("Not recognized")
