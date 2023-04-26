from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_teacher', 'is_student','is_principal')
    ordering = ('email',)
    list_filter = ('is_teacher', 'is_student')

admin.site.register(CustomUser, CustomUserAdmin)
