from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ChocoPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ChocoPost,Comment, Like
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.http import JsonResponse  # 追加
from .forms import CommentForm  # 追加
from django.shortcuts import redirect, get_object_or_404 # 追加

 
# Create your views here.

class IndexView(ListView):
    template_name = 'index.html'
    queryset = ChocoPost.objects.order_by('-posted_at')
    paginate_by = 6





@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    form_class = ChocoPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy('chocolate:post_done')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
    





class PostSuccessView(TemplateView):
    template_name = 'post_success.html'






class CategoryView(ListView):
    template_name='index.html'
    paginate_by = 6

    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ChocoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories






class UserView(ListView):
    template_name='index.html'
    paginate_by = 6

    def get_queryset(self):
        user_id = self.kwargs['user']

        user_list = ChocoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
    






class DetailView(DetailView):
    template_name='detail.html'
    model = ChocoPost

    #comment
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # テンプレートにコメント作成フォームを渡す
        context['comment_form'] = CommentForm
 
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        # 投稿に対するいいねの数
        like_count = self.object.like_set.count()
        context['like_count'] = like_count
 
        if self.object.like_set.filter(user_id=self.request.user).exists():
            context['is_user_liked'] = True
        else:
            context['is_user_liked'] = False
 
        return context
    
def like(request):
    chocopost_pk = request.POST.get('chocopost_pk')
    context = {
        'user_id': f'{ request.user }',
    }
    article = get_object_or_404(ChocoPost, pk=chocopost_pk)
    like = Like.objects.filter(target=article, user_id=request.user)

    if like.exists():
        like.delete()
        context['method'] = 'delete'
    else:
        like.create(target=article, user_id=request.user)
        context['method'] = 'create'

    context['like_count'] = article.like_set.count()

    return JsonResponse(context)


    # #good bottom
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     like_for_post_count = self.object.likeforpost_set.count()
    #     # ポストに対するイイね数
    #     context['like_for_post_count'] = like_for_post_count
    #     # ログイン中のユーザーがイイねしているかどうか
    #     if self.object.likeforpost_set.filter(user=self.request.user).exists():
    #         context['is_user_liked_for_post'] = True
    #     else:
    #         context['is_user_liked_for_post'] = False





class MypageView(ListView):
    template_name = 'mypage.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = ChocoPost.objects.filter(
            user = self.request.user).order_by('-posted_at')
        return queryset
    




class PhotoDeleteView(DeleteView):
    model = ChocoPost
    template_name = 'photo_delete.html'
    success_url = reverse_lazy('chocolate:mypage')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    





class CommentView(DetailView):
    model = Comment
    form_class = CommentForm
 
    #格納する値をチェック
    def form_valid(self, form):
        form.instance.author = self.request.user
        article_pk = self.kwargs.get('pk')
        article = get_object_or_404(ChocoPost, pk=article_pk)
 
        comment = form.save(commit=False)
        comment.target = article
        comment.save()
 
        return redirect('chocolate:detail', pk=article_pk)
    

# def like_for_post(request):
#     post_pk = request.POST.get('post_pk')
#     context = {
#         'user': f'{request.user.last_name} {request.user.first_name}',
#     }
#     post = get_object_or_404(ChocoPost, pk=post_pk)
#     like = LikeForPost.objects.filter(target=post, user=request.user)

#     if like.exists():
#         like.delete()
#         context['method'] = 'delete'
#     else:
#         like.create(target=post, user=request.user)
#         context['method'] = 'create'

#     context['like_for_post_count'] = post.likeforpost_set.count()

#     return JsonResponse(context)



