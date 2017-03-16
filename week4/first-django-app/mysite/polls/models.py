from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    am_i_stupid = models.BooleanField()

    def __repr__(self):
        return "Question(id={}, question_text={}, pub_date={}, am_i_stupid={})".format(
        self.id, self.question_text, self.pub_date, self.am_i_stupid)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def do_stuff(self):
        if self.am_i_stupid:
            return "duh"
        else:
            return "good_question"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __repr__(self):
        return "Choice(id={}, choice_text={}, votes={}, question={})".format(
        self.id, self.choice_text, self.votes, self.question)

    def __str__(self):
        return self.choice_text
