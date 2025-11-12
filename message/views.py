from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Login, Home1, Home2, Home3
from .forms import LoginForm, Home1Form, Home2Form, Home3Form

# صفحه ورود / ثبت نام
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home1')  # بعد از ثبت نام به home1 منتقل شود

    def form_valid(self, form):
        form.save()  # داده‌ها را ذخیره می‌کند
        return super().form_valid(form)

# صفحه آپلود فایل ها
class Home1View(FormView):
    template_name = 'home1.html'
    form_class = Home1Form
    success_url = reverse_lazy('home2')  # بعد از آپلود به home2 منتقل شود

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# صفحه شکایات، سوالات، انتقادات
class Home2View(FormView):
    template_name = 'home2.html'
    form_class = Home2Form
    success_url = reverse_lazy('home3')  # بعد از ارسال به home3 منتقل شود

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            'firstname': 'نام',
            'lastname': 'نام خانوادگی',
            'phonenumber': 'شماره موبایل',
            'user_complaints': 'شکایات',
            'user_questions': 'سوالات',
            'criticisms': 'انتقادات',
            'other_items': 'سایر موارد',
            'subject': 'موضوع',
            'message': 'پیام',
        }
        return context

# صفحه تماس یا پیام
class Home3View(FormView):
    template_name = 'home3.html'
    form_class = Home3Form
    success_url = reverse_lazy('login')  # بعد از ارسال به l
