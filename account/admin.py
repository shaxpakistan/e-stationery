from django.contrib import admin
from django.contrib.auth.models import Group
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth import get_user_model
# from .forms import UserAdminCreationForm, UserAdminChangeForm
# from account.models import User

# Modify Site Header default: "Django Administration"
admin.site.site_header = 'E-Stationery Service'                
# Modify Site Title default: "Site administration"
admin.site.index_title = 'E-Stationery Site Management'          
# Modify Site Index Title default: "Django site admin"
admin.site.site_title = 'Welcome to E-Stationery service admin site'                  
# Modify Site URL
admin.site.site_urls = 'E-Stationery admin site'

# User = get_user_model()
# # class UserAdmin(BaseUserAdmin):    
# class UserAdmin(admin.ModelAdmin):    
#     form = UserAdminChangeForm
#     add_form = UserAdminCreationForm

#     #.....fields used in displaying user models......
#     list_display    = ('first_name', 'last_name', 'username', 'email', 'admin')
#     list_filter     = ('admin','staff', 'active')

#     fieldsets       = (
#         (None, {'fields': ('username', 'email','password',)}),
#         ('personal info', {'fields': ('first_name','last_name','sex',)}),
#         ('permission',{'fields': ('admin', 'staff', 'active',)}),

#     )
#     #.............add fields set is not standard model.admin attribute..........
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
#         }),
#     )
#     #............ overrides get_fieldsets to use when creating a user...........
   
#     search_fields = ('email','username', 'first_name','last_name',)
#     ordering      = ('email','username',)
#     filter_horizontall = ()
    
# admin.site.register(User)
# admin.site.register(User, UserAdmin)
# .........removing group model from admin we`re not using it....... 
admin.site.unregister(Group)