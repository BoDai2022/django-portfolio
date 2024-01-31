from django.db import models


class Skill(models.Model):
    '''
    Skills required by jobs 
    '''
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name    

class JobApplication(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    skill_set = models.ManyToManyField(Skill, blank=True)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    start_date = models.DateField(blank=True, null=True)
    position_type = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    contact_person = models.CharField(max_length=255)
    application_status = models.CharField(max_length=100)
    interview_date = models.DateField(blank=True, null=True)
    follow_up_actions = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    job_posting_link = models.URLField(max_length=200)
    reflection = models.TextField(blank=True)
    cover_letter = models.URLField(blank=True)
    feedback_link_uuid = models.CharField(max_length=255, blank=True, unique=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

class Feedback(models.Model):
    """
    Feedbacks provided by hiring managers related to one job application
    """
    job_application = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    detailed_feedback = models.TextField(blank = True)
    factors = models.ManyToManyField('Factor', blank=True)  # Many-to-many relationship to Factor

    def __str__(self):
        return f"Feedback for {self.job_application.job_title} on {self.date}"

class Factor(models.Model):
    '''
    factors may influence decisions for jobapplicaiton
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name