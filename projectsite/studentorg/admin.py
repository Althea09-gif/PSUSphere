from django.contrib import admin
from .models import Student, OrgMember


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program")
    search_fields = ("lastname", "firstname")


@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined")
    search_fields = ("student__lastname", "student__firstname")

    def get_member_program(self, obj):
        return obj.student.program

    get_member_program.short_description = "Program"
