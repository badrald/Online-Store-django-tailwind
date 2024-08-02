from django.shortcuts import render,get_object_or_404,redirect
from .models import Item
from .form import ConversationMessageForm
from .models import Conversation
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def new_conversation(request,item_id):
  item=get_object_or_404(Item,id=item_id)
  
  if item.created_by == request.user:
    return redirect('dash:index')
  
  conversations = Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

  if conversations:
    return redirect('contact:detail',id=conversations.first().id)

  if request.method =="POST":
      form=ConversationMessageForm(request.POST)
      if form.is_valid():
        conversation=Conversation.objects.create(item=item)
        conversation.members.add(request.user)
        conversation.members.add(item.created_by)
        conversation.save()

        conversation_masg=form.save(commit=False)
        conversation_masg.conversation = conversation
        conversation_masg.created_by = request.user
        conversation_masg.save()
        print("I am here")
        return redirect('item:detail',id=item_id)
  else :
      form=ConversationMessageForm()
      return render(request,'contact/new.html',{
        'form':form,})
  
@login_required
def inbox(request):
     conversations = Conversation.objects.filter(members__in=[request.user.id])
     return render(request,'contact/inbox.html',{"conversations":conversations})

@login_required
def deatil(request,id):
        conversation = Conversation.objects.filter(members__in=[request.user.id]).get(id=id)
        form=ConversationMessageForm()
        if request.method =="POST":
          form=ConversationMessageForm(request.POST)
          if form.is_valid():
            conversation_masg=form.save(commit=False)
            conversation_masg.conversation = conversation
            conversation_masg.created_by = request.user
            conversation_masg.save()
            return redirect('contact:detail',id=id)
        else:
          return render(request,'contact/detail.html',{
            'conversation':conversation,
            'form':form
        })
