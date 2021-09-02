from django.contrib import admin
from django.contrib.admin import AdminSite
from  .models import  News
# Register your models here.
class MyEmsAdminSite(AdminSite):

    site_title = 'Esports admin'
    #
    site_header = 'Esports admin'
    #
    index_title = 'Esports admin'



myems_admin_site = MyEmsAdminSite()



myems_admin_site.register(News)
