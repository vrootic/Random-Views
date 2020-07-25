import logging
import inspect

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, FormView
from django.urls import reverse
from django.db.utils import IntegrityError

from .forms import UrlMappingCreateForm
from .models import UrlMapping

logger = logging.getLogger(__name__)

class UrlMappingCreateView(FormView):
    form_class = UrlMappingCreateForm
    template_name = 'shortener/urlmapping_form.html'
    success_url = '/shortener'

    def form_valid(self, form):
        try: 
            url_mapping = UrlMapping.objects.get(full_url=form.cleaned_data['full_url'])
        except UrlMapping.DoesNotExist:
            return super(UrlMappingCreateView, self).form_valid(form)
        return redirect('create-view', pk=url_mapping.id)
        
    def post(self, request, *args, **kwargs):
        try:
            url_mapping = UrlMapping(full_url=request.POST.get('full_url'))
            url_mapping.save()
            
            self.kwargs['result'] = url_mapping
            self.kwargs['full_url'] = url_mapping.full_url 
            return redirect('create-view', pk=url_mapping.id)
        except IntegrityError:
            logger.warning(f"{url_mapping.full_url} exists")
            return super(UrlMappingCreateView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            url_mapping = UrlMapping.objects.get(id=self.kwargs.get('pk'))
            self.kwargs['result'] = url_mapping
            self.kwargs['full_url'] = url_mapping.full_url
        except:
            logger.warning(f"No objects found.")
        return super(UrlMappingCreateView, self).get(request, *args, **kwargs)

def resolve_url(request, url_hash):
    try:
        result = UrlMapping.objects.get(url_hash=url_hash)
    except UrlMapping.DoesNotExist:
        raise Http404('not found')
    return redirect(result.full_url)
