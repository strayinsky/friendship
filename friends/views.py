from django.http import HttpResponse, request
from django.views.generic.base import View, TemplateResponseMixin, TemplateView
from friends.models import Activity


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
