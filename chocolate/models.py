from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(
        verbose_name='カテゴリ',
        max_length=20)

    def __str__(self):
        return self.title
    

class ChocoPost(models.Model):
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
        )

    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ',
        on_delete=models.PROTECT
        )
    
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200
        )
    
    comment = models.TextField(
        verbose_name='本文',
        )

    image = models.ImageField(
        verbose_name='イメージ',
        upload_to='photos'
        )

    comment2 = models.TextField(
        verbose_name='購入詳細',
        )
    
    posted_at = models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE, related_name = "detail",
    )
    target = models.ForeignKey(
        ChocoPost,
        on_delete=models.CASCADE, related_name = "detail",
    )
    content = models.TextField(verbose_name = 'コメント')
    created_at = models.DateTimeField(auto_now_add=True)



class LikeForPost(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(ChocoPost, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)


class LikeForComment(models.Model):
    """コメントに対するいいね"""
    target = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)

class Like(models.Model):
    user_id = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    target = models.ForeignKey(
        ChocoPost,
        on_delete=models.CASCADE
    )