import xadmin

from apps.organizations.models import Teacher, CourseOrg, City

class TeacherAdmin(object):
    list_display = ["org", "name", "work_years","work_company"]
    search_fields = ["org", "name", "work_years","work_company"]
    list_filter = ["org", "name", "work_years","work_company"]
    list_editable = ["org", "name", "work_years","work_company"]

class CourseOrgAdmin(object):
    list_display = ["name", "description","click_nums","course_number" ]
    search_fields = ["name", "description","click_nums","course_number" ]
    list_filter =  ["name", "description","click_nums","course_number" ]
    list_editable = ["name", "description","click_nums","course_number" ]

class CityAdmin(object):
    list_display = ["id", "name", "description" ]
    search_fields = ["name", "description"]
    list_filter =  ["name", "description", "add_time"]
    list_editable = ["name", "description"]



xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)