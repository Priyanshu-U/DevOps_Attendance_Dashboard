# DevOps Course Attendance Dashboard
Welcome to the DevOps Course Attendance Dashboard! This project is a web-based dashboard built using Streamlit that provides insights into the attendance of the course. It pulls the attendance data directly from the form responses and calculates and segments the students based on their attendance percentage, considering the minimum applicable criteria of 75% attendance as per school laws.

## Features
Graphical representation of attendance data
Segmentation of students based on attendance criteria
Dataframe view for detailed insights
Automatic data updates from form responses

## Demo
Check out the live demo of the [DevOps Course Attendance Dashboard](https://devops-dash-iiitl.streamlit.app/).

## Screenshots
Dashboard Screenshot
<img width="1143" alt="image" src="https://github.com/Priyanshu-U/DevOps_Attendance_Dashboard/assets/62770722/d7f148c6-02fb-4a45-baeb-874f79eb5353">


## Prerequisites
Before running this project locally, ensure that you have the following prerequisites installed:

- Python 3.7 or later
- Streamlit
- Pandas
- Plot.ly


## Installation
### Clone the repository:
```bash
git clone https://github.com/your-username/devops-attendance-dashboard.git
```
### Navigate to the project directory:

```bash
cd devops-attendance-dashboard
```
### Install the dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Set up your Google Form to collect attendance responses. 
Use of a google workspace is preffered for ideal conditions.


```python
# Google Form URL
FORM_URL = "https://your-google-form-url"

# Sheet name where attendance responses are stored
SHEET_NAME = "Attendance"
```

Run the Streamlit application:

```bash
streamlit run app.py
```
Open your web browser and access the Streamlit app at http://localhost:8501.

## License
This project is licensed under the MIT License.

## Contact
If you have any questions or suggestions, please feel free to reach out to me:

Email: lit2020011@iiitl.ac.in

Thank you for using the DevOps Course Attendance Dashboard!
