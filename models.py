from django.db import models

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Enrollment Model
class Enrollment(models.Model):
    student_name = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


# Question Model
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    grade = models.IntegerField(default=1)

    def __str__(self):
        return self.question_text

    def is_get_score(self, selected_choice):
        return selected_choice.is_correct


# Choice Model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


# Submission Model
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id}"
