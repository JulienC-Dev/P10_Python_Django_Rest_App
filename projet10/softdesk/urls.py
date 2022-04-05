from django.urls import path
from .views import (ProjectsAPI,
                    ContributorsAPI,
                    IssueAPI,
                    CommentAPI)


Projects_list = ProjectsAPI.as_view({
    'post': 'create',
    'get': 'list',
})
Projects_detail = ProjectsAPI.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
Contributors_list = ContributorsAPI.as_view({
    'post': 'create',
    'get': 'list',
})
Contributors_detail = ContributorsAPI.as_view({
    'delete': 'destroy'
})
Issues_list = IssueAPI.as_view({
    'post': 'create',
    'get': 'list'
})
Issues_detail = IssueAPI.as_view({
    'put': 'update',
    'delete': 'destroy'
})
Comments_list = CommentAPI.as_view({
    'post': 'create',
    'get': 'list'
})
Comments_detail = CommentAPI.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'put': 'update',
})
urlpatterns = [
    path('', Projects_list, name='projets-list'),
    path('<int:pk>/', Projects_detail, name='projets-detail'),
    path('<int:project_id>/users/', Contributors_list, name='contributors-list'),
    path('<int:project_id>/users/<int:user_id>/', Contributors_detail, name='contributors-detail'),
    path('<int:project_id>/issues/', Issues_list, name='issues-list'),
    path('<int:project_id>/issues/<int:issue_id>/', Issues_detail, name='issues-detail'),
    path('<int:project_id>/issues/<int:issue_id>/comments/', Comments_list, name='comments-list'),
    path('<int:project_id>/issues/<int:issue_id>/comments/<int:comment_id>/', Comments_detail, name='comments-detail'),
]

