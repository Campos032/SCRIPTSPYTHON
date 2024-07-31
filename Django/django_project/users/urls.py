from django.urls import path
from .views import index, CreateUserView, GetUserView

# Create your urls here.

urlpatterns = [
    path('', index, name='index'),
    path('create', CreateUserView.as_view(), name='create_user'),
    path('get_user_by_id', GetUserView.as_view(), name='get_user_by_id')
]