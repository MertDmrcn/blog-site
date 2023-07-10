from django.http.response import HttpResponse
from django.shortcuts import render
from blog.models import Blog


data = {
    "blogs": [
        {
            "id":1,
            "title":"komple web geliştirme",
            "img":"1.jpg",
            "is_active":True,
            "is_home":False,
            "description":"çok iyi kurs bea"
        },
        {
            "id":2,
            "title":"python web geliştirme",
            "img":"2.jpg",
            "is_active":True,
            "is_home":True,
            "description":"çok iyi kurs bea"
        },
        {
            "id":3,
            "title":"Php web geliştirme",
            "img":"3.jpg",
            "is_active":True,
            "is_home":True,
            "description":"çok iyi kurs bea"
        }
    ]
}

# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def  blog_details(request,id):
    # blogs= data["blogs"]
    # selectBlog= None
    
    # for blog in blogs:
    #     if blog["id"]== id:
    #         selectBlog=blog
    
    blogs = data["blogs"]
    selectBlog = [blog for blog in blogs if blog ["id"]==id][0]
    
    return render(request,"blog/blog-details.html",{
        "blog":selectBlog
     })
