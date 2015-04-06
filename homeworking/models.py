from random import shuffle

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.conf import settings

class AbstractSentence(models.Model):
    """
        Abstract sentence model
    """
    sentence_text = models.CharField(max_length=200)
    
    def clean(self):
        if not self.sentence_text[-1] in ["?", "."]:
            raise ValidationError('Sentence should end in either a question mark (?), or full stop (.)');

    def __unicode__(self):
        return self.sentence_text
    
    class Meta:
        abstract = True

class Sentence(AbstractSentence):
    """
    Original sentence model.
    For sentences written by teacher.
    """

    homework_sheet = models.ForeignKey("HomeworkSheet", related_name="sentences");

    def get_mixed(self):
        """ 
            Mix all words in given sentence.
            Last char stays at the end of sentence.
        """
        splited = self.sentence_text[:-1].split()
        shuffle(splited)
        return " ".join(splited) + self.sentence_text[-1]

class HomeworkSheet(models.Model):
    """
    Homework assignment sheet
    """

    author = models.ForeignKey(User, null=True, blank=True);
    
    def get_url(self):
        try:
            base_url = settings.BASE_URL
        except AttributeError:
            base_url = ""
        return base_url + reverse("assignment", kwargs={"homework_sheet_id":self.pk})

    def __unicode__(self):
        return self.get_url()


class Homework(models.Model):
    """
    Homework done by student
    """

    homework_sheet = models.ForeignKey(HomeworkSheet)
    name = models.CharField(max_length=200)


class StudentSentence(AbstractSentence):
    """
    Sentence written by student
    """
    original_sentence = models.ForeignKey(Sentence)
    homework = models.ForeignKey("Homework", related_name = "sentences")