from django.views.generic import TemplateView


# class ProfilePage(TemplateView):
#     template_name = 'profiles/profile.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'
