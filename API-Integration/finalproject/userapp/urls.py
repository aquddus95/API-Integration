from django.conf.urls import include,url 

from . import views


urlpatterns = [
    url('create_account/', views.Create_Account.as_view(), name='create_account'),
]
