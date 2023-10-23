from django.views.generic import TemplateView
from django.shortcuts import render
from .form import CurrencyForm
from .nbp_api import FetchAPI


class HomeView(TemplateView):
    template_name = "nbp/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = FetchAPI("http://api.nbp.pl/api/exchangerates/tables/C/").return_data()
        context['nbp_data'] = response

        return context


class GoldView(TemplateView):
    template_name = 'nbp/gold.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = FetchAPI("http://api.nbp.pl/api/cenyzlota/last/90/").return_data()
        context['nbp_data'] = response
        return context


class CurrenciesView(TemplateView):
    template_name = 'nbp/currencies.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CurrencyForm()
        context['nbp_data'] = None
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = CurrencyForm(request.POST)

        if form.is_valid():
            base_currency = form.cleaned_data['currency1'].code
            response = FetchAPI(f"http://api.nbp.pl/api/exchangerates/rates/a/{base_currency}/last/90").return_data()

            context = self.get_context_data()
            context['form'] = form
            context['nbp_data'] = response

            return render(request, self.template_name, context)

        return render(request, self.template_name, {'form': form, 'nbp_data': None})
