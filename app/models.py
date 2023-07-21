from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Quiz(TimeStampedModel):
    class QuizType(models.TextChoices):
        SELECTIVE = "SELECTIVE"
        STATE = "STATE"
    question = models.CharField(max_length=256)
    quiz_type = models.CharField(max_length=20, choices=QuizType.choices, default=QuizType.SELECTIVE)
    state_question_answer = models.CharField(max_length=24, null=True, blank=True)    


class QuizOptions(TimeStampedModel):
    quiz = models.ForeignKey("Quiz", on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    is_answer = models.BooleanField(default=False)


