from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, Lesson, Learner, Question, Choice, Submission


def course_details(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, "onlinecourse/course_details_bootstrap.html", {"course": course})


@login_required
def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    if request.method != "POST":
        return redirect("course_details", course_id=lesson.course_id)

    learner, _ = Learner.objects.get_or_create(user=request.user)
    questions = lesson.questions.prefetch_related("choices").all()
    if not questions.exists():
        messages.error(request, "This lesson does not have an exam yet.")
        return redirect("course_details", course_id=lesson.course_id)

    # A fresh submission is recorded for every question in this attempt.
    for question in questions:
        choice_id = request.POST.get(f"question_{question.id}")
        selected = Choice.objects.filter(pk=choice_id, question=question).first()
        Submission.objects.create(
            learner=learner,
            question=question,
            selected_choice=selected,
            is_correct=bool(selected and selected.is_correct),
        )

    request.session["last_exam_lesson_id"] = lesson.id
    return redirect("show_exam_result", lesson_id=lesson.id)


@login_required
def show_exam_result(request, lesson_id):
    lesson = get_object_or_404(Lesson, pk=lesson_id)
    learner = get_object_or_404(Learner, user=request.user)
    # Show the latest attempt by selecting the latest submission timestamp per question.
    latest_by_question = []
    for question in lesson.questions.prefetch_related("choices").all():
        attempt = Submission.objects.filter(
            learner=learner, question=question
        ).order_by("-submitted_at", "-id").first()
        if attempt:
            latest_by_question.append((question, attempt))

    total = len(latest_by_question)
    correct = sum(1 for _, attempt in latest_by_question if attempt.is_correct)
    score = round((correct / total) * 100) if total else 0
    results = [
        {"question": question, "submission": attempt,
         "correct_choice": question.choices.filter(is_correct=True).first()}
        for question, attempt in latest_by_question
    ]
    return render(request, "onlinecourse/exam_result.html", {
        "lesson": lesson, "results": results, "total": total,
        "correct": correct, "score": score,
    })
