from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from .forms import newItemForm,EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def detail(request,id):
    item=get_object_or_404(Item,id=id)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(id=id)[0:3]
    return render(request,'item/detail.html',{'item':item,'related':related_items})

@login_required
def new_item(request):
    if request.method == 'POST':
        form = newItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail',id=item.id)

    form = newItemForm()
    return render(request,"item/form.html",{'form':form,'title':'New'})

@login_required
def delete(request,id):
    item = get_object_or_404(Item,id=id,created_by=request.user)
    item.delete()
    return redirect('dash:index')

@login_required
def edit(request,id):
    item = get_object_or_404(Item,id=id,created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',id=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request,"item/form.html",{'form':form,'title':'Edit '})

  
def browse(request):
    items=Item.objects.filter(is_sold=False)
    categories=Category.objects.all()
    category_id = request.GET.get('category',0)
    query=(request.GET.get('query',''))

    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/items.html',{'items':items,
        'query':query , 
        'categories':categories,
        'category_id':int(category_id)
        })