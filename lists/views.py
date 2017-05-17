from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.utils.html import escape

from lists.models import Item, List


def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list':list_})

def new_list(request):
    list_ = List.objects.create()
    item = Item(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html', {'error':error}) 
    return redirect('/lists/{field}/'.format(field=list_.id))

def add_item(request, list_id):
    item_text = request.POST['item_text']
    correct_list = List.objects.get(id=list_id)
    Item.objects.create(text=item_text, list=correct_list)
    return redirect('/lists/{field}/'.format(field=list_id))
