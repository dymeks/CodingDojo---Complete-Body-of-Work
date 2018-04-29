from __future__ import unicode_literals
from django.db import models
import re, bcrypt

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class usersManager(models.Manager):
    def user_validator(self, postData):
        #errors dictionary for passing error messages to template
        errors ={}
        #validation
        if postData['type'] == 'register':
            print "Register validation"
            if self.filter(email=postData['email']).exists(): #checks if a record with a matching email address exists in the database
                errors['Email error'] = 'Email address is allready registered'
            if len(postData['first_name'])< 2:
                errors['first_name'] = "First name should be more than 2 characters"
            if len(postData['last_name'])< 2:
                errors['Last Name'] = "Last name should be more than 2 characters"
            if not NAME_REGEX.match(postData['first_name']):
                errors['First name Format'] = "First name can only have characters"
            if not NAME_REGEX.match(postData['last_name']):
                errors["Last Name Format"] = "Last name can only have characters"
            if not EMAIL_REGEX.match(postData['email']):
                errors['Email Format'] = "Email is not in proper format"
            if postData['password'] != postData['Confirm_pw']:
                errors['Password'] = 'Passwords do not match'
            if len(postData['password']) < 8:
                errors['Password Length'] = "Password should be longer than 8 characters"
        
        elif postData['type'] == 'login':
            print "login validation"
            #if email is not found create error message, 
            if not self.filter(email=postData['email']).exists():
                    #self is equivilant to users.objects in this scope
                errors['Email error'] = 'Email address is not registered'
            #else get user object via email match, check password 
            else:
                this_user = users.objects.get(email = postData['email']) 
                if not bcrypt.checkpw(postData['password'].encode(), this_user.salt.encode()):
                    errors['Password Error'] ='Password is invalid'
        
        
        return errors


class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    def __repr__():
        print self.first_name, self.last_name, self.email, self.password, self.salt
    #this includes the users manager object in the user object, extends the functionality of the object
    objects = usersManager()

