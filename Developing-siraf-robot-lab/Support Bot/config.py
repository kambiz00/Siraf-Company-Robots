def date():
    path = input('Please Enter the date we are in (1401_12):  ')
    if path:
        return path
    else:
        print("Invalid path, try again!")
        date()


def hedayat_tarakonesh_menha_10():
    path = input('Please enter your hedayat_tarakonesh_menha_10 file path:  ')
    if path:
        return path
    else:
        print("Invalid path, try again!")
        hedayat_tarakonesh_menha_10()


def last_month_marketing_file():
    path = input('Please enter your last month marketing file path:  ')
    if path:
        return path
    else:
        print("Invalid path, try again!")
        last_month_marketing_file()


def terminal_worked_file():
    path = input('Please enter your terminal worked file path:  ')
    if path:
        return path
    else:
        print("Invalid path, try again!")
        terminal_worked_file()


files_path = {
    "date": date(),
    "hedayat_tarakonesh": hedayat_tarakonesh_menha_10(),
    "last_month_marketing": last_month_marketing_file(),
    "terminal_worked": terminal_worked_file()
}
