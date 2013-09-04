from django.http import HttpResponse, request
from django.views.generic import UpdateView
from django.views.generic.base import View, TemplateResponseMixin, TemplateView
from friends.forms import ActivitiesForm
from friends.models import Activity, Profile


class HomeView(TemplateView):
    template_name = "friends/home.html"


class ConnectView(TemplateView):
    template_name = 'friends/connect.html'

    def get_context_data(self, **kwargs):
        print "i got here!!"
        context = super(ConnectView, self).get_context_data(**kwargs)
        #context['user'] = request.user
        context['activities'] = Activity.objects.all
        for act in Activity.objects.all():
            print act.name
        context['times'] = {"Friday", "Saturday", "Sunday", "Monday"}
        return context


class InterestsView(UpdateView):
    template_name = "friends/interests.html"
    form_class = ActivitiesForm
    model = Profile
    success_url = '/friends'#this is required