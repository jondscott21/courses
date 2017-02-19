from django.shortcuts import render, redirect, HttpResponse
from .models import Course, Description, Comment

def index(request):
    context = {
      'courses': Course.objects.all()
    }

    return render(request, 'course/index.html', context)
def process(request):
    if request.method == 'POST':
       course = Course.objects.create(course_name=request.POST['name'])
       Description.objects.create(course=course, description=request.POST['desc'])
    return redirect('/')
def destroy(request, id):
    context = {
        'rem_course': Course.objects.get(id=id)
    }
    return render(request, 'course/destroy.html', context)
def deleted(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
def comments(request, id):
    context = {
        'course': Course.objects.get(id=id),
        'comments': Comment.objects.filter(course=id),
    }
    return render(request, 'course/comments.html', context)
def process2(request, id):
    Comment.objects.create(comment=request.POST['comment'], course=Course.objects.get(id=id))
    id = id
    return redirect('/comments/{}'.format(id))