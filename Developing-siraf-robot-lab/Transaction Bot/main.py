# Importing required modules
import os  # To interact with the operating system
from transaction import Transaction  # To work with transactions
from config import files_path  # To get the file paths from configuration

# This line clears the terminal before running the code
os.system("")

# Creating a new thread to run the animation

# Starting the animation thread

# Creating a new transaction object by passing in file paths for the input and output files
tr = Transaction(
    files_path['month_1_31'], files_path["zero_transaction"], files_path["cumulative_terminal"]
)

# Starting the transaction process
tr.start()
