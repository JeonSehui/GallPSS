from django.shortcuts import render
from django.views.generic import View
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core import serializers
from users import models as users


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class MainView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        print("mainview load")
        
        #print("queryset for mainview list")
        #data = users.Task.objects.all()
        #json = serializers.serialize('json', data)
        #print(data)

        return render(request, "main.html", context={})
