from django.urls import path
from . import views

app_name = 'chocolate'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('photos/<int:category>', views.CategoryView.as_view(), name='photos_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('photo-detail/<int:pk>', views.DetailView.as_view(), name='photo_detail'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('photo/<int:pk>/delete', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo-detail/<int:pk>', views.CommentView.as_view(), name='comment'),
    path('photo-detail/like/', views.like, name='like'),
    # path('article/create/', ArticleCreateView.as_view(), name="article_create"),
    # path('like_for_post/', views.like_for_post, name='like_for_post'),  # 追加
]