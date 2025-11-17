from django import forms
from .models import Login, Home1, Home2, Home3

# Choices برای فیلد subject در Home2Form
REQUEST_TYPES = [
    ('complaint', 'شکایت'),
    ('question', 'سوال'),
    ('criticism', 'انتقاد'),
    ('other', 'سایر'),
]

# ----------------------
# فرم Login
# ----------------------
class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['firstname', 'lastname', 'phonenumber', 'email', 'username', 'password']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),
        }

# ----------------------
# فرم Home1 (آپلود فایل‌ها)
# ----------------------
class Home1Form(forms.ModelForm):
    class Meta:
        model = Home1
        fields = ['title', 'file']

# ----------------------
# فرم Home2 (شکایات / سوالات / انتقادات / سایر موارد)
# ----------------------
class Home2Form(forms.ModelForm):
    subject = forms.ChoiceField(choices=REQUEST_TYPES, label='موضوع')

    class Meta:
        model = Home2
        fields = [
            'firstname', 'lastname', 'phonenumber', 'email',
            'subject', 'user_complaints', 'user_questions',
            'criticisms', 'other_items', 'message'
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'user_complaints': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'شکایات', 'rows': 2}),
            'user_questions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'سوالات', 'rows': 2}),
            'criticisms': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'انتقادات', 'rows': 2}),
            'other_items': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'موارد دیگر', 'rows': 2}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'rows': 4}),
        }

# ----------------------
# فرم Home3 (تماس / پیام)
# ----------------------
class Home3Form(forms.ModelForm):
    class Meta:
        model = Home3
        fields = ['firstname', 'lastname', 'phonenumber', 'email', 'subject', 'message']
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'rows': 4}),
        }
