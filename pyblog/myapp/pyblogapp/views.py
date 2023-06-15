from django.shortcuts import render
from pyblogapp.models import Blog
def project_view(request):
    blg = Blog.objects.all()
    print(blg)
    context = {
        'Blog' : blg
    }
    return render(request, 'project.html', context)

def newpost_view(request):
    return render(request, 'newpost.html', {})

def addpost_view(request):
    tit = request.POST.get('title')
    print(tit)
    desc = request.POST.get('description')
    print(desc)
    auth = request.POST.get('name')
    print(auth)
    blg = Blog(title=tit,description=desc,name=auth)
    blg.save()
    blg = Blog.objects.all()
    context = {
        'Blog':blg
    }
    return render(request,'project.html',context)

def delete_project(request, pk):
    print("In delete")
    Blog.objects.filter(pk=pk).delete()

    blg = Blog.objects.all()
    print(blg)
    context = {
        'Blog': blg
    }
    return render(request,'project.html', context)