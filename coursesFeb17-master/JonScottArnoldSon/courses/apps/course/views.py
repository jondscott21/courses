from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
    context = {
      'courses': Course.objects.all()
    }

    return render(request, 'course/index.html', context)
def process(request):
    print 'got here'
    if request.method == 'POST':
        print 'hello'
        print request.POST['name'], request.POST['desc']
        Course.objects.create(course_name=request.POST['name'], description=request.POST['desc'])
    return redirect('/')
def destroy(request, id):
    print id
    context = {
        'rem_course': Course.objects.get(id=id)
    }
    return render(request, 'course/destroy.html', context)
def deleted(request, id):
    Course.objects.filter(id=id).delete()

    return redirect('/')