from django.conf.urls import url
from basic_App import views

app_name = 'basic_App'

urlpatterns = [
    url('register/',views.register,name='register'),
    url('login/',views.logins,name='login'),
]