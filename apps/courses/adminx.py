import xadmin

from apps.courses.models import Course, Lesson, Video, CourseResource

class CourseAdmin(object):
    list_display = ["name", "description", "detail_description", "difficultly", "learn_time", "students"]
    search_fields = ["name", "description", "detail_description", "difficultly", "students"]
    list_filter = ["name", "description", "detail_description", "difficultly", "students"]
    list_editable = ["description", "detail_description"]


class LessonAdmin(object):
    list_display = ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course", "name", "add_time"]
    list_editable = ["course", "name", "add_time"]


class VideoAdmin(object):
    list_display = ["name",     "lesson", "learning_time"]
    search_fields = ["name", "lesson", "learning_time"]
    list_filter = ["name", "lesson", "learning_time"]


class CourseResoureAdmin(object):
    list_display=["course", "name", "file"]
    search_fields=["course","name","file"]
    list_filter = ["course", "name", "file"]



xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResoureAdmin)
