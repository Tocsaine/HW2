from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage


def paginate(objects_list, request, per_page=10):
    paginator = Paginator(objects_list, per_page)
    page_number = request.GET.get('page', 1)

    try:
        page = paginator.page(page_number)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return page


def home(request):
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })

    objects_list = questions
    page = paginate(objects_list, request)

    context = {
        'page': page,
    }
    return render(request, 'index.html', context)


def hot(request):
    questions = []

    for i in range(1, 50):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })

    objects_list = questions
    page = paginate(objects_list, request)

    context = {
        'page': page,
    }
    return render(request, 'hot.html', context)


def tag(request, tag_name):
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })

    objects_list = questions
    page = paginate(objects_list, request)

    context = {
        'page': page,
        'tag_name': tag_name,
    }
    return render(request, 'tagindex.html', context)


def question(request, question_id):
    question = {
        'title': 'title ' + str(question_id),
        'id': question_id,
        'text': 'text' + str(question_id)
    }
    answers = []
    for i in range(1, 13):
        answers.append({
            'id': i,
            'text': 'answer ' + str(i)
        })

    objects_list = answers
    page = paginate(objects_list, request)

    context = {
        'page': page,
        'question': question,
    }
    return render(request, 'question.html', context)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def settings(request):
    return render(request, 'settings.html')
