from django.conf.urls import url
from LoginApp import views
urlpatterns=[
    url(r'^login/',views.index),
    url(r'^Register/',views.signup),


]