from django.views.generic import TemplateView
from django.views.generic import TemplateView 
from .models import Message, Home2, Home3 
from .forms import Home2Form, Home3Form
# from .views import MessageView, Home2View, Home3View 

class MessageView(TemplateView):
    template_name = 'home1.html'


class Home2View(TemplateView):
    template_name = 'home2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            'firstname': 'نام',
            'lastname': 'نام خانوادگی',
            'phonenumber': 'شماره موبایل',
            'user_complaints': 'شکایات',
            'questions': 'سوالات',
            'criticisms': 'انتقادات',
            'other_items': 'سایر موارد',
            'subject': 'موضوع',
            'message': 'پیام',
        }
        return context


class Home3View(TemplateView):
    template_name = 'home3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fields'] = {
            'firstname': 'نام',
            'lastname': 'نام خانوادگی',
            'phonenumber': 'شماره موبایل',
            'subject': 'موضوع',
            'message': 'پیام',
        }
        return context
