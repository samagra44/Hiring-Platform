# Hiring Platform Project

## Overview
This Django-based Hiring Platform is designed to streamline the hiring process, providing a platform for candidates and Human Resources (HR) professionals. The system includes features for job posting, candidate applications, resume shortlisting, and status tracking.

## Features

### Candidate Section
1. **Resume Shortlisting:**
   - Candidates are selected based on resume shortlisting.
   - Relevant information from resumes is extracted for efficient screening.

2. **Job Application Status:**
   - Candidates can view the status of their job applications.
   - Status categories include selected, pending, and deselected.

### HR Section
1. **Job Posting:**
   - HR professionals can post job openings, specifying job details and requirements.
   - Jobs are displayed for candidates to view and apply.

2. **Candidate Management:**
   - HRs can view candidate applications and resumes.
   - Shortlisting and selection functionalities are available for efficient candidate management.

## Project Structure
- **Candidates App:**
  - Models:
    - `Sort`: For storing shortlisted candidates.
    - `Application`: For managing candidate applications and status.

- **HRs App:**
  - Models:
    - `Job`: For job posting details.
    - `CandidateApplication`: For managing candidate applications from the HR perspective.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/samagra44/hiring-platform.git
   cd hiring-platform

### Create a virtual environment:
```
python -m venv venv
```
### Activate the virtual environment:

- On Windows: ``` .\venv\Scripts\activate ```        
- On Unix or MacOS: ``` source venv/bin/activate ```   

### Clone This Repository :    

```
git clone https://github.com/samagra44/Hiring-Platform.git
```

### Change the directory :

```
cd Hiring-Platform
```

### Install all the Requirements :    

```
pip install -r requirements.txt
```    

### Create Super User :    

```
python manage.py createsuperuser
```   

### Make Migration :     

```
python manage.py makemigrations
```   

### Migrate The Changes :    

```
python manage.py migrate
```

### Start the development server :

```
python manage.py runserver
```

**Access the application at http://localhost:8000/**      

**Visit the admin interface at http://localhost:8000/admin/ to manage job postings, candidates, and applications.**

![Screenshot 2023-12-24 230222](https://github.com/samagra44/Hiring-Platform/assets/77968722/dcd3a362-c76b-4f7d-a6f0-718d27a40a34)

![Screenshot 2023-12-24 230253](https://github.com/samagra44/Hiring-Platform/assets/77968722/9e85c46b-49b5-4891-8b82-8f3c4b9c6aa4)

![Screenshot 2023-12-24 230405](https://github.com/samagra44/Hiring-Platform/assets/77968722/6acc4007-0100-4592-a939-70447d7ad3a3)

![Screenshot 2023-12-24 230432](https://github.com/samagra44/Hiring-Platform/assets/77968722/731cb63f-2e1f-4e6d-8ff7-3746e3c68a49)

![ss5](https://github.com/samagra44/Hiring-Platform/assets/77968722/db9ba419-4bb9-4dfa-afd5-2c8e70dc19f1)
