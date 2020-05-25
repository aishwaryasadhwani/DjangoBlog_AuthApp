from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blogapp.models import PostBlog
from blogapp.forms import SignUpForm,PostBlogForm
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView,
TemplateView, View
)

# Create your views here.
def defaults(request):
    return render(request,'blogapp/index.html')

def home(request):
    return render(request,'blogapp/home.html')


# @login_required
# def postblog(request):
#     postblogform = PostBlogForm()
#     mydict = {'postblogform':postblogform}
#     if request.method == 'POST':
#         postblogform = PostBlogForm(request.POST,request.FILES)
#         if postblogform.is_valid():
#             data = postblogform.save()
#             data.author = str(request.user)
#             data.save()
#             mydict.update({'msg':'Posted Successfully !'})
#     return render(request,'blogapp/postblog.html',context=mydict)


# def viewblog(request):
#     blogs = PostBlog.objects.all().order_by('-posted_date')
#     mydict = {'blogs':blogs}
#     return render(request,'blogapp/viewblog.html',context=mydict)

def SignupPage(request):
    signupform = SignUpForm()
    mydict = {'signupform':signupform}
    if request.method == 'POST':
        signupform = SignUpForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            user.set_password(user.password)
            user.save()

            subject = "Welcome to our Blogs!"
            message = "Greetings!! "+ user.first_name+", You have successfully registered.You can avail our services by logging in.This is an auto generated mail.For any query,write to admin@gmail.com"
            recipient_list =[user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)

            mydict.update({'msg':'User is registered successfully !'})
    return render (request,'blogapp/signup.html',context=mydict)

# @login_required
# def PostDetailView(request,pid):
#     blog = PostBlog.objects.get(id=pid)
#     return render(request,'blogapp/detailblog.html',{'blog':blog})

# @login_required
# def delete_new(request,pid):
#     context={}
#     blog = PostBlog.objects.get(id=pid)
#
#     if request.method =="POST":
#         # delete object
#         blog.delete()
#         # after deleting redirect to
#         # home page
#         return HttpResponseRedirect("/viewblog/")
#     # return render(request,'blogapp/detailblog.html',{'blog':blog})
#     return render(request, "blogapp/delete_view.html", context)



class PostList(ListView):
    model = PostBlog
    template_name= 'blogapp/viewblog.html'
    context_object_name = 'blogs'
    ordering = ['-posted_date']


@method_decorator(login_required, name='dispatch')
class CreateBlog(CreateView):
    model = PostBlog
    fields = '__all__'
    template_name = 'blogapp/postblog.html'

    def get_success_url(self):
        return reverse('home')


@method_decorator(login_required, name='dispatch')
class DetailBlog(DetailView):
    model = PostBlog
    template_name = 'blogapp/detailblog.html'
    context_object_name = 'blog'

@method_decorator(login_required, name='dispatch')
class UpdateBlog(UpdateView):
    model = PostBlog
    fields = '__all__'
    template_name = 'blogapp/postblog.html'

    def get_success_url(self):
        return reverse('home')

@method_decorator(login_required, name='dispatch')
class DeleteBlog(DeleteView):
    model = PostBlog
    template_name = 'blogapp/delete_view.html'

    def get_success_url(self):
        return reverse('home')
