from django.urls import path

from hanrei import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post_new, name='post'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('search_result', views.search, name='search_result'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('shrine/', views.shrine, name='shrine'),
    path('shrine_detail/<int:id>/', views.shrine_detail, name='shrine_detail')
]
