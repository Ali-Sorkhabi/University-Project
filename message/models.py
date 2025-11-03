from django.db import models

class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title


class Home2(models.Model):
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    user_complaints = models.TextField(blank=True, null=True)  # شکایات
    user_questions = models.TextField(blank=True, null=True)   # سوالات
    criticisms = models.TextField(blank=True, null=True)       # انتقادات
    other_items = models.TextField(blank=True, null=True)      # سایر موارد
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title


class Home3(models.Model):
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.title
