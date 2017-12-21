
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_topic(request):
    """Выводит страницу для добавления новой темы"""
    if request.method != 'POST':
        # Выводит пустую форму для заполнения
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        # Проверяем переданные данные
        if form.is_valid():
             form.save()
             return HttpResponseRedirect(reverse('blog:topics'))

    context = {'form': form}
    return render(request, 'blog/new_topic.html', context)

def new_entry(request, topic_id):
    """Выводит страницу для добавление новой записи"""
    topic = Topic.objects.get(id=topic_id)
        # Если данные не отправлялись; создается пустая форма.
    if request.method != 'POST':
        form = EntryForm()
    else:
        # Отправленны данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic_id]))

    context = {'topic': topic,'form': form }
    return render(request, 'blog/new_entry.html', context)

def edit_entry(request, entry_id):
    """Страница для редактирования запией"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
        # Если пустая форма
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать запрос
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic',args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blog/edit_entry.html', context )


# Create your views here.
