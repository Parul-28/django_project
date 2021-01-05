from django.conf.urls import url
from basic_app import views


app_name='basic_app'

# for registration
urlpatterns=[

    url(r'^registration/$', views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login')
]
