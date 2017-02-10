# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexTemplateView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexTemplateView, self).get_context_data(**kwargs)
		
		
		context.update(data)
		return context