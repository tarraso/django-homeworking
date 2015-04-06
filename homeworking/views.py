from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

from .models import HomeworkSheet, Homework, StudentSentence


def assignment(request, homework_sheet_id):
    """
        homework_sheet homework_sheet page where student can see all sentences and fill them
    """
    try:
        homework_sheet =  HomeworkSheet.objects.prefetch_related("sentences").get(pk=homework_sheet_id)
    except ObjectDoesNotExist:
        raise Http404("Assignment does not exist")
    if request.method == "GET":
        context = {
            "homework_sheet": homework_sheet, 
            "sentences": homework_sheet.sentences.all(),
            }
        return render(request, "homeworking/assignment.html", context)

    if request.method == "POST":
        homework = Homework(name=request.POST.get("name"), homework_sheet_id = homework_sheet.pk)
        homework.save()
        student_sentences = []
        for sentence in homework_sheet.sentences.all():
            sentence_text = request.POST.get("sentence_%s"%sentence.pk)
            student_sentence = StudentSentence(sentence_text=sentence_text, 
                homework_id=homework.pk, original_sentence_id=sentence.pk)
            student_sentence.save()
            student_sentences.append(student_sentence)
        return render(request, "homeworking/thanks.html")
