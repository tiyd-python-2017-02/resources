from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
# from django.template import loader


def example(request, question_id):
    import requests
    print(requests.get("http://www.google.com").text)
    print(dir(request))
    print(request.GET)
    print(request.POST)
    return render(request, 'polls/index.html', {})

def api(request, question_id):
    q = Question.objects.get(id=question_id)
    print(q)
    data = "id: {}, question_text: '{}', pub_date: '{}', am_i_stupid: '{}'".format(q.id, q.question_text, q.pub_date, q.am_i_stupid)
    return HttpResponse("{" + data + "}", content_type='application/json')


def api_save(request):
    q = Question(question_text=request.POST['question_text'],
                 pub_date=request.POST['pub_date'],
                 am_i_stupid=request.POST['am_i_stupid'])
    q.save()
    
    data = "id: {}, question_text: '{}', pub_date: '{}', am_i_stupid: '{}'".format(q.id, q.question_text, q.pub_date, q.am_i_stupid)
    return HttpResponse("{" + data + "}", content_type='application/json')




def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:10]
    context = {'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': q})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'




def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def charlie_brown(request):
    # somehow get an id, then rturn that question...
    print(dir(request))
    return HttpResponse("Snoopy")
