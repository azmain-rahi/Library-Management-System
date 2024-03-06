from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField(Genre)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    summary = models.TextField(max_length=1000,null=True,blank=True)

    def __str__(self):
        genre_name = ', '.join([x.name for x in self.genre.all()])
        return f'{self.title} written by {self.author}, a {genre_name} book'
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    


import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,max_length=1,default=uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.RESTRICT)
    due_back = models.DateField()
    imprint = models.CharField(max_length=200)
    borrower = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    LOAN_STATUS = (
        ('m','Maintainance'),
        ('o','On Loan'),
        ('a','Avaiable'),
        ('r','reserved')
    )

    status = models.CharField(choices=LOAN_STATUS,default='a',max_length=1)

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'Id: {self.id}, Title: {self.book.title}'

