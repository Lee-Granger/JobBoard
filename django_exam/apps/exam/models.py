from django.db import models
import datetime
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# ********************************************************************************************************************************
class UserManager(models.Manager):
    def validate_reg(self, post_data):
        errors = {}
        if len(post_data['f_name']) == 0:
            errors['f_name'] = 'Must enter a valid first name'
        if len(post_data['l_name']) == 0:
            errors['l_name'] = 'Must enter a valid last name'
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Must enter a valid email'
        return errors
# ********************************************************************************************************************************
class JobManager(models.Manager):
    def validate_job(self, post_data):
        errors = {}
        if len(post_data['title']) < 3:
            errors['title'] = 'Must enter a valid title'
        if len(post_data['description']) < 3:
            errors['description'] = 'Must enter a valid description'
        if len(post_data['location']) < 3:
            errors['location'] = 'Must enter a valid location'
        return errors                
# ********************************************************************************************************************************
class User(models.Model):
    First_name = models.CharField(max_length=45)
    Last_name = models.CharField(max_length=45)
    Email = models.CharField(max_length=45)
    Password = models.CharField(max_length=255)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

# ********************************************************************************************************************************
class Job(models.Model):
    Name = models.CharField(max_length=45)
    Location = models.CharField(max_length=100)
    Description = models.CharField(max_length=45)
    user = models.ForeignKey(User, related_name = 'jobs')
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()
# ********************************************************************************************************************************
