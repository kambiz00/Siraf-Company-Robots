def date():
    path = input('Please Enter the date we are in (1401_11):  ')
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


files_path = {
    "date": date(),
    "hedayat_tarakonesh": hedayat_tarakonesh_menha_10()
}
