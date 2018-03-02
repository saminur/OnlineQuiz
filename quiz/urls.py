from django.conf.urls import patterns, include, url
from OnlineQuiz.settings import STATIC_ROOT

urlpatterns = patterns('',
       url(r'^$', 'quiz.views.index', name='index'),
       url(r'^two/$', 'quiz.views.viewtwo', name='viewt')
)
