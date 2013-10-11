# -*- coding: utf-8 -*-

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import date
from vom.models import *
from vom.forms import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotAllowed
from django.core.urlresolvers import reverse

@login_required
def index(request):
    if request.method == "GET":
        answers = request.user.answer_set.all()

        # 중복제거 안된상태의 list
        _questions = [q.question for q in answers]

        # 중복 제거된 상태의 query_set
        questions = Question.objects.filter(pk__in=[q.pk for q in _questions])

        variables = {'questions': questions}
        requestContext = RequestContext(request, variables)

        return render_to_response('index.html', requestContext)
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def createAnswer(request):
    if request.method == "GET":
        variables = {}

        if request.user.dateOfRecevingLastQuestion < date.today():
            answeredQuestions = [a.question.pk 
                                for a in request.user.answer_set.all()]
            try:
                questions = Question.objects.exclude(pk__in=answeredQuestions)
                question = questions.order_by('?')[0]
            except:
                assert False, u"답변하지 않은 질문이 존재하지 않습니다."
            else:
                request.user.dateOfRecevingLastQuestion = date.today()
                request.user.point = True
                request.user.questionOfToday = question

                if request.user.status.count == request.user.status.star.dot:
                    Item.objects.create(
                        user=request.user,
                        stuff=request.user.status.star
                    )
                    _items = Item.objects.filter(user=request.user)
                    items = [i.pk for i in _items]
                    constellations = Constellation.objects.exclude(pk__in=items)
                    constellation = constellations.order_by('?')[0]
                    request.user.status.star = constellation
                    request.user.status.count = 0

                request.user.save()
        else:
            question = request.user.questionOfToday

        answer = request.user.answer_set.filter(question=question)

        variables['form'] = AnswerForm()
        variables['question'] = question
        variables['answer'] = answer
        variables['star'] = request.user.status.star

        requestContext = RequestContext(request, variables)

        return render_to_response('today.html', requestContext)
    elif request.method == "POST":
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.writer = request.user
            answer.question = request.user.questionOfToday
            answer.star = request.user.status.star
            answer.save()

            if request.user.point:
                request.user.point = False
                request.user.save()
                status = request.user.status
                status.count += 1
                status.save()

            return HttpResponseRedirect(
                reverse(
                    'showAnswer',
                    kwargs={'pk': request.user.questionOfToday.pk},
                )
            )
        else:
            requestContext = RequestContext(request, {'form': form})
            return render_to_response('today.html', requestContext)
    else:
        return HttpResponseNotAllowed(['POST'])

# @login_required
# def questions(request):
#     answers = request.user.answer_set.all()

#     #중복제거 안된상태의 list
#     _questions = [q.question for q in answers]

#      #중복 제거된 상태의 query_set
#     questions = Question.objects.filter(pk__in=[q.pk for q in _questions])

#     variables = {'questions': questions}
#     requestContext = RequestContext(request, variables)

#     return render_to_response('questions.html', requestContext)

@login_required
def showAnswer(request, pk):
    if request.method == "GET":
        question = Question.objects.get(pk=pk)
        answers = question.answer_set.filter(writer=request.user)

        variables = {
            'answers': answers,
            'question': question,
            'status': request.user.status,
            'star': answers[0].star,
        }
        requestContext = RequestContext(request, variables)

        return render_to_response('showAnswer.html', requestContext)
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])

def join(request):
    if request.method == "POST":
        form = JoinForm(request.POST)

        if form.is_valid():
            user = VomUser.objects.create_user(
                    email=form.cleaned_data['email'],
                    name=form.cleaned_data['name'],
                    birthday=form.cleaned_data['birthday'],
                    sex=form.cleaned_data['sex'],
                    password=form.cleaned_data['password'],
            )
            # import ipdb;ipdb.set_trace()
            Status.objects.create(
                user=user,
                star=Constellation.objects.order_by('?')[0]
            )

            return HttpResponseRedirect(reverse('login'))
    elif request.method == "GET":
        form = JoinForm()
    else:
        return HttpResponseNotAllowed(['POST', 'GET'])

    variables = {'form': form}
    requestContext = RequestContext(request, variables)

    return render_to_response('registration/join.html', requestContext)

@login_required
def cogwheel(request):
    if request.method == "GET":
        return render_to_response('setting.html')
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def stars(request):
    if request.method == "GET":
        variables = {}

        constellations = Item.objects.filter(user=request.user)

        variables['constellations'] = constellations
        variables['star'] = request.user.status.star

        requestContext = RequestContext(request, variables)
        return render_to_response('star.html', requestContext)
    else:
        return HttpResponseNotAllowed(['GET'])

@login_required
def showConstellation(request, name):
    if request.method == "GET":
        constellation = Constellation.objects.get(name=name)
        answers = constellation.answer_set
        _questions = [a.question for a in answers.filter(writer=request.user)]
        questions = Question.objects.filter(pk__in=[q.pk for q in _questions])

        variables = {'questions': questions, 'constellation': constellation}
        requestContext = RequestContext(request, variables)

        return render_to_response(
            'constellationRelatedQuestion.html',
            requestContext,
        )
    else:
        return HttpResponseNotAllowed(['GET'])

def test(request):
    from django.core import serializers

    data = serializers.serialize(
        "json", Answer.objects.all(),
        fields=('date', 'writer')
    )
    return HttpResponse(data, content_type="application/json")
