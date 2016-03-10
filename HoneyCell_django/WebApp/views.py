from django.shortcuts import render

# allow us to redirect
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.http import HttpResponse
from django.template import RequestContext, loader

# import the User class in models.py
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# import the auth.models User
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from WebApp.models import *


@login_required
def index(request):
    print("in the index function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/index.html', context)



# registration is normal route, and login is login is "django.contrib.views.login"
def registration(request):
    errors = []
    context = {}
    if request.method == "GET":
        return render(request, 'WebApp/register.html', context)

    # add 'errors' attribute to the context
    context['errors'] = errors

    password1 = request.POST['password']
    password2 = request.POST['password_confirmation']

    if password1 != password2:

        print("Passwords did not match.")

        # error1 happens
        errors.append("Passwords did not match.")

    if len(User.objects.all().filter(username = request.POST['user_name'])) > 0:
        print("Username is already taken.")

        # error2 happens
        errors.append("Username is already taken.")

    if errors:
        return render(request, 'WebApp/register.html', context)

    # create a new user from the valid form data, using create_user function with 2 arguments, 'username' and 'password'
    new_user = User.objects.create_user(username=request.POST['user_name'], password=request.POST['password'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    new_user.save()

    # using 'authenticate' function
    new_user = authenticate(username = request.POST['user_name'], password = request.POST['password'])

    # using 'login' function
    login(request, new_user)

    # using 'redirect' function
    return redirect(reverse('message'))

@login_required
def message(request):
    print("in the message function.")

    print("%" * 30)
    print(request.session)
    print(request.COOKIES)
    print("%" * 30)


    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/message.html', context)

@login_required
def upload(request):
    print("in the upload function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/upload.html', context)

@login_required
def preprocess(request):
    print("in the preprocess function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/preprocessing.html', context)

@login_required
def visualization(request):
    print("in the visualization function.")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/knnresult.html', context)

# def logout view
def my_logout(request):
    logout(request)
    return redirect(reverse('index'))

@login_required
def honeycell(request):
    print("in the honeycell function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycell.html', context)

@login_required
def honeycomb(request):
    print("in the honeycomb function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/honeycomb.html', context)

@login_required
def analytics(request):
    print("in the analytics function")
    context = {}
    user = request.user
    context['user'] = user
    return render(request, 'WebApp/analytics.html', context)








@login_required
def show_articles(request):
    print("in the show_articles.")

    context = {}
    context['user'] = request.user

    articles = Article.objects.all()
    context['articles'] = articles

    return render(request, 'WebApp/show_articles.html', context)



from WebApp.forms import *

@login_required
def add_article(request):
    print("in the add_article function.")

    context = {}
    context['user'] = request.user

    errors = []
    context['errors'] = errors

    if request.method == "GET":

        form = ArticleForm()
        context['form'] = form

        return render(request, 'WebApp/add_article.html', context)

    else:

        form = ArticleForm(request.POST, request.FILES)
        context['form'] = form


        print(form)


        if not form.is_valid():
            errors.append("The form is not valid.")
            return render(request, 'WebApp/add_article.html', context)
        form.save()
        print("Already save the form.")


        return render(request, 'WebApp/add_article.html', {'user': request.user, 'form': ArticleForm()})








@login_required
def article_detail(request, article_id):
    print("in the article_detail function.")

    context = {}
    context['user'] = request.user

    article = Article.objects.get(id=article_id)
    context['article'] = article

    return render(request, 'WebApp/article_detail.html', context)





@login_required
def like_article(request, article_id):
    print("in the like_article function.")

    context = {}
    context['user'] = request.user

    article = Article.objects.get(id=article_id)
    context['article'] = article

    article.like = article.like + 1
    article.save()
    print("Already update the like attribute of the Article object.")

    return render(request, 'WebApp/article_detail.html', context)




@login_required
def search_articles(request):
    print("in the search_article function.")

    context = {}
    context['user'] = request.user

    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    if search_text:
        print("The search_text is not None.")

        articles = Article.objects.filter(title__contains=search_text)
        context['articles'] = articles

        print("%" * 30)
        print(articles)
        print("%" * 30)


        return render(request, 'WebApp/search_articles_results.html', context)

    else:
        print("The search_text is None.")

        context['articles'] = None

        return render(request, 'WebApp/search_articles_results.html', context)














