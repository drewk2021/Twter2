from django.urls import path

from . import views

app_name = 'twts'
urlpatterns = [
    #/twts/posttwt
    path('postwt/<int:posteroftwt_id>/', views.posttwt, name="posttwt"),
    #/twts/authenticate/
    path('authenticate', views.authenticate, name='authenticate'),
    # /twts/indexnewuser/
    path('indexnewuser', views.indexnewuser, name='indexnewuser'),
    # ex: /twts/
    path('', views.home, name='home'),
    # ex: /twts/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /twts/5/vote/
    path('<int:twt_id>/vote/', views.vote, name='vote'),
    # ex /twts/reply/6/
    path('reply/<int:twt_id>/', views.replytotwt, name='replytotwt')
]
