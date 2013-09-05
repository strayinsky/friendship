from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from haystack.views import SearchView
from friends import views

urlpatterns = patterns('',
                       url(r'^$', views.HomeView.as_view(), name='home'),
                       url(r'^connect$', login_required(views.ConnectView.as_view()), name='connect'),
                       url(r'^interests/(?P<pk>\d+)/$', login_required(views.InterestsView.as_view()), name='interests'),
)
