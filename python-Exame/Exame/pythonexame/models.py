from django.db import models
import re

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email_address']): 
            errors['email_address'] = "Invalid email address!"
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least two characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least two characters'
        if postData['password'] != postData['confirm_password']:
            errors['password'] = 'Passwords must match'
        if len(postData['password']) < 8:
            errors['password_length'] = 'Password must be at least eight characters long'
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=45)
    password = models.CharField(max_length=255)  # For simplicity, consider using a more secure way to store passwords
    objects = UserManager()
