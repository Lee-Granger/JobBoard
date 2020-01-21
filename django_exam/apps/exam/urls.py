from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user', views.register_user),
    url(r'^login_user', views.login_user),
    url(r'^dashboard', views.dashboard),
    url(r'^jobs/new', views.add_new_job),
    url(r'^post_created_job', views.post_created_job),
    url(r'remove/(?P<id>[0-9]+)$', views.delete),
    url(r'^logout', views.logout),
    url(r'^jobs/edit/(?P<id>[0-9]+)$', views.edit_job),
    url(r'^post_edit_job/(?P<id>[0-9]+)', views.post_edit_job),
    url(r'^jobs/(?P<id>[0-9]+)', views.view_job)
]