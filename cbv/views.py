from django.shortcuts import render
from django.views.generic import View
#from django.views.generic import TemplateView


class MyView(View):
    http_method_names = [u'get', u'post', u'put', u'patch', u'delete', u'head', u'options', u'trace']
    options = ''
    trace = ''

    def get(self):
        return render(self.request, template_name='')

    def post(self):
        pass

    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]


class RestfulView(object):
    allowed_methods = ["GET", "POST"]

    def __call__(self, request, *args, **kwargs):
        if request.method not in self.allowed_methods or not hasattr(self, request.method):
            return self.method_not_allowed(request)
        return getattr(self, request.method)(request, *args, **kwargs)

    @staticmethod
    def method_not_allowed(request):
        return render(request, "405.html", status=405)

