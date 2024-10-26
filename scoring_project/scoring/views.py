from django.shortcuts import render
from .forms import ScoringForm
import requests


def get_data(request):
    """
    Генерация страницы скоринга
    """

    template = 'scoring/index.html'
    title = 'scoring'
    result = 'no info'

    scoring_form = ScoringForm()
    # Получение из форм данных для json-шаблона 
    # после выполнения POST запооса
    if request.method == 'POST':

        scoring_form = ScoringForm(request.POST)
        scoring_form.save()

        dict_data = dict(scoring_form.cleaned_data)
        clean_data = list(dict_data.values())
        api_message = requests.post(
            'http://127.0.0.1:5000/api/v1/get_data/',
            json={'client_form': [clean_data]})
        result = api_message.json()['result']

    context = {'scoring_form': scoring_form, 'title': title, 'result': result}

    return render(request, template, context=context)
