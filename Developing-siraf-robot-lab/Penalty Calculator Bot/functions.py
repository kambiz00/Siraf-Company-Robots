from jdatetime import datetime
from config import what_month_are_we_in
from jdatetime import timedelta

# Convert the current date string to a datetime object
today_date = datetime.strptime(what_month_are_we_in(), '%Y_%m_%d').date()

# Calculate the date sixty days ago
sixty_days_ago = today_date - timedelta(days=60)


# Function to check for penalty in all cases
def check_for_penalty_at_all(dataframe):
    # Set "don't penalty" column to True for specific conditions
    dataframe.loc[(dataframe["جمع آوری"] == True) | (dataframe["وضعیت"] == "غيرفعال") | (
            dataframe["وضعیت"] == "غير فعالي موقت"), "dont penalty"] = True
    return dataframe


# Function to check if a target time is within a given time range
def check_is_in_time_range(start_time, target_time, end_time):
    if start_time < end_time:
        return start_time <= target_time <= end_time
    else:
        return target_time >= start_time or target_time <= end_time


# Function to check if a given date is older than sixty days
def it_older_than_sixty(tarikh_nasb):
    return check_is_in_time_range(sixty_days_ago, tarikh_nasb, today_date)


# Function to calculate installation date
def installation_date_calc(date):
    return datetime.strptime(date, "%Y_%m_%d").date()


# Function to calculate document difference penalty
def document_difference(dataframe):
    # Set "document difference penalty" column to 15000 for specific conditions
    dataframe.loc[
        (dataframe["it's in range"] == True) & (dataframe["مغایرت"] == True), "document difference penalty"] = 15000
    return dataframe


# Function to calculate penalty for zero em and pm values
def calculate_zero_em_pm(dataframe):
    # Set "calculate_pm_em" column to 25000 for specific conditions
    dataframe.loc[(dataframe["pm"] == False) & (dataframe["em"] == False), "calculate_pm_em"] = 25000
    return dataframe


# Function to calculate the month of an installation date
def installation_date_calc_month(date):
    this_month_date = datetime.strptime(date, "%Y_%m_%d").date()
    return this_month_date.month


# Function to calculate penalty for complaints in the current month
def calculate_complaint(dataframe):
    # Set "complaint_penalty" column to 25000 for specific conditions
    dataframe.loc[
        (dataframe["month number"] == today_date.month) & (dataframe["شکایت"] == True), "complaint_penalty"] = 25000
    return dataframe


# Function to calculate penalty for purchases under 60
def calculate_under_60_purchase(dataframe):
    dataframe.loc[
        (dataframe["میانگین خرید دو ماه"] <= 60), "purchase penalty"
    ] = 12000
    return dataframe


# Function to remove penalty for purchases in the given time range
def remove_penalty_from_in_range(dataframe):
    dataframe.loc[(dataframe["it's in range"] == True), "purchase penalty"] = 0
    return dataframe


# Function to calculate suspect score
def calculate_suspect_score(dataframe):
    dataframe.loc[
        (dataframe["it's in range"] == False) & (dataframe["purchase penalty"] == 12000), "suspect score"] += 1
    return dataframe


# Function to add a new column for score calculations
def new_column_for_score(dataframe):
    # Set "change score" column to True for specific conditions
    dataframe.loc[(dataframe["purchase penalty"] != 12000), "change score"] = True
    # Set "last_score" column to the current "suspect score" for rows where "change score" is True
    dataframe['last_score'] = 0
    dataframe.loc[dataframe['change score'] == True, 'last_score'] = dataframe.loc[
        dataframe['change score'] == True, 'suspect score']
    # Set "suspect score" column to 0 for rows where "change score" is True
    dataframe.loc[dataframe['change score'] == True, 'suspect score'] = 0
    return dataframe


# Function to calculate penalty for suspect scores over 2
def penalty_1005(dataframe):
    dataframe.loc[(dataframe["it's in range"] == False) & (dataframe["month number"] == today_date.month) & (
            dataframe["suspect score"] >= 2), "1005 penalty"] = 25000
    return dataframe


# Function to remove unnecessary penalties
def remove_unecceray_penalty(dataframe):
    dataframe.loc[(dataframe["dont penalty"] == True), "document difference penalty"] = 0
    dataframe.loc[(dataframe["dont penalty"] == True), "complaint_penalty"] = 0
    dataframe.loc[(dataframe["dont penalty"] == True), "em and pm penalty"] = 0
    dataframe.loc[(dataframe["dont penalty"] == True) | (dataframe["it's in range"] == True), "purchase penalty"] = 0
    dataframe.loc[(dataframe["dont penalty"] == True), "1005 penalty"] = 0
    return dataframe
