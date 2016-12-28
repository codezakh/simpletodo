from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list':list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/{field}/'.format(field=list_.id))

def add_item(request, list_id):
    item_text = request.POST['item_text']
    correct_list = List.objects.get(id=list_id)
    Item.objects.create(text=item_text, list=correct_list)
    return redirect('/lists/{field}/'.format(field=list_id))
