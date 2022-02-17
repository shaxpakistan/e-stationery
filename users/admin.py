from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserProfile

# Modify Site Header default: "Django Administration"
admin.site.site_header = 'E-Stationery System'                
# Modify Site Title default: "Site administration"
admin.site.index_title = 'E-Stationery Site Management'          
# Modify Site Index Title default: "Django site admin"
admin.site.site_title = 'Welcome to E-Stationery system admin site'                  
# Modify Site URL
admin.site.site_urls = 'E-Stationery admin site'


admin.site.register(UserProfile)
admin.site.unregister(Group)
