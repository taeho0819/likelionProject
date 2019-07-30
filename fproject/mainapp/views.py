from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone
from django.core.paginator import Paginator
from .form import BlogPost

def home(request):
    blogs = Blog.objects
    #모델로 부터 객체목록을 전달받는다(쿼리셋)(기능을 표시하는 -메소드)
    #블로그의 모든 글들을 대상으로
    blog_list=Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator=Paginator(blog_list,3)
    #request된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    page=request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다.
    posts=paginator.get_page(page)
    return render(request, 'home.html',{'blogs':blogs, 'posts':posts})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html',{'blogs':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/' + str(blog.id))

# urls.py에서 blog_id 받아서 각각의 blog_detail 에 넣고 detail.html로 반환할 때 blogs로 같이 준다

def blogpost(request):
    #1.입력된 내용을 처리하는 기능
    #2.빈페이지를 띄워주는 기능
    if request.method == 'POST':
        form =BlogPost(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html',{'form':form})