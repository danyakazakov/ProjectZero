from django.views.generic import TemplateView

class AboutTechView(TemplateView):
    template_name = 'about/tech.html'

class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'

