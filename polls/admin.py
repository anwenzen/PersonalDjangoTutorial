from django.contrib import admin

from polls.models import Subject, Teacher


class SubjectModelAdmin(admin.ModelAdmin):
    related_name = "学科"
    list_display = ('no', 'name', 'intro', 'is_hot')
    search_fields = ('name',)
    ordering = ('no',)

    def __str__(self):
        return '123'


class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'sex', 'birth', 'good_count', 'bad_count', 'subject')
    search_fields = ('name',)
    ordering = ('no',)


admin.site.register(Subject, SubjectModelAdmin)
admin.site.register(Teacher, TeacherModelAdmin)
