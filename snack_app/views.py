from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Idea
from login_app.models import User
from django.db.models import Count

def index(request):
    context = {
        'ideas': Idea.objects.annotate(num_likes=Count('user_likes')).order_by('-num_likes'),
    }
    return render(request,'snack_index.html',context)

def create_idea(request):
    errors = Idea.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items(): 
            messages.error(request, v)
        return redirect('/snacks')
    else:
        user = User.objects.get(id = request.session['user_id'])
        idea = Idea.objects.create(
            title = request.POST['title'],
            description = request.POST['description'],
            user = user,
        )
        idea.user_likes.add(user)
        return redirect('/snacks')

def display_idea(request, idea_id):
    context = {
        'snack': Idea.objects.get(id = idea_id),
        'this_user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'snack.html', context)


def like(request, idea_id):
    user = User.objects.get(id = request.session['user_id'])
    idea = Idea.objects.get(id = idea_id)
    idea.user_dislikes.remove(user)
    idea.user_likes.add(user)
    return redirect('/snacks')

def dislike(request, idea_id):
    user = User.objects.get(id = request.session['user_id'])
    idea = Idea.objects.get(id = idea_id)
    idea.user_likes.remove(user)
    idea.user_dislikes.add(user)
    return redirect('/snacks')

def delete(request, idea_id):
    idea = Idea.objects.get(id = idea_id)
    idea.delete()
    return redirect('/snacks')

    



