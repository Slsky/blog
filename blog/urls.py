from django.conf.urls import url
from . import views

urlpatterns = [
        #Домашняя страница
        url(r'^$', views.index, name='index'),
        url(r'^topics/$', views.topics, name='topics'),
        url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
        #Страница создания новой темы
        url(r'^new_topic/', views.new_topic, name='new_topic'),
        # Страница для добавления новых тем
        url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
        ]
