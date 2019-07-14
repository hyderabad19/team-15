from django.contrib import admin
from .models import TypeUsers,Users,District,Mandal,State,School,Cluster,SchoolCluster,Report
# Register your models here.
admin.site.register(TypeUsers)
admin.site.register(Users)
admin.site.register(Mandal)
admin.site.register(District)
admin.site.register(State)
admin.site.register(School)
admin.site.register(Cluster)
admin.site.register(SchoolCluster)
admin.site.register(Report)