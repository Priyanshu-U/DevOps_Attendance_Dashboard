#DevOps Course Attendance Dashboard
Welcome to the DevOps Course Attendance Dashboard! This project is a web-based dashboard built using Streamlit that provides insights into the attendance of the course. It pulls the attendance data directly from the form responses and calculates and segments the students based on their attendance percentage, considering the minimum applicable criteria of 75% attendance as per school laws.

##Features
Graphical representation of attendance data
Segmentation of students based on attendance criteria
Dataframe view for detailed insights
Automatic data updates from form responses

##Demo
Check out the live demo of the DevOps Course Attendance Dashboard here.

##Screenshots
Dashboard Screenshot

##Prerequisites
Before running this project locally, ensure that you have the following prerequisites installed:

Python 3.7 or later
Streamlit
Pandas
Plot.ly


##Installation
###Clone the repository:
```bash
git clone https://github.com/your-username/devops-attendance-dashboard.git
```
###Navigate to the project directory:

```bash
cd devops-attendance-dashboard
```
###Install the dependencies:
```bash
pip install -r requirements.txt
```
##Usage
Set up your Google Form to collect attendance responses. Make sure the form includes a question for each student's attendance.

Obtain the credentials file (credentials.json) for accessing Google Sheets API. Follow the instructions provided by the Google Sheets API documentation to generate the credentials file.


```python
# Google Form URL
FORM_URL = "https://your-google-form-url"

# Sheet name where attendance responses are stored
SHEET_NAME = "Attendance"
```

Run the Streamlit application:

```streamlit run app.py```
Open your web browser and access the Streamlit app at http://localhost:8501.

License
This project is licensed under the MIT License.

Contact
If you have any questions or suggestions, please feel free to reach out to me:

Email: lit2020011@iiitl.ac.in
Thank you for using the DevOps Course Attendance Dashboard!
