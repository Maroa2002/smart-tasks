from django.db import models

# # Create your models here.
# class TaskType(models.Model):
#     title = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title

TASK_TYPE_CHOICES = [
    ('personal', 'personal'),
    ('work', 'work'),
    ('wishlist', 'wishlist'),
    ('school', 'school')
]

class Tasks(models.Model):
    task_title = models.CharField(max_length=200)
    # task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    # , null=True, blank=True
    task_type = models.CharField(max_length=100, choices=TASK_TYPE_CHOICES)
    task_details = models.TextField()
    due_date = models.DateField(default='2023-03-01')
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task_title
# this is a django model