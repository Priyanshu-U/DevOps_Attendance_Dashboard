import sheet
import pandas as pd
import re


def emailRoll(email):
    if matches := re.search(r"^(.+)@iiitl\.ac\.in", email, re.IGNORECASE):
        return matches.group(1)


def getDates(key, df):
    fil = (df['Id'] == key.lower())
    return df.loc[fil, 'Date']


data = pd.read_csv(sheet.url)
data['Date'] = pd.to_datetime(data['Timestamp']).dt.date
data['Id'] = data['Email Address'].apply(emailRoll)
data['Name'] = data['Name'].str.title().str.strip()

data.drop(['Timestamp', 'Email Address', 'Roll Number'], axis=1, inplace=True)
data = data.filter(['Date', 'Id', 'Name'])
data.drop_duplicates(subset=['Date', 'Id'], inplace=True)

classDates = data['Date'].unique()
classCount = len(classDates)
totalStudents = data['Id'].nunique()

dateAttendance = data.value_counts('Date').sort_index().reset_index()

attendance = (data[['Id']].value_counts()) / classCount * 100
attendance = pd.DataFrame(attendance).reset_index()

print(attendance)