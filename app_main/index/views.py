# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView
from web_headers.models import WebHeader

class IndexTemplateView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)
		web_headers = None
		if self.request.user.is_authenticated():
			web_headers = WebHeader.objects.all()
		data = {
			'web_headers':web_headers,
			}

		context.update(data)
		return context