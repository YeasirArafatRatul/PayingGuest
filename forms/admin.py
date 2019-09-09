from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms  import RegisterForm, UserAdminChangeForm
from .models import User 



User = get_user_model()

# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = RegisterForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'full_name','phone','Address','bio','admin')
    list_filter = ('admin','staff','active','Gender') 

    #fieldsets is used for displaying things inside table
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('full_name','Address','bio','phone','Gender')}),
        ('Permissions', {'fields': ('admin','staff','active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email','full_name',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User,UserAdmin)

admin.site.unregister(Group)


















# class UserAdmin(BaseUserAdmin):
# 	form = UserAdminChangeForm                     #for updating
# 	add_form = UserAdminCreationForm               #for creating
# 	list_display = ('full_name','email','is_admin')
	

# 	fieldsets = (
#             (None,{'fields':('username','email','password',)}),
#             ('Permission',{'fields':('is_admin',)}),
# 		)

# 	search_fields = ['full_name','email'] #for_searching in database
# 	ordering = ('full_name') #for ordering
# 	filter_horizontal = ()


# 	class Meta:
# 		model = User