from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name="City")
    description = models.CharField(max_length=100, verbose_name="Description of the city")

    class Meta:
        verbose_name = "City"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Organization name")
    description = models.TextField(verbose_name="Organization description")
    tag = models.CharField(default="Good", max_length=10, verbose_name="Course tage")
    category = models.CharField(default="School", verbose_name="Type of the organization", max_length=40,
                                choices=(("school", "School"), ("personal", "Personal"), ("university","University")))
    click_nums = models.IntegerField(default=0, verbose_name=u"Number of clicks")
    image = models.ImageField(upload_to="org/%Y%m", verbose_name="Organization image")
    address = models.CharField(max_length=150, verbose_name="Address of the organization")
    student = models.IntegerField(default=0, verbose_name="Number of student in this course")
    course_number = models.IntegerField(default=0, verbose_name="Number of courses")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")

    class Meta:
        verbose_name = "Course Organization"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.

class Teacher(BaseModel):
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="Belonging organization")
    name = models.CharField(default="", max_length=50, verbose_name="Tearch's name")
    work_years = models.IntegerField(default=0, verbose_name="Years of experience")
    work_company = models.CharField(max_length=50, verbose_name="Working company")
    work_position = models.CharField(max_length=50, verbose_name="Position")
    style = models.CharField(max_length=100, verbose_name="Teaching style")
    click_nums = models.IntegerField(default=0, verbose_name=u"Number of clicks")
    favorite_number = models.IntegerField(default=0, verbose_name="Favorites")
    age = models.IntegerField(default=18, verbose_name="Age")
    image = models.ImageField(default="", upload_to="tearch/%Y%m", verbose_name="Image", max_length=60)

    class Meta:
        verbose_name = "Tearchs in this organization"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
