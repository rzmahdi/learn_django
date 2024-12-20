from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blogs'),
    path('new/', views.BlogCreateView.as_view(), name='new_blog'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='detail_blog'),
    path('<int:pk>/edit/', views.BlogUpdateView.as_view(), name='update_blog'),
    path('<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_blog'),
]