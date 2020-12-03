from django.db import models
import bcrypt
import re

class UserManager(models.Manager):
    def register_validator(self, post_data):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(post_data['first_name']) < 1:
            errors["first_name"] = "first name can not be empty"

        if len(post_data['last_name']) < 1:
            errors["last_name"] = "Last name can not be empty "

        if len(post_data['user_email']) < 1:
            errors["user_email"] = "email can not be empty "

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['user_email']):            
            errors['email'] = "Invalid frommat email address!"

        if (post_data['user_password'] != post_data['password_confirm'] ):
            errors["password_confirm"] = "password did not match"

        if len(post_data['user_password']) < 8:
            errors["user_password"] = "password must be 8 charicters log"
        return errors
    def login_validator(self, post_data):
        errors = {}
        # check the email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['user_email']):            
            errors['email'] = "Invalid frommat email address!"

        users_list = User.objects.filter(user_email= post_data['user_email'])
        if len(users_list) == 0:
            errors['email_not_found'] = "Email address not in DB"
        else:
            if bcrypt.checkpw(
                post_data['user_password'].encode(),
                users_list[0].user_password.encode()
            ) != True:
                errors['password'] = "invalid Password!"
        
        #check the password

        
        return errors
        



# Create your models here.
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    user_email= models.CharField(max_length=255)
    user_password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    #budgets


class Budget(models.Model):
    title= models.CharField(max_length=255)
    posted_by = models.ForeignKey('User', related_name='bugets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #categorys

class Category(models.Model):
    title= models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    budget = models.ForeignKey('Budget', related_name='categorys', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #transcations



class Transaction(models.Model):
    category = models.CharField(max_length=255)
    posted_by = models.ForeignKey('User', related_name='transactions', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Income(models.Model):
    category= models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    notes = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    posted_by = models.ForeignKey('User', related_name='incomes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



# ##add models with relashatinps and run migrations 