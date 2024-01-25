from datetime import datetime
from uuid import uuid4

class User:
    def __init__(self, username, email, password):
        self.user_id = str(uuid4())
        self.username = username
        self.email = email
        self.password = password
        self.registration_date = datetime.utcnow()

class JobPosting:
    def __init__(self, employer, job_title, job_description, salary):
        self.job_id = str(uuid4())
        self.employer = employer
        self.job_title = job_title
        self.job_description = job_description
        self.salary = salary
        self.post_date = datetime.utcnow()

class JobApplication:
    def __init__(self, job, applicant):
        self.application_id = str(uuid4())
        self.job = job
        self.applicant = applicant
        self.status = "Pending"
        self.application_date = datetime.utcnow()

class EmployerProfile:
    def __init__(self, user, company_name, industry, company_description, contact_number):
        self.employer_id = user.user_id
        self.company_name = company_name
        self.industry = industry
        self.company_description = company_description
        self.contact_number = contact_number

class Resume:
    def __init__(self, user, resume_title, skills, experience, education):
        self.resume_id = str(uuid4())
        self.applicant = user
        self.resume_title = resume_title
        self.skills = skills
        self.experience = experience
        self.education = education

# Example Usage:
if __name__ == "__main__":
    # Creating a user
    user1 = User("john_doe", "john@example.com", "securepassword")

    # Creating an employer profile
    employer_profile = EmployerProfile(user1, "ABC Corp", "IT", "Leading tech company", "123-456-7890")

    # Creating a job posting
    job_posting = JobPosting(employer_profile, "Software Engineer", "Exciting opportunity for a software engineer", 80000)

    # Creating a resume
    resume = Resume(user1, "Software Engineer Resume", ["Python", "JavaScript"], "5 years of experience", "Bachelor's in Computer Science")

    # Creating a job application
    job_application = JobApplication(job_posting, user1)

    # Displaying information
    print(f"User: {user1.username}, Email: {user1.email}")
    print(f"Employer: {employer_profile.company_name}, Job Title: {job_posting.job_title}")
    print(f"Applicant: {user1.username}, Applied for: {job_posting.job_title}")
    print(f"Resume: {resume.resume_title}, Skills: {resume.skills}")
    print(f"Application Status: {job_application.status}, Date: {job_application.application_date}")
