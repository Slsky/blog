from django.shortcuts import render
from .models import Topic

def index(request):
    """Домашняя страница приложения Блога"""
    return render(request, 'blog/index.html')

def topics(request):
    """Выводит список тем."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html', context)

def topic(request, topic_id):
    """Вывод одну тему и все её записи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blog/topic.html', context)

# Create your views here.
