from django.views.generic import ListView  
from .filters import PostFilter  

class NewsListView(ListView):  
    model = Post  
    template_name = 'news_list.html'  
    context_object_name = 'news_list'  
    paginate_by = 10  

    def get_queryset(self):  
        queryset = Post.objects.filter(post_type=Post.NEWS)  
        self.filterset = PostFilter(self.request.GET, queryset=queryset)  
        return self.filterset.qs  

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)  
        context['filterset'] = self.filterset  
        return context