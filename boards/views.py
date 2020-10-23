from django.shortcuts import render
from django.views.generic.list import BaseListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse
from core.views import LoginRequiredMixin
from . import models
from django.views.generic import TemplateView
from .models import Board, BoardItem

# class LeftMenu(LoginRequiredMixin, BaseListView):
#     model = models.Board
#     template_name = 'leftmenu.html'

#     def render_to_response(self, context, **response_kwargs):
#         print("leftmenu queryset start")
#         menuList = list(context['object_list'].values())
#         return JsonResponse(data=menuList, safe=False)

@method_decorator(ensure_csrf_cookie, name='dispatch')
class Category(LoginRequiredMixin, TemplateView):
    template_name = 'users/test_main.html'
    def get(self, request):
        context = {'categories': Board.objects.all().order_by('categoryid', 'itemid', 'detailid'),
                    'boarditems': BoardItem.objects.all()}

        return render(request, self.template_name, context)