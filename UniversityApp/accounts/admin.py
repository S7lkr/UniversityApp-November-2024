from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from UniversityApp.accounts.forms import UserRegisterForm, UserEditForm
from UniversityApp.accounts.models import Profile

UserModel = get_user_model()


class ShowProfile(admin.StackedInline):     # allows PROFILE data (all or selected fields)
    model = Profile                         # to be showcased in admin panel
    can_delete = False
    fields = (                  # select which fields to be shown
        # 'first_name',
        # 'last_name',
        # 'personal_image',
        # 'bio',
        # 'age',
        # 'course',
        'is_lector',
    )


@admin.register(UserModel)
class UserAdmin(UserAdmin):
    inlines = (ShowProfile, )       # declare that PROFILE will be showcased beneath USER data
    model = UserModel
    add_form = UserRegisterForm             # user creation form
    form = UserEditForm                     # user edit form
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)          # search by
    ordering = ('pk',)

    # User information, separated into CATEGORIES (sections):
    fieldsets = (
        ('User email/password', {'fields': ('email', 'password')}),
        ('User info', {'fields': ()}),
        ('User Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        ('User\'s last login', {'fields': ('last_login',)})
    )

    # when creating new user, which fields to be shown:
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
            }
        )
    )
