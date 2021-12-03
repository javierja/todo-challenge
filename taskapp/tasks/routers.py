from rest_framework import routers, urlpatterns
from rest_framework.routers import DefaultRouter
from tasks.viewsets import UsersViewSet, TasksViewSet


router=DefaultRouter()

router.register(r'users', UsersViewSet, basename='users')
router.register(r'tasks', TasksViewSet, basename='tasks')


urlpatterns=router.urls