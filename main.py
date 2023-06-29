import plotly.express as px
import streamlit as st

from data import dateAttendance, classCount, attendance

st.set_page_config(page_title='Dev-Ops Dashboard')

st.header('Dev-Ops Dashboard')
st.subheader('Attendance / Date')

form = 'https://forms.gle/8trcijgsAGvEhrUE9'
classLink = 'https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19' \
            '%3Ameeting_NWNjOTIwMGItNjg4Zi00NzhjLTllMDAtMjkxMDcxZWI3MGYx%40thread.v2%2F0%3Fcontext%3D%257B%2522Tid' \
            '%2522%253A%2522a655e90a-2df5-4b5e-8964-0a6b354f73d2%2522%252C%2522Oid%2522%253A%2522b5cd4905-1ca0-43ce' \
            '-881e-ceca52428881%2522%252C%2522MessageId%2522%253A%25220%2522%257D%26anon%3Dtrue&type=meetup-join' \
            '&deeplinkId=94c13f0a-a330-41b6-9ff8-350a7c25059b&directDl=true&msLaunch=true&enableMobilePage=true' \
            '&suppressPrompt=true '

st.sidebar.image("images/analysis.png", use_column_width=True)
st.sidebar.header(f"Total Lectures: {classCount}")
st.sidebar.write(f"Class [Link]({classLink})")
st.sidebar.write(f"Attendance Form [Link]({form})")




dateAttendance.columns = ['Lecture', 'Attendees']

attendanceCount = px.bar(dateAttendance, x='Lecture', y='Attendees',
                         hover_data='Attendees', hover_name='Lecture',
                         # title='Attendance / Date',
                         color_discrete_sequence=['#45CFDD'])
attendanceCount.update_layout(
    xaxis={'type': 'category'},
    xaxis_title="Lecture Dates",
    yaxis_title="Attendee Count"
)
st.plotly_chart(attendanceCount)

col1, col2 = st.columns(2)

attendance.columns = ['Roll Number', 'Percentage Attendance']
attendance_ok = attendance[attendance['Percentage Attendance'] >= 75]
attendance_low = attendance[attendance['Percentage Attendance'] < 75]

col1.subheader('Above 75%')
col1.dataframe(attendance_ok)

col2.subheader('Below 75%')
col2.dataframe(attendance_low)