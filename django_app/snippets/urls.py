from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippet'

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view(), name='list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name='detail'),
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)