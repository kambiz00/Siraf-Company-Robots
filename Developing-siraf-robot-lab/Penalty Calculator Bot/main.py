from read_files import df
import pandas as pd
from functions import *

if __name__ == "__main__":
    # Check for penalty at all
    df = check_for_penalty_at_all(df)

    # Apply installation date calculation to "تاریخ نصب" column
    df["تاریخ نصب"] = df["تاریخ نصب"].apply(installation_date_calc)

    # Check if the date is older than sixty
    df["it's in range"] = df["تاریخ نصب"].apply(it_older_than_sixty)

    # Apply installation date calculation to "تاریخ" column
    df["month number"] = df["تاریخ"].apply(installation_date_calc_month)

    # Document the difference
    df = document_difference(df)

    # Calculate complaints
    df = calculate_complaint(df)

    # Group by 'شماره ترمینال' and calculate the sum of 'em' and 'pm'
    df_group_by_em_pm = df.groupby('شماره ترمینال', as_index=False, dropna=False)[["em", "pm"]].sum()

    # Calculate the zero 'em' and 'pm' cases
    df_group_by_em_pm = calculate_zero_em_pm(df_group_by_em_pm)

    # Set 'شماره ترمینال' as the index
    df_group_by_em_pm.set_index("شماره ترمینال", inplace=True)

    # Group by 'شماره ترمینال' and calculate the sum of 'تعداد خرید'
    df_group_by_purchase = df.groupby('شماره ترمینال', as_index=False, dropna=False)['تعداد خرید'].sum()

    # Calculate the average purchase for two months
    df_group_by_purchase["میانگین خرید دو ماه"] = df_group_by_purchase['تعداد خرید'] / 2

    # Calculate the under 60 purchase cases
    df_group_by_purchase = calculate_under_60_purchase(df_group_by_purchase)

    # Set 'شماره ترمینال' as the index
    df_group_by_purchase.set_index("شماره ترمینال", inplace=True)

    # Set 'شماره ترمینال' as the index
    df.set_index("شماره ترمینال", inplace=True)

    # Filter the dataframe to include only rows with the current month number
    df_only_this_month = df.loc[df["month number"] == today_date.month]

    # Filter the dataframe to include only rows with the last month number
    df_only_last_month = df.loc[df["month number"] == today_date.month - 1]

    # Disable the chained assignment warning
    pd.options.mode.chained_assignment = None

    # Calculate "em and pm penalty" for rows in the current month if the month number is even
    if today_date.month % 2 == 0:
        df_only_this_month["em and pm penalty"] = df_only_this_month.index.map(df_group_by_em_pm["calculate_pm_em"])

    # Calculate "میانگین خرید دو ماه" for rows in the current month
    df_only_this_month["میانگین خرید دو ماه"] = df_only_this_month.index.map(
        df_group_by_purchase["میانگین خرید دو ماه"])

    # Calculate "purchase penalty" for rows in the current month
    df_only_this_month["purchase penalty"] = df_only_this_month.index.map(df_group_by_purchase["purchase penalty"])

    # Remove penalty from rows that are in range
    df_only_this_month = remove_penalty_from_in_range(df_only_this_month)

    # Concatenate the rows from the last month and the current month
    one_step_remain_to_purchase_penalty = pd.concat([df_only_last_month, df_only_this_month], axis=0)

    # Calculate the suspect score
    df = calculate_suspect_score(one_step_remain_to_purchase_penalty)

    # Reset index and set 'ردیف' as the new index
    df = df.reset_index().set_index('ردیف')

    # Group by 'شماره ترمینال' and calculate the sum of 'suspect score'
    df_group_by_suspect_score = df.groupby('شماره ترمینال', as_index=False, dropna=False)["suspect score"].sum()

    # Set 'شماره ترمینال' as the index
    df_group_by_suspect_score.set_index("شماره ترمینال", inplace=True)

    # Set 'شماره ترمینال' as the index
    df.set_index("شماره ترمینال", inplace=True)

    # Filter the dataframe to include only rows with the current month number
    df_only_this_month = df.loc[df["month number"] == today_date.month]

    # Filter the dataframe to include only rows with the last month number
    df_only_last_month = df.loc[df["month number"] == today_date.month - 1]

    # Calculate "suspect score" for rows in the current month
    df_only_this_month["suspect score"] = df_only_this_month.index.map(df_group_by_suspect_score["suspect score"])

    # Create a new column for score calculation
    df_only_this_month = new_column_for_score(df_only_this_month)

    # Concatenate the rows from the last month and the current month
    df = pd.concat([df_only_last_month, df_only_this_month], axis=0)

    # Apply penalty 1005
    df = penalty_1005(df)

    # Remove unnecessary penalty
    df = remove_unecceray_penalty(df)

    # Filter the dataframe to include only rows with the current month number
    df = df.loc[df["month number"] == today_date.month]

    # Save the dataframe to an Excel file
    df.to_excel(f'penalty {today_date.month}.xlsx')

    # Print "Done" when the execution is finished
    print("Done")
