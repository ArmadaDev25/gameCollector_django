from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('games/', views.GameList.as_view(), name='game_list'),
    path('games/<int:pk>/', views.GameDetail, name='game_detail'),
    path('games/create/', views.GameCreate.as_view(), name='game_form'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),
    
    path('games/<int:pk>/add_content/', views.add_content, name='add_content'),

    path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),

    #Features URLS
    path('features/', views.FeatureList.as_view(), name='features_list'),
    path('features/create/', views.FeatureCreate.as_view(), name='feature_create'),
    path('features/<int:pk>/', views.FeatureDetail.as_view(), name='features_detail'),
    path('games/<int:pk>/assoc_feat/<int:feat_pk>/', views.assoc_feat, name='assoc_feat'),

]