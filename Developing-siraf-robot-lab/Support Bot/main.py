from config import files_path
import os
from marketing import Marketing

if __name__ == "__main__":
    os.system("")
    m = Marketing(files_path["hedayat_tarakonesh"],files_path["last_month_marketing"],files_path["terminal_worked"])
    m.start()


