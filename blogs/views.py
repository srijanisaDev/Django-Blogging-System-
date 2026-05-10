from django.shortcuts import redirect, render , get_object_or_404
from django.http import HttpResponse

from .models import Blog , Category

# Create your views here.
def posts_by_category(request , category_id):
    ## Fetch the posts that belongs to the category with the id category_id

    posts = Blog.objects.filter(status = 'Published' , category = category_id)

    # category = Category.objects.get(pk=category_id)  ---> this will return normal error page by django itself
    # category = get_object_or_404(Category , pk=category_id) ---> use this to show error 404 page 
    # use this to perform some custom action if the object doesnot exist
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')    

    context = {
        'posts' : posts,
        'category' : category,
    }
    return render(request , 'post_by_category.html' , context)