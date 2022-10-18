from django.urls import path
from .views import GitHubRepoViewSet

urlpatterns = [
    path('gitrepos', GitHubRepoViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('gitrepos/<str:pk>', GitHubRepoViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('usernames', GitHubRepoViewSet.as_view({
        'get': 'get_user_names',
    })),
    path('repos/<str:username>', GitHubRepoViewSet.as_view({
        'get': 'get_repo_by_username',
    })),
]
