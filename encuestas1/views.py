from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choise, Question, Survey
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
# Create your views here.


def index(request):
    # questions = Question.objects.all()
    surveys = Survey.objects.filter(active=True).order_by('-pub_date')[:5]
    # output = ', '.join([q.question_text for q in questions])
    template = loader.get_template('encuestas/index.html')
    context = {
        'mensaje': "Lista de encuestas",
        'surveys': surveys,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Survey.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")
    context = {
        'mensaje': "Detalle de la encuesta",
        'question': question
    }
    return render(request, 'encuestas/detail.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choise_set.get(pk=request.POST['choice'])
    except (KeyError, Choise.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'encuestas/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('encuestas1:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'encuestas/results.html', {'question': question})
