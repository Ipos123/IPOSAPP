from django.urls import path,re_path
from. import views
from django import urls
app_name = 'IposApp'

urlpatterns = [
    path('',views.Home,name="Home"),
    path('Display/', views.Display, name="Display"),
    path('Reg/',views.Reg,name="Reg"),
    path('show/<int:id>/', views.show, name="show"),
    path('update/<int:id>/',views.update,name="update"),
     path('report/<int:id>/',views.report,name="report"),
    path('updt/<int:id>/',views.updt,name="updt"),
    path('Stat/<int:id>/',views.Stat,name="Stat"),
    path('FinalReports/',views.FinalReports,name="FinalReports"),
   
]