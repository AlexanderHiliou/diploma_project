from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin

from .models import Post, Comment, Tag
from .forms import CommentForm


def blog_list(request):
    last = Post.objects.latest()
    list_o = Post.objects.all()[1:]
    tags = Tag.objects.all()
    context = {'list': list_o, 'last': last, 'tags': tags}
    return render(request, 'blog_list.html', context )


<<<<<<< HEAD
=======

>>>>>>> 8b78af407452b522ac97fd0e20ded3d9f72af807
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
    context_object_names = "post"
    
    template_name = "blog_detail.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

    def get_success_url(self):
<<<<<<< HEAD
        return reverse_lazy('blog_detail', kwargs={'pk':self.get_object().id})

        
=======
        return reverse_lazy('blog_detail', {'pk':self.get_object().id})

     
>>>>>>> 8b78af407452b522ac97fd0e20ded3d9f72af807
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
