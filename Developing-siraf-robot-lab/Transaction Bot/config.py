# define a function to get the current year from the user
def what_year_are_we_in():
    path = input('Please Enter the year we are in (01):  ')
    if path:
        return path
    else:
        # if the user entered an invalid value, prompt them to try again
        print("Invalid path, try again!")
        what_year_are_we_in()


# define a function to get the current month from the user
def what_month_are_we_in():
    path = input('Please Enter the month we are in (08):  ')
    if path:
        return path
    else:
        # if the user entered an invalid value, prompt them to try again
        print("Invalid path, try again!")
        what_month_are_we_in()


# define a function to get the file path for the 1 to 31 month file from the user
def month_1_31():
    path = input('Please enter your 1 to 31 month file path:  ')
    # path = '1-13_21-29_esfand01.xlsx'
    if path:
        return path
    else:
        # if the user entered an invalid value, prompt them to try again
        print("Invalid path, try again!")
        month_1_31()


# define a function to get the file path for the cumulative terminal file from the user
def cumulative_terminal():
    path = input('Please enter your cumulative terminal file path:  ')
    # path = 'Cumulative Terminals until 02.01.15.xlsx'
    if path:
        return path
    else:
        # if the user entered an invalid value, prompt them to try again
        print("Invalid path, try again!")
        cumulative_terminal()


# define a function to get the file path for the zero transaction file from the user
def zero_transaction():
    path = input('Please enter your zero transaction file path:  ')
    # path = 'zero_terminals.xlsx'
    if path:
        return path
    else:
        # if the user entered an invalid value, prompt them to try again
        print("Invalid path, try again!")
        zero_transaction()


# define a dictionary of file paths, obtained from user input via the above functions
files_path = {
    'year': what_year_are_we_in(),
    'month': what_month_are_we_in(),
    'month_1_31': month_1_31(),
    'zero_transaction': zero_transaction(),
    'cumulative_terminal': cumulative_terminal()
}
