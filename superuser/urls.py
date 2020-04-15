from django.contrib import admin
from django.urls import path,include
from superuser import views
from django.conf import settings
from django.conf.urls.static import static

app_name='superuser'
urlpatterns = [
    path('freshlyapplied/', views.freshlyapplied,name='freshlyapplied'),
    path('accepted/', views.accepted,name='accepted'),
    path('rejected/', views.rejected,name='rejected'),
    path('check/', views.check,name='check'),
    path('addevent/',views.addevent,name='addevent'),
    path('checkdate/',views.checkdate,name='checkdate'),
    path('requestedevents/<int:pk>',views.requestedevents,name='requestedevents'),
    path('acceptedevents/',views.acceptedevents,name='acceptedevents'),
    path('rejectedevents/',views.rejectedevents,name='rejectedevents'),
    path('givereview/',views.givereview,name='givereview'),
   # path('showreview/',views.showreview,name='showreview'),
    path('solution', views.solution, name='solution'),
    path('result', views.result, name='r_result1'),
    path('viewcompanyprofile/<int:pk>',views.viewcompanyprofile,name='viewcompanyprofile'),
    path('viewreviews/',views.viewreviews,name='viewreviews')

]
