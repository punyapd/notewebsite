from django.db import models
from django.db.models.base import ModelState
from django.contrib.auth.models import User


# Create your models here.
class Course(models.Model):
    faculty = models.CharField(max_length=100)

class Semester(models.Model):
    sem = models.CharField(max_length=100)
    faculty = models.ForeignKey(Course, on_delete=models.CASCADE)

class Subject(models.Model):
    faculty = models.ForeignKey(Course, on_delete=models.CASCADE)
    sem = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)

class TuModelQuestions(models.Model):
    date = models.IntegerField()
    model_question = models.ImageField(upload_to='imgs/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class UnitwiseQuestions(models.Model):
    unit = models.IntegerField()
    unit_question = models.TextField(max_length=10000)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class RefrencedBooks(models.Model):
    book = models.FileField(upload_to='file/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=200)

class MicroSyllabus(models.Model):
    syllabus = models.FileField(upload_to='syllabus/')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class TechNews(models.Model):
    tech_image = models.ImageField(upload_to="tech_imgs/", blank=True, null=True)
    news_title = models.CharField(max_length=1000)
    news_description = models.TextField()
    
CATEGORY = (
    ('Sports', 'Sports'),
    ('Tech_news', 'Tech_news')
)

class News(models.Model):
    category = models.CharField(choices=CATEGORY, max_length=100)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imgs/')
    detail = models.TextField()
    add_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "News"

    def __str__(self):
        return self.title

STATE_CHOICES = (
    ('Achham','Achham'),
    ('Arghakhanhi','Arghakhanchi'),
    ('Baglung','Baglung'),
    ('Baitadi','Baitadi'),
    ('Bajhang','Bajhang'),
    ('Bajura','Bajura'),
    ('Banke','Banke'),
    ('Bara','Bara'),
    ('Bardiya','Bardiya'),
    ('Bhaktapur','Bhaktapur'),
    ('Bhojpur','Bhojpur'),
    ('Chitwan','Chitwan'),
    ('Dadeldhura','Dadeldhura'),
    ('Dailekh','Dailekh'),
    ('Dang','Dang'),
    ('Darchula','Darchula'),
    ('Dhading','Dhading'),
    ('Dhankuta','Dhankuta'),
    ('Dhanusha','Dhanusha'),
    ('Dolakha','Dolakha'),
    ('Doti','Doti'),
    ('Eastern Rukum','Eastern Rukum'),
    ('Gorkha','Gorkha'),
    ('Gulmi','Gulmi'),
    ('Humla','Humla'),
    ('Ilam','Ilam'),
    ('Jajarkot','Jajarkot'),
    ('Jhapa','Jhapa'),
    ('Jumla','Jumla'),
    ('Kailali','Kailali'),
    ('Kalikot','Kalikot'),
    ('Kanchanpur','Kanchanpur'),
    ('Kapilvastu','Kapilvastu'),
    ('Kaski','Kaski'),
    ('Kathmandu','Kathmandu'),
    ('Kavrepalanchok','Kavrepalanchok'),
    ('Khotang','Khotang'),
    ('Lalitpur','Lalitpur'),
    ('Lamjung','Lamjung'),
    ('Mahottari','Mahottari'),
    ('Makwanpur','Makwanpur'),
    ('Manang','Manang'),
    ('Morang','Morang'),
    ('Mugu','Mugu'),
    ('Mustang','Mustang'),
    ('Myagdi','Myagdi'),
    ('Nawalpur','Nawalpur'),
    ('Nuwakot','Nuwakot'),
    ('Okhaldhunga','Okhaldhunga'),
    ('Palpa','Palpa'),
    ('Panchthar','Panchthar'),
    ('Parasi','Parasi'),
    ('Parbat','Parbat'),
    ('Parsa','Parsa'),
    ('Pyuthan','Pyuthan'),
    ('Ramechhap','Ramechhap'),
    ('Rasuwa','Rasuwa'),
    ('Rautahat','Rautahat'),
    ('Rolpa','Rolpa'),
    ('Rupandehi','Rupandehi'),
    ('Salyan','Salyan'),
    ('Sankhuwasabha','Sankhuwasabha'),
    ('Saptari','Saptari'),
    ('Sarlahi','Sarlahi'),
    ('Sindhuli','Sindhuli'),
    ('Sindhupalchowk','Sindhuplachowk'),
    ('Siraha','Siraha'),
    ('Solukhumbu','Solukhumbu'),
    ('Sunsari','Sunsari'),
    ('Surkhet','Surkhet'),
    ('Syangja','Syangja'),
    ('Tanahun','Tanahun'),
    ('Taplejung','Taplejung'),
    ('Tehrathum','Tehrathum'),
    ('Udayapur','Udayapur'),
    ('Western Rukum','Western Rukum')
)

class Customers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    district = models.CharField(choices=STATE_CHOICES, max_length=200)
    city = models.CharField(max_length=100)
    number = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return str(self.id)