from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

    def average_score(self):
        votes = self.vote_set.all()
        if votes.exists():
            return round(sum(v.score for v in votes) / votes.count(), 2)
        return "평가 없음"

class Vote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.project.title} - {self.score}"
