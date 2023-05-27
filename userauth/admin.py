from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id','first_name','email', 'is_teacher', 'is_student', 'is_principal','classroom')
    list_filter = ('is_teacher', 'is_student', 'is_principal',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password','classroom')}),
        (_('Permissions'), {'fields': ('is_teacher', 'is_student', 'is_principal', 'groups', 'user_permissions')}),
#        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_teacher', 'is_student', 'is_principal', 'is_active')}
        ),
    )





admin.site.register(CustomUser, CustomUserAdmin)


