import requests
import os
import pandas as pd
# reads .env-file with seperated credentials
from dotenv import load_dotenv

# automatically looking for .env files in current path
load_dotenv()

# extraction from .env
url = os.getenv("SN_URL")
password = os.getenv("SN_PW")
username = os.getenv("SN_UN")

# Module url's from API doc  
incident_url = "/api/now/table/incident"
problem_url = "/api/now/table/problem"
change_url = "/api/now/table/change_request"
request_url = "/api/now/table/sc_request"

# create targetpath for data extract
inc_target_path = f"{url}{incident_url}"
problem_target_path = f"{url}{problem_url}"
change_target_path = f"{url}{change_url}"
req_target_path = f"{url}{request_url}"

# params for clean names instead of numbers
params = {
    "sysparm_display_value": "true",
}

# send and get JSON
headers = {
    "Content-Type":"application/json",
    "Accept":"application/json"
}


# Helper function - checking for dictionary (needed for request module)
# yes - "display_value", else value
def get_clean_value(field_data):
    if isinstance(field_data, dict):
        return field_data.get("display_value", "")
    return field_data

print("Loading data from ServiceNow...")


# Send Requests
inc_response = requests.get(inc_target_path, auth=(username,password), headers=headers,params=params)
problem_response = requests.get(problem_target_path, auth=(username,password), headers=headers,params=params)
change_response = requests.get(change_target_path, auth=(username,password), headers=headers, params=params)
req_response = requests.get(req_target_path, auth=(username,password), headers=headers,params=params)


# create dictionary for data handling
inc_data = inc_response.json()
problem_data = problem_response.json()
change_data = change_response.json()
req_data = req_response.json()

# extract list of data from variable data
all_incidents = inc_data["result"]
all_problems = problem_data["result"]
all_changes = change_data["result"]
all_requests = req_data["result"]

# container fpr pandas
inc_my_data = []
problem_my_data = []
change_my_data = []
req_my_data = []


# filter for incident
for element in all_incidents:

    inc_excel_dict = {
            "INC-Number": get_clean_value(element.get("number")),
            "Description": get_clean_value(element.get("short_description")),
            "Open Time": get_clean_value(element.get("opened_at")),
            "Urgency": get_clean_value(element.get("urgency")),
            "Caller / Opended By": get_clean_value(element.get("caller_id"))

            }
    inc_my_data.append(inc_excel_dict)

# output new Dataframe to Excel
target_path = "C:\\Users\\chris\\Documents\\UiPath\\PythonIntegration\\PythonWorker"


inc_file_name = "inc_output.xlsx"
inc_full_path = os.path.join(target_path, inc_file_name)
df = pd.DataFrame(inc_my_data)
df.to_excel(inc_full_path, index=False)

# filter for problems 
for element in all_problems:

    problem_excel_dict = {
            "Problem-Number": get_clean_value(element.get("number")),
            "Description": get_clean_value(element.get("short_description")),
            "Open Time": get_clean_value(element.get("opened_at")),
            "Urgency": get_clean_value(element.get("urgency")),
            "state": get_clean_value(element.get("problem_state")),
            }
    
    problem_my_data.append(problem_excel_dict)

# output new Dataframe to Excel
problem_file_name = "problem_output.xlsx"
problem_full_path = os.path.join(target_path, problem_file_name)
df = pd.DataFrame(problem_my_data)
df.to_excel(problem_full_path, index=False)

# filter for changes
for element in all_changes:

    change_excel_dict = {
            "Change-Number": get_clean_value(element.get("number")),
            "Description": get_clean_value(element.get("short_description")),
            "start date": get_clean_value(element.get("start_date")),
            "end date": get_clean_value(element.get("end_date")),
            "risk": get_clean_value(element.get("risk")),
            "type": get_clean_value(element.get("type"))
            }
    change_my_data.append(change_excel_dict)

# output new Dataframe to Excel
change_file_name = "change_output.xlsx"
change_full_path = os.path.join(target_path, change_file_name)
df = pd.DataFrame(change_my_data)
df.to_excel(change_full_path, index=False)


# filter for requests 
for element in all_requests:

    req_excel_dict = {
            "REQ-Number": get_clean_value(element.get("number")),
            "Short Description": get_clean_value(element.get("short_description")),
            "Open Time": get_clean_value(element.get("opened_at")),
            "Open by": get_clean_value(element.get("opened_by")),
            "Requested for": get_clean_value(element.get("requested_for")),
            "Request State": get_clean_value(element.get("request_state")),
            "Price": get_clean_value(element.get("price"))
            }
    req_my_data.append(req_excel_dict)

# output new Dataframe to Excel
req_file_name = "req_output.xlsx"
req_full_path = os.path.join(target_path, req_file_name)
df = pd.DataFrame(req_my_data)
df.to_excel(req_full_path, index=False)