from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('',views.home),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('cluster',views.clusters,name='cluster'),
    path('school',views.schools,name='school'),
    path('school/<int:id>',views.school,name="schools"),
    path('cluster/<int:id>',views.cluster,name="cluster"),
   # path('reports',views.report,name="report")
    
]
