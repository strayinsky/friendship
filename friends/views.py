from django.http import HttpResponse, request
from django.views.generic.base import View, TemplateResponseMixin, TemplateView


class HomeView(TemplateView):
    template_name = "friends/home.html"


class ConnectView(TemplateView):
    template_name = 'friends/connect.html'

    def context_data(self, **kwargs):
        context = super(Connectview, self).get_context_data(**kwargs)
        context['user'] = request.user
        return context
