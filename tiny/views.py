from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.base import RedirectView

from django.shortcuts import redirect

from tiny.models import Link

class LinkCreate(CreateView):
    model = Link
    fields = ['url']
    # template_name = "templates/link/link_form.html"

    def form_valid(self, form):
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect('link_show', token=prev[0].token)
        return super(LinkCreate, self).form_valid(form)

class LinkShow(DetailView):
    model = Link
    slug_field = 'token'
    slug_url_kwarg = 'token'

    def get_context_data(self, **kwargs):
        context = super(LinkShow, self).get_context_data(**kwargs)
        protocol = 'http'
        if self.request.is_secure:
            protocol = 'https'
        context['url_base'] = protocol + "//" + self.request.get_host() + "/r/"
        return context
    
class RedirectUrlView(RedirectView):
    
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        short_url = kwargs['short_url']
        return Link.expand(short_url)
