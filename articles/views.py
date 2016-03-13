# Author: David Good
# Contact: david_good@users.sourceforge.net
# Copyright: This module has been placed in the public domain.

__docformat__ = 'reStructuredText'

from django.views.generic import TemplateView

from articles.models import Article


class HomePageView(TemplateView):
    """
        HomePageView that extends TemplateView
    """

    template_name = 'home.html'
    response_class = ''
    http_method_names = ''

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context

    def dispatch(self, request, *args, **kwargs):
            pass

    def get(self, request, *args, **kwargs):
        return super(HomePageView, self).get(request, *args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        return super(HomePageView, self).render_to_response(context, **response_kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        pass

    def __init__(self, **kwargs):
        super(HomePageView, self).__init__(**kwargs)
