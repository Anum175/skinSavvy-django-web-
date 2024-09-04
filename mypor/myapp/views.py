import jwt
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from .models import Extra, Skill

SECRET_KEY = "secret"


def send_activation_email(user, email):
    encoded_id = jwt.encode({'myid': str(user.pk)}, key=SECRET_KEY, algorithm='HS256')
    link = f"http://127.0.0.1:8000/activate/{encoded_id}/"
    em = EmailMessage(
        "Registration",
        f"Thank you for registering on our website. Click below for confirmation: {link}",
        "your-email@example.com",
        [email]
    )
    em.send()


@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')


def login_user(request):
    if request.method == 'POST':
        un = request.POST['n']
        p = request.POST['p']
        user = authenticate(request, username=un, password=p)
        if user is not None:
            login(request, user)
            return redirect('admin_panel' if user.username == 'anum' else 'home')
        else:
            return render(request, 'login.html', {'msg': "Wrong credentials"})
    else:
        if request.user.is_authenticated:
            return redirect('admin_panel' if request.user.username == 'anum' else 'home')
        else:
            return render(request, 'login.html')


def user_list(request):
    users = User.objects.all()
    context = {'ob': users}
    return render(request, 'admin.html', context)


def signup_user(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        us = request.POST['n']
        e = request.POST['e']
        p = request.POST['p']
        pic = request.FILES.get('i')

        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username=us, email=e, password=p,
                                            is_active=False)
            Extra.objects.create(pid=user, img=pic)
            send_activation_email(user, e)
            return redirect('login')
        except Exception as error:
            return HttpResponse(f"Error: {error}")

    return render(request, 'signup.html')


def activate(request, encoded_id):
    try:
        dec = jwt.decode(encoded_id, key=SECRET_KEY, algorithms=['HS256'])
        user_id = int(dec['myid'])
        user = get_object_or_404(User, pk=user_id)
        user.is_active = True
        user.save()
        return redirect('login')
    except (jwt.DecodeError, jwt.ExpiredSignatureError, User.DoesNotExist) as e:
        return redirect('/error')  # Redirect to an error page or show an appropriate message


@login_required(login_url='login')
def logout_user(request):
    try:
        logout(request)
        return redirect('login')
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@login_required(login_url='login')
def blogs(request):
    return render(request, "blogs.html")


@login_required(login_url='login')
def contact(request):
    return render(request, "contact.html")


@login_required(login_url='login')
def admins(request):
    return render(request, "admin.html")


@login_required(login_url='login')
def adds(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        us = request.POST['n']
        e = request.POST['e']
        p = request.POST['p']
        img = request.FILES.get('f')
        try:
            user = User.objects.create_user(username=us, first_name=fn, last_name=ln, email=e, password=p,
                                            is_active=False)
            Extra.objects.create(pid=user, img=img)
            send_activation_email(user, e)
            return redirect('admin_panel')
        except Exception as e:
            return HttpResponse("Error: " + str(e))
    return render(request, "adduser.html")


@login_required(login_url='login')
def delete(request, id):
    try:
        obj = User.objects.get(pk=int(id))
        obj.delete()
        return redirect("admin_panel")
    except User.DoesNotExist:
        return HttpResponse("User not found")
    except Exception as e:
        return HttpResponse("Error: " + str(e))


@login_required(login_url='login')
def update(request, id):
    if request.method == 'POST':
        try:
            user = User.objects.get(pk=id)
            user.first_name = request.POST['fn']
            user.last_name = request.POST['ln']
            user.email = request.POST['e']
            user.save()
            return redirect('admin_panel')
        except User.DoesNotExist:
            return HttpResponse("User not found")
        except Exception as e:
            return HttpResponse("Error: " + str(e))

    user = get_object_or_404(User, pk=id)
    context = {'ob': user, 'id': id}
    return render(request, 'update.html', context)


@login_required(login_url='login')
def portfolio(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio.html', {'skills': skills})


@login_required(login_url='login')
def add_skill(request):
    if request.method == 'POST':
        skill_name = request.POST['skill_name']
        if skill_name:
            if Skill.objects.filter(name=skill_name).exists():
                return render(request, 'addskill.html', {'error': 'Skill already exists.'})
            else:
                Skill.objects.create(name=skill_name)
                return redirect('portfolio')
    return render(request, 'addskill.html')


def cv_view(request):
    skills = Skill.objects.all()
    return render(request, 'portfolio.html', {'skills': skills})
