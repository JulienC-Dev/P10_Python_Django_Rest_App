from django.urls import path
from .views import (ProjectsAPI,
                    ContributorsAPI,
                    IssueAPI)


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

urlpatterns = [
    path('', Projects_list, name='projets-list'),
    path('<int:pk>/', Projects_detail, name='projets-detail'),
    path('<int:project_id>/users/', Contributors_list, name='contributors-list'),
    path('<int:project_id>/users/<int:user_id>/', Contributors_detail, name='contributors-detail'),
    path('<int:project_id>/issues/', Issues_list, name='issues-list'),

]



from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('', ProjectsAPI, basename="project")
# router.register('<int:project_id>/users/', ContributorsAPI, basename="contributor")
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]