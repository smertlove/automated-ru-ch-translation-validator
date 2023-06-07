from django.db import models

class Lesson(models.Model):
    number = models.IntegerField()
    name   = models.CharField(max_length=64)


    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Lessons"

    def __str__(self):
        return f"{self.number}) {self.name}"




class ChineseRegexp(models.Model):

    lesson = models.ForeignKey(Lesson, on_delete=models.PROTECT)
    number = models.IntegerField()
    regexp = models.TextField()

    def __str__(self):
        return f"{self.lesson.number}.{self.number}) {self.regexp}"

    class Meta:
        ordering = ["lesson", "number"]
        verbose_name_plural = "Chinese Regexps"