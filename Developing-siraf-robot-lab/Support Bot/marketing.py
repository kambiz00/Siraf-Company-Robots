import numpy as np
from jdatetime import datetime, timedelta
from config import files_path
import pandas as pd
from cli import Style

# Convert the date string to a datetime object
date = datetime.strptime(files_path["date"], '%Y_%m').date()

# Calculate the last month's date
last_month_date = date.replace(day=1) - timedelta(days=1)
last_month_date = last_month_date.strftime('%Y_%m')


class Marketing:

    def __init__(self, hedayat_tarakonesh_path, last_month_marketing_path, terminal_worked_path):
        self.hedayat_tarakonesh_path = hedayat_tarakonesh_path
        self.last_month_marketing_path = last_month_marketing_path
        self.terminal_worked_path = terminal_worked_path

    def create_last_month_marketing(self):
        # Read the last month marketing file
        print("reading last month marketing file")
        df = pd.read_excel(self.last_month_marketing_path)

        # Add the date column to the last month marketing file
        print("adding date to last month marketing file")
        df.insert(0, "تاریخ", last_month_date)

        print(Style.GREEN + "last month marketing file created" + Style.RESET)
        return df

    def create_marketing_sheet1(self, last_month_marketing):
        # Read the terminal worked file
        print("reading terminal worked file")
        terminal_worked_file = pd.read_excel(self.terminal_worked_path)

        # Create the base of the marketing dataframe
        print("creating base of marketing")
        required_data = {
            "تاریخ": date,
            "شماره ترمینال": terminal_worked_file["شماره ترمینال"],
            "نوع درخواست": terminal_worked_file["نوع درخواست"],
            "تعداد": terminal_worked_file["تعداد"],
            "مبلغ": terminal_worked_file["مبلغ"],
            "تاریخ نصب": terminal_worked_file["تاریخ نصب"],
            "ماه بعد": None,
            "فروش و غیر فروش ": None,
            "مبلغ فرمول ": None,
        }

        df = pd.DataFrame(required_data)

        # Merge both marketing dataframes
        print("merging both marketing dataframes")
        df = pd.concat([last_month_marketing, df], ignore_index=True)

        # Add 3 more columns to the dataframe
        print("adding 3 more columns to our dataframe...")
        df['فروش و غیر فروش '] = df['نوع درخواست'].apply(lambda x: 'فروش' if x == 'فروش' else 'غیرفروش')

        hedayat_tarakonesh_df = pd.read_excel(self.hedayat_tarakonesh_path)

        # Calculate the sum of purchases for each terminal
        summed_data = hedayat_tarakonesh_df.groupby('شماره ترمینال')['تعداد خرید'].sum().reset_index()

        # Fill the "ماه بعد" column based on the summed_data
        df['ماه بعد'] = df['شماره ترمینال'].apply(
            lambda x: summed_data.loc[summed_data['شماره ترمینال'] == x, 'تعداد خرید'].values[0] if x in summed_data[
                'شماره ترمینال'].values else 0)
        df.loc[df['تاریخ'] == date, 'ماه بعد'] = np.nan

        lookup_data = pd.DataFrame({'K': [1, 21, 41, 81, 151],
                                    'L': [20, 40, 80, 150, 100000],
                                    'M': [30000, 80000, 120000, 170000, 200000],
                                    'N': [36000, 96000, 144000, 204000, 240000]})

        def lookup(x, lookup_table):
            # Perform a lookup in the lookup_table based on the value of x
            idx = lookup_table['K'].searchsorted(x, side='right') - 1
            if idx < 0:
                return 0
            return lookup_table.iloc[idx, 3]

        # Apply the lookup function to calculate the "مبلغ فرمول " column
        df["مبلغ فرمول "] = df['ماه بعد'].apply(lambda x: lookup(x, lookup_data))
        df.to_excel("marketing_sheet1.xlsx")
        print(Style.GREEN + "marketing file sheet1 created" + Style.RESET)
        return df

    @staticmethod
    def create_marketing_main_data(marketing_sheet1):
        # Calculate various metrics based on the marketing_sheet1 dataframe
        print("reading marketing file sheet1...")
        print("creating marketing file main data")
        current_month_sales_len = (
                    (marketing_sheet1['فروش و غیر فروش '] == "فروش") & (marketing_sheet1['تاریخ'] == date)).sum()
        current_month_unsold_len = (
                    (marketing_sheet1['فروش و غیر فروش '] == "غیرفروش") & (marketing_sheet1['تاریخ'] == date)).sum()
        sum_of_non_sale_previous_month = marketing_sheet1.loc[
            (marketing_sheet1['تاریخ'] == date) & (
                        marketing_sheet1['فروش و غیر فروش '] == "غیرفروش"), 'مبلغ فرمول '].sum()
        count_non_sales_previous_month = len(marketing_sheet1[(marketing_sheet1['مبلغ فرمول '] > 0) & (
                marketing_sheet1['فروش و غیر فروش '] == "غیرفروش") & (marketing_sheet1['تاریخ'] == last_month_date)])

        df = pd.DataFrame({
            "تاریخ": [date],
            "تعداد فروش ماه فعلی": [current_month_sales_len],
            "تعداد غیر فروش ماه فعلی": [current_month_unsold_len],
            "جمع مبلغ غیر فروش ماه قبل": [sum_of_non_sale_previous_month],
            "تعداد غیر فروش های ماه قبل": [count_non_sales_previous_month],
        })
        df.to_excel("marketing_main_data.xlsx")
        print(Style.GREEN + "marketing file main data created" + Style.RESET)
        return df

    def start(self):
        # Start the marketing file creation process
        print(
            Style.YELLOW + "! if you don't have the last month marketing file dont forget to create it." + Style.RESET)
        print("creating last month marketing...")
        last_month_marketing = self.create_last_month_marketing()
        print("creating marketing...")
        marketing_sheet1 = self.create_marketing_sheet1(last_month_marketing)
        marketing = self.create_marketing_main_data(marketing_sheet1)
        print(Style.CYAN + "Marketing File Created Successfully!" + Style.RESET)
        return marketing
