from django.contrib import admin

from .models import *

admin.site.register(StudentClass)
#admin.site.register(Student)
admin.site.register(Subjects)
admin.site.register(StudentSubject)


class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(user__is_teacher=True)   

admin.site.register(Teacher, TeacherAdmin)

class JSS1StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name']
    list_filter = ['student_class']
    search_fields = ['first_name']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs
    
admin.site.register(Student, JSS1StudentAdmin)

from django.utils.translation import gettext_lazy as _
from django.contrib.admin.sites import AdminSite
from django.contrib.admin.sites import AdminSite

class TeacherAdminSite(AdminSite):
    site_header = _('Teacher Administration')
    site_title = _('Teacher Admin')
    index_title = _('Site Administration')

    def has_permission(self, request):
        return request.user.is_active and request.user.is_teacher

    def has_change_permission(self, request, obj=None):
        if request.user.is_teacher:
            # Allow teachers to edit scores for subjects they teach
            return obj is not None and obj.subject.teacher == request.user.teacher and 'score' in request.GET
        else:
            return super().has_change_permission(request, obj=obj)

    def has_permission(self, request):
        return request.user.is_active and request.user.is_teacher

teacher_admin_site = TeacherAdminSite(name='teacher_admin')
teacher_admin_site.register(Teacher)
teacher_admin_site.register(Student)

from django import forms
from django.contrib import admin
from .models import StudentSubject


class StudentSubjectForm(forms.ModelForm):
    class Meta:
        model = StudentSubject
        fields = ['score']

class StudentSubjectAdmin(admin.ModelAdmin):
    
    form = StudentSubjectForm


    list_display = ('student', 'subject', 'score')
    list_filter = ('subject__teacher',)  # Only show subjects that are taught by the logged-in teacher
    search_fields = ('student__name', 'subject__name')  # Enable searching by student or subject name

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_teacher:
            # Only show subjects that are taught by the logged-in teacher
            qs = qs.filter(subject__teacher=request.user.teacher)
        return qs

    def has_change_permission(self, request, obj=None):
        if request.user.is_teacher:
            # Allow teachers to edit scores for subjects they teach
            return obj is not None and obj.subject.teacher == request.user.teacher
        else:
            return super().has_change_permission(request, obj=obj)

teacher_admin_site.register(StudentSubject, StudentSubjectAdmin)






