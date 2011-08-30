from django.shortcuts import get_object_or_404, render_to_response
from coltrane.models import Entry, Category
from django.views.generic.list_detail import object_list

def entries_index(request):
    return render_to_response('coltrane/entry_index.html', {'entry_list': Entry.live.all()})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('coltrane/category_detail.html',
                               {'object_list': category.live_entry_set()})