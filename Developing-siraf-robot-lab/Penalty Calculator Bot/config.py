def what_month_are_we_in():
    path = str(input('Please Enter the date we are in (1401_01_31):  '))
    # path = "1401_06_01"
    if path:
        return path
    else:
        print("Invalid path, try again!")
        what_month_are_we_in()


