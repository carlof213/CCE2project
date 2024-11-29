from django.shortcuts import render
# from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage


class ContactView(FormView):
    template_name = 'contact_choco.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:contact_choco')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        subject = 'お問い合わせ: {}'.format(title)

        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        
        from_email  = 'mcd2476035@stu.o-hara.ac.jp'
        to_list = ['mcd2476035@stu.o-hara.ac.jp']

        message = EmailMessage(subject = subject,
                               body = message,
                               from_email = from_email,
                               to = to_list,
                               )
        
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        
        return super().form_valid(form)