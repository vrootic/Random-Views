import logging
import inspect

from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, View
from django.urls import reverse

from .forms import UrlMappingCreateForm
from .models import UrlMapping

logger = logging.getLogger(__name__)

class UrlMappingCreateView(View):
    model = UrlMapping
    form_class = UrlMappingCreateForm

    def get_success_url(self):
        return reverse('create-view', kwargs = {'pk': self.object.id})

    def form_invalid(self, form):
        logger.warning(f"invalid:")

        #url_mapping = UrlMapping.objects.get(full_url=form.cleaned_data['full_url'])
        #return redirect('create-view', pk=url_mapping.id)
        return super(UrlMappingCreateView, self).form_invalid(form)

    def form_valid(self, form):
        logger.warning(f"valid: {form.cleaned_data}")

        return super(UrlMappingCreateView, self).form_valid(form)
    
    def post(self, request, *args, **kwargs):
        try:
            url_mapping = UrlMapping.objects.get(full_url=request.POST.get('full_url'))
            if url_mapping:
                self.kwargs['result'] = url_mapping
                self.kwargs['full_url'] = url_mapping.full_url 
        except UrlMapping.DoesNotExist:
            pass
        return super(UrlMappingCreateView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        logger.warning(f"{self.__class__}.{inspect.currentframe().f_code.co_name}")
        try:
            logger.warning(f"id={self.kwargs.get('pk')}")
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
