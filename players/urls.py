from django.urls import path
from . import views

urlpatterns = [
    # path('',views.PlayerMixinView.as_view()),
    path('', views.PlayerListCreateAPIView.as_view(),name="player-list"),
    # path("<int:pk>/",views.PlayerMixinView.as_view()),
    path('<int:pk>/', views.PlayerDetailAPIView.as_view(),name="player-detail"),
    path('<int:pk>/update/', views.PlayerUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.PlayerDeleteAPIView.as_view())
    # path('',views.player_alt_view),
    # path('<int:pk>/', views.player_alt_view)
]