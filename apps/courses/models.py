from datetime import datetime

from django.db import models

from apps.users.models import  BaseModel
from apps.organizations.models import Teacher
# Design the primary structure of the course table
"""
One Course:Multiple Charpther
           Multiple documentation
           Resource

"""


class Course (BaseModel):
    name = models.CharField(verbose_name ="Course Name", max_length = 50)
    description = models.CharField(verbose_name = "Course Description",max_length = 100)
    learn_time =  models.IntegerField(default=0, verbose_name="Learning Time (Minute)")
    difficultly = models.CharField(verbose_name= "Difficultly",choices=(("easy","Easy"),("medium","Medium"),("hard","Hard")), max_length = 2)
    students = models.IntegerField(default=0, verbose_name= "Students")
    favorite_number = models.IntegerField(default=0, verbose_name= "Favorites")
    click_number = models.IntegerField(default=0, verbose_name="Number of Clicks")
    category = models.CharField(default=u"BackEnd Development", max_length=20, verbose_name="Course Category")
    tag = models.CharField(default="", verbose_name="Course tag",max_length=10)
    you_should_know = models.CharField(default="", max_length=300, verbose_name="Student should know")
    description_by_teach = models.CharField(default="",max_length=300,verbose_name="Teacher's words")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Teacher")

    detail_description = models.TextField(verbose_name= "Course Description")
    image = models.ImageField(upload_to="courses/%Y%m",verbose_name="Course head image",max_length=100)

    class Meta:
        verbose_name = "Couse information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name="Charter") # ondelete means what happen when foreign key deleted
    name = models.CharField(verbose_name =u"Lesson Name", max_length = 50)
    learning_time = models.IntegerField(default=0, verbose_name="Learning time")

    class Meta:
        db_table = "course.lesson"
        verbose_name = "Lesson information"
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="Charter", on_delete=models.CASCADE)
    learning_time = models.IntegerField(default=0, verbose_name="Learning Time")
    url = models.CharField(max_length=200,verbose_name=u"URL Address")
    name = models.CharField(max_length=100,verbose_name=u"Video Name")

    class Meta:
        verbose_name = "Video information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    name = models.CharField(verbose_name="Name", max_length=100)
    file = models.FileField(upload_to="course/resource/%Y%m", verbose_name="Download URL", max_length=200)


