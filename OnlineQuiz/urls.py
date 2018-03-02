from django.conf.urls import patterns, include, url
from OnlineQuiz.settings import STATIC_ROOT

urlpatterns = patterns('',
     url(r'^', include('quiz.urls')),
     url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT, 'show_indexes' : True}),
)
