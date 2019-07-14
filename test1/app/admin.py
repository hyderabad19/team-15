from django.contrib import admin
from .models import Mandal,District,User,School,ClusterSchool,TypeResource,Resource
#Cluster
# Register your models here.
admin.site.register(Mandal)
admin.site.register(District)
admin.site.register(User)
admin.site.register(School)
#admin.site.register(Cluster)
admin.site.register(ClusterSchool)
admin.site.register(TypeResource)
admin.site.register(Resource)
