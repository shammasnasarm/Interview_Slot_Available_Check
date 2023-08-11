# Interview_Slot_Available_Check

Step1: Create virtual enviorment
python3 -m venv env

Step2: Activate it
source env/bin/activate

Step3: Download the Project in Same Folder

Step4: Change directry to project Folder

Step5: Install requirments
pip install -r requirments.txt

Step6: Run the project
python3 manage.py runserver



API Endpoints

To create Interviewer and Candidate Avaiblle time
POST method - http://localhost:8000/api/available/
Input fields - 
{
    "user_id": int,
    "is_interviewer": false,
    "date": "",
    "start_time": "",
    "end_time": ""
}



To get list of Interviewer and Candidate Avaiblle time
GET request - http://localhost:8000/api/available/

To get both Interviewer and Candidate available slot
GET request - http://localhost:8000/api/available/slots/?interviewer_id=&candidate_id=&available_date=

here,
interviewer_id and candidate_id is manitory and 
available_date default = today date




