from django.db import models

# -------------------------
# مدل Login
# -------------------------
class Login(models.Model):
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.title

# -------------------------
# مدل Home1
# -------------------------
class Home1(models.Model):
    title = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/')
    audio = models.FileField(upload_to='audio/')
    video = models.FileField(upload_to='videos/')
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title

# -------------------------
# مدل Home2 (شکایات، سوالات، انتقادات، سایر موارد)
# -------------------------
class Home2(models.Model):
    title = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()

    # لیست موضوع (choices)
    SUBJECT_CHOICES = [
        ('complaint', 'شکایت'),
        ('question', 'سوال'),
        ('criticism', 'انتقاد'),
        ('other', 'سایر'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)

    # فیلدهای تکمیلی
    user_complaints = models.TextField(blank=True, null=True)  # شکایات
    user_questions = models.TextField(blank=True, null=True)   # سوالات
    criticisms = models.TextField(blank=True, null=True)       # انتقادات
    other_items = models.TextField(blank=True, null=True)      # سایر موارد
    message = models.TextField()                               # متن پیام اصلی

    def __str__(self):
        return self.title

# -------------------------
# مدل Home3 (تماس / پیام)
# -------------------------
class Home3(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.subject}"
