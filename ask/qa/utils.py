from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def get_question_list(request, qs):
    paginator = Paginator(qs, 2)
    page_number = request.GET.get('page', 10)
    try:
        questions = paginator.page(page_number)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return questions
