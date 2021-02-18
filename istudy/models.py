from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
    

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    roles=(('parent','parent'),('student','student'),('teacher','teacher'))
    role = models.CharField(max_length=200,choices=roles)
    phone_number=models.CharField(max_length=255)
    full_name=models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
   

class Teachers(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    created=models.DateTimeField(auto_now_add=True)
    profile_picture = CloudinaryField('image',null=True)
    bio=models.TextField(null=True,blank=True)


    def __str__(self):
        return self.user.username  

class Parents(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.user.username


class Module(models.Model):
    year=models.CharField(max_length=50)

    def __str__(self):
        return self.year

       

class Courses(models.Model):
    course_name=models.CharField(max_length=255)
    created=models.DateTimeField(auto_now_add=True)
    module_id=models.ForeignKey(Module,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.course_name

class Students(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    profile_picture = CloudinaryField('image',null=True)
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True)


    def __str__(self):
        return self.user.username
class CoursesPaid(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True)
    student_id=models.ForeignKey(Students,on_delete=models.SET_NULL,null=True,blank=True)
    parent_id=models.ForeignKey(Parents,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering =['-pk']
    

class Subjects(models.Model):
    subject_name=models.CharField(max_length=255)
    content=models.TextField(null=True,blank=True)
    image=CloudinaryField('image',null=True,blank=True)
    book_link= models.URLField(null=True,blank=True)
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True)
    teacher_id=models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f'{self.subject_name} Subject'





class StudentNotification(models.Model):
    student_id=models.ForeignKey(Students,on_delete=models.SET_NULL,null=True,blank=True)
    mesage=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_id} student notification"

class TeacherNotification(models.Model):
    teacher_id=models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True,blank=True)
    mesage=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher_id} teacher notification"


class Payment(models.Model):
    tx_ref=models.CharField(null=True,blank=True,max_length=200)
    amount=models.FloatField(null=True,blank=True)
    currency=models.TextField(max_length=3)
    network=models.TextField(max_length=50)
    user=models.OneToOneField(Parents,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f'{self.amount} Payment'

class Completed_course(models.Model):
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    finished_course=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course_id} completed course"

class Completed_module(models.Model):
    module_id=models.ForeignKey(Module,on_delete=models.SET_NULL,null=True,blank=True)
    course_id=models.ForeignKey(Courses,on_delete=models.SET_NULL,null=True,blank=True)
    user_id=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,null=True,blank=True)
    finished_module=models.BooleanField(default=False)


    def __str__(self):
        return f"{self.module_id} completed module"

  
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
    



    