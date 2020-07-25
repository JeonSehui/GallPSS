from django.shortcuts import render
from django.views.generic import View

class MainView(View):
    def get(self, request):
        print("mainview load")
        return render(request, "main.html", context={'text': '메인이에요'})