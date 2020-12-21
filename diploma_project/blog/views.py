from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .models import Post, Comment
from .forms import CommentForm


def blog_list(request):
    last = Post.objects.latest()
    list_o = Post.objects.all()[1:]
    context = {'list': list_o, 'last': last }
    return render(request, 'blog_list.html', context )


def get_likes(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        return render(request,'blog_detail.html', {'post':post})


class BlogDetailView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    context_object_name = "post"
    template_name = "blog_detail.html"

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk':self.get_object().id})

        
    def post(self,request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    




# Create your views here.
