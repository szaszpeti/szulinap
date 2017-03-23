from django.conf.urls import url
from boldog import views

# SET THE NAMESPACE!
app_name = 'boldog'

urlpatterns=[
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^register/$',views.register,name='register'),
    url(r'^welcome/$',views.welcome,name='welcome'),
    url(r'^user_logout/$',views.user_logout,name='user_logout'),
    url(r'^ajandek/$',views.ajandek,name='ajandek'),
    url(r'^by/$',views.by,name='by'),

]