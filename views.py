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


def show_exam_result(request):
    submissions = Submission.objects.all()

    total_questions = submissions.count()
    return render(request, "exam_result.html", {
        "submissions": submissions,
        "total": total_questions
    })
