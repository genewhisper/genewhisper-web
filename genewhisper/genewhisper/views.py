from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class ThanksPage(TemplateView):
    template_name = 'thanks.html'


class HomePage(TemplateView):
    template_name = 'index.html'


class TestPage(TemplateView):
    template_name = 'test.html'
#
#
# class ProfileTest(TemplateView):
#     template_name = 'profile_base.html'
