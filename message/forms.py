from django import forms
from .models import Home2, Home3

# class Home2Form(forms.ModelForm):
    # class Meta:
        # models = Home2 
        # fields = [
            # 'firstname',
            # 'lastname',
            # 'phonenumber',
            # 'subject',
            # 'message',
        # ]
# لیست انتخابی موضوع
REQUEST_TYPES = [
    ('complaint', 'شکایات'),
    ('question', 'انتقادات'),
    ('criticism', 'سوالات'),
    ('other', 'سایر موارد'),
]

# فرم Home2 با ModelForm
class Home2Form(forms.ModelForm):
    # بازنویسی فیلد subject برای انتخابی بودن
    subject = forms.ChoiceField(choices=REQUEST_TYPES, label='موضوع')

    class Meta:
        model = Home2
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'subject',
            'message',
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره موبایل'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام', 'rows': 4}),
        }

class Home3Form(forms.ModelForm):
    class Meta:
        models = Home3 
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'subject',
            'message',
        ]