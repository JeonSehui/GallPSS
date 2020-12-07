from django.shortcuts import render, get_object_or_404
from django.views.generic.list import BaseListView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import JsonResponse
from core.views import LoginRequiredMixin
from . import models
from django.views.generic import TemplateView
from .models import Board, BoardItem
from django.core.paginator import Paginator
import math
from .forms import PostForm

@method_decorator(ensure_csrf_cookie, name='dispatch')
class Category(LoginRequiredMixin, TemplateView):
    template_name = 'users/test_main.html'
    def get(self, request):
        context = {'categories': Board.objects.all().order_by('categoryid', 'itemid', 'detailid')}

        return render(request, self.template_name, context)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class GetBoardItem(LoginRequiredMixin, TemplateView):
    board_template = 'users/test_main.html'
    detail_template = 'users/item_detail.html'
    create_template = 'users/create_item.html'

    def get(self, request, id):

        categories = Board.objects.all().order_by('categoryid', 'itemid', 'detailid')

        url = request.get_full_path().split("/")

        if url[2] == 'boardid':
            boarditems = BoardItem.objects.select_related('assginboardid').filter(assginboardid=id)
           
            paginator = Paginator(boarditems, 5)
            page = int(request.GET.get('page',1))
            contacts = paginator.get_page(page)
            page_range = 5 
            current_block = math.ceil(int(page)/page_range)
            start_block = (current_block-1) * page_range
            end_block = start_block + page_range
            p_range = paginator.page_range[start_block:end_block]

            context = {'categories':categories, 'p_range':p_range, 'boarditems': contacts}

            return render(request, self.board_template, context)
        elif url[2] == 'itemid':
            itemdetails = BoardItem.objects.get(pk=id)
            context = {'categories':categories, 'itemdetails': itemdetails}
            return render(request, self.detail_template, context)
        elif url[2] == 'create':
            form = PostForm()
            context = {'categories':categories, 'form':form}
            return render(request, self.create_template, context)



