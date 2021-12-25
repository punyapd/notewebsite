from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from .forms import CustomerRegistrationForm, CustomerProfileForm
from .models import CATEGORY, Course, News, Semester, Subject, TuModelQuestions, UnitwiseQuestions, RefrencedBooks, Customers

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

# ===========course view===========
def courses(request):
    course = Course.objects.all()
    return render(request, 'app/courses.html', {'course':course})

# =============SEMESTER================
def semesterView(request, id):
    course = Course.objects.get(id=id)
    semester = Semester.objects.filter(faculty=course)
    subject = Subject.objects.filter(faculty=course)
    return render(request, 'app/semester.html', {'semester':semester, 'subject':subject})

# =============SUBJECT================
def subject(request):
    return render(request, 'app/subject.html')

# =============MODEL QUESTIONS================
def modelQuestion(request, id):
    id = id
    obj = Subject.objects.get(id=id)
    print(obj)
    question = TuModelQuestions.objects.filter(subject=obj)
    print(question)
    return render(request, 'app/modelquestions.html', {'question':question, 'id':id})

def unitwiseQuestion(request, id):
    id = id
    obj = Subject.objects.get(id=id)
    print(obj)
    question = UnitwiseQuestions.objects.filter(subject=obj)
    print(question)
    return render(request, 'app/unitwisequestion.html', {'question':question, 'id':id})

# =============REFRENCED BOOKS================
def refrenced_books(request, id):
    id = id
    obj = Subject.objects.get(id=id)
    print(obj)
    question = RefrencedBooks.objects.filter(subject=obj)
    print(question)
    return render(request, 'app/refrenced-books.html', {'question':question, 'id':id})

# =============TECH NEWS================
def tech_news(request):
    tech = News.objects.filter(category='Tech_news')
    return render(request, 'app/tech-news.html', {'tech_news':tech})

def tech_detail(request, id):
    tech = News.objects.get(id=id)
    last_three = News.objects.filter(category='Tech_news').order_by('-id')[:4]
    return render(request, 'app/tech_detail.html', {'tech':tech, 'last_three':last_three})

def sports(request):
    sports = News.objects.filter(category='Sports')
    last_four_sports = News.objects.filter(category='Sports').order_by('-id')[:10]
    last_sports = News.objects.last()
    return render(request, 'app/sports.html', {'sports':sports, 'last_four':last_four_sports, 'last_sports':last_sports})

def sports_detail(request,id):
    sport = News.objects.get(id=id)
    last_three_sp = News.objects.filter(category='Sports').order_by('-id')[:4]
    return render(request, 'app/sports_detail.html',{'sport':sport, 'last_three_sp':last_three_sp})

def about(request):
    return render(request , 'app/about.html')
#============= ALL PROGRAMMING VIEWS ================
def programming(request):
    return render(request , 'app/programming.html')
def learnhtml(request):
    return render(request , 'app/learnhtml.html')
def intro(request):
    return render(request , 'app/introduction.html')


def learncss(request):
    return render(request , 'app/learncss.html')

def learnbootstrap(request):
    return render(request , 'app/learnbootstrap.html')

def learnjavascript(request):
    return render(request , 'app/learnjavascript.html')

def learnjquery(request):
    return render(request , 'app/learnjquery.html')

def learnphp(request):
    return render(request , 'app/learnphp.html')

def learnpython(request):
    return render(request , 'app/learnpython.html')

def learndjango(request):
    return render(request , 'app/learndjango.html')

def learnsql(request):
    return render(request  , 'app/learnsql.html')

#====================END OF PROGRAMMING VIEWS ==============


#contact view
def contact(reqeust):
    return render(reqeust , 'app/contact.html')

# ======================REGISTRATION VIEW=================
class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', {'form':form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations! Registered Successfully!')
            form.save()
        return render(request, 'app/customerregistration.html', {'form':form})
    
# ================LOGIN VIEW============================
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("password"), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'app/contact.html', {'form':form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            city = form.cleaned_data['city']
            district = form.cleaned_data['district']
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']
            reg = Customers(user=usr, fname=fname, lname=lname, city=city, district=district, number=number, message=message)
            messages.success(request, 'Congratulations!! Profile Updated Successfully')
            reg.save()
        return render(request, 'app/contact.html', {'form':form})

