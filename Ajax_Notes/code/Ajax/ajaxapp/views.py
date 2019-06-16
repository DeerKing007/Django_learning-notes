from django.shortcuts import render,HttpResponse

# Create your views here.


def regist(request):
    return render(request,'regist.html')


def checkname(request):
    name=request.POST.get('name')
    password=request.POST.get('pwd')
    if name == 'zhang3':
        return HttpResponse('用户名已存在')
    else:
        return HttpResponse('有效用户')



