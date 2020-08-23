from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

User_Profile = get_user_model()


class UserQuestions(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Name")
    phone_numebr = models.CharField(max_length=10, verbose_name="Self-phone number")
    course_name = models.CharField(max_length=50, verbose_name=u"Course Name")

    class Meta:
        verbose_name = 'User Quesitons'
        verbose_name_plural = verbose_name


class CourseComment(BaseModel):
    user = models.ForeignKey(User_Profile, on_delete= models.CASCADE, verbose_name="User")
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name="Comments")

    class Meta:
        verbose_name = 'Course command'
        verbose_name_plural = verbose_name



class UserFavorite(BaseModel):
    user = models.ForeignKey(User_Profile, on_delete=models.CASCADE, verbose_name="User")
    fav_id = models.IntegerField(verbose_name="Data id")
    fav_type = models.IntegerField(choices=((1,"Course"),(2,"Organization"),(3,"Teacher")),default=1)

    class Meta:
        verbose_name = 'User favorite'
        verbose_name_plural = verbose_name


class UserMessage(BaseModel):
    user = models.ForeignKey(User_Profile, verbose_name="User", on_delete=models.CASCADE)
    message = models.CharField(max_length=200, verbose_name="Message")
    has_read = models.BooleanField(default=False, verbose_name="Read message")

    class Meta:
        verbose_name = 'User message'
        verbose_name_plural = verbose_name


class UserCourses(BaseModel):
    user = models.ForeignKey(User_Profile, verbose_name="User", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User courses'
        verbose_name_plural = verbose_name