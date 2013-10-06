from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from django.views.generic.base import View, TemplateResponseMixin, TemplateView
from friends.forms import ActivitiesForm
from friends.models import Activity, Profile


class HomeView(TemplateView):
    template_name = "friends/home.html"


class ConnectView(TemplateView):
    template_name = 'friends/connect.html'

    def get_context_data(self, **kwargs):
        context = super(ConnectView, self).get_context_data(**kwargs)
        #context['user'] = request.user
        context['activities'] = Activity.objects.all
        context['times'] = {"Friday", "Saturday", "Sunday", "Monday"}
        return context


class ProfileView(UpdateView):
    template_name = "friends/profile.html"
    form_class = ActivitiesForm
    model = Profile
    success_url = '/friends'#this is required

    def get_object(self, queryset=None):
        return self.request.user.profile


def checkprofile(request):
    #right after someone signs up, create a new profile for them if they don't have one
    if not hasattr(request.user, 'profile'):
        p = Profile(user=request.user)
        p.save()
    else:
        p = request.user.profile
    if p.profile_complete():
        return HttpResponseRedirect("/friends/connect")
    return HttpResponseRedirect("/friends/profile")
