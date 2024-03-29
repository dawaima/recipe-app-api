from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']

    fieldsets = (
        (None, {"fields": ('email', 'password')}),
        (_('Personal info'), {"fields": ('name',)}),
        (_('Permissions'),
         {"fields": ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {"fields": ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            "fields": ('email', 'password', 'password2'),
            'classes': ('wide', ),
        }),
    )


admin.site.register(models.User, UserAdmin)
