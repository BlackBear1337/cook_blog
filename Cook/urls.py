from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Cook import views
from Cook.views import HomeView

app_name = 'cook'

urlpatterns = [
    path('comment/<int:pk>/', views.CreateComment.as_view(), name='create_comment'),
    path('', HomeView.as_view(), name='home'),
    path('<slug:slug>/<slug:post_slug>/', views.PostDetailView.as_view(), name="post_single"),
    path('<slug:slug>/', views.PostListView.as_view(), name="post_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
