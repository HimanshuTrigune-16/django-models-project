from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission

def submit(request):
    if request.method == "POST":
        question_id = request.POST.get("question_id")
        choice_id = request.POST.get("choice_id")

        question = get_object_or_404(Question, id=question_id)
        choice = get_object_or_404(Choice, id=choice_id)

        Submission.objects.create(
            question=question,
            selected_choice=choice
        )

        return render(request, "result.html", {"question": question, "choice": choice})

    return render(request, "submit.html")


def show_exam_result(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    submissions = Submission.objects.filter(course=course)

    total_score = 0
    possible_score = 0
    selected_ids = []

    for submission in submissions:
        choices = submission.choices.all()
        for choice in choices:
            selected_ids.append(choice.id)
            if choice.is_correct:
                total_score += choice.question.grade
        possible_score += submission.question.grade

    context = {
        'course': course,
        'selected_ids': selected_ids,
        'grade': total_score,
        'possible': possible_score
    }

    return render(request, 'exam_result_bootstrap.html', context)
