# from django.urls import path

# from . import views

# app_name = "polls"
# urlpatterns = [
#     ## calls the index function
#     ## path has the method sig of:
#     ## path(route, view, (optional) kwags, (optional) name)
    
#     # ex: /polls
#     path("", views.index, name="index"),
#     # ex: /polls/5/
#     path("<int:question_id>/", views.detail, name="detail"),
#     # ex: /polls/5/results/
#     path("<int:question_id>/results/", views.results, name="results"),
#     # ex: /polls/5/vote/
#     path("<int:question_id>/vote/", views.vote, name="vote"),

# ]


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create_post/', views.create_post, name='create_post'),
    path('create_post_page', views.create_post_page, name = 'create_post_page'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('post/<int:post_id>/', views.post, name="post"),
    path('users/<int:user_id>', views.users, name="users"),
]
