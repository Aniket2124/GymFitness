from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email
    

class Enrollment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=25)
    phonenumber = models.CharField(max_length=12)
    dob = models.CharField(max_length=50)
    select_membership_plan = models.CharField(max_length=200)
    select_trainer = models.CharField(max_length=55)
    referance = models.CharField(max_length=55)
    address = models.TextField()
    payment_status = models.CharField(max_length=55, blank=True, null=True)
    price = models.IntegerField(max_length=55, blank=True, null=True)
    due_date = models.DateTimeField(blank =True, null=True)
    timestamp = models.DateTimeField(auto_now_add = True, blank =True)

    def __str__(self):
        return self.fullname
    


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=25)
    salary = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add = True, blank =True)

    def __str__(self):
        return self.trainer_name


class Membership_Plan(models.Model):
    plan = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.plan

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    timestamp = models.DateTimeField(auto_now_add = True, blank =True)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    select_date = models.DateTimeField(auto_now_add = True)
    phonenumber = models.CharField(max_length=15)
    login = models.CharField(max_length=200)
    logout = models.CharField(max_length=200)
    select_workout = models.CharField(max_length=200)
    trained_by = models.CharField(max_length=200)

    def __int__(self):
        return self.id