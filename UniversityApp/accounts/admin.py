from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from UniversityApp.accounts.forms import UserRegisterForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    model = UserModel
    add_form = UserRegisterForm
    form = UserEditForm
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('pk',)

    # categories in admin panel (user information):
    fieldsets = (
        ('User email/password', {'fields': ('email', 'password')}),
        ('User info', {'fields': ()}),
        ('User Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('User\'s last login', {'fields': ('last_login',)})
    )

    # when creating new user, which fields to be shown:
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            }
        ),
    )
