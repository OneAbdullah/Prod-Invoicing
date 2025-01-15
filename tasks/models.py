from django.db import models
from django.contrib.auth.models import User

status_choices = (
    ('Active','Active'),
    ('Closed','Closed')
)

priority_choices = (
    ('P1','P1'),
    ('P2','P2'),
    ('P3','P3')
)

class user_tasks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_from")
    assigned = models.ForeignKey(User,on_delete=models.CASCADE,related_name="assigned_to")
    status = models.CharField(max_length=20,choices=status_choices,default='Active')
    desc = models.TextField(max_length=1000,null=True,blank=True)
    priority = models.CharField(max_length=20,choices=priority_choices,default='P1')
    deadline = models.DateField(null=True,blank=True)
    last_updated_at = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return "{} assigned to {} : {}".format(self.user.username, self.assigned.username, self.desc)
    
    def get_latest_update(self):
        try:
            obj = user_tasks_log.objects.filter(task=self).last()
            return obj.note
        except:
            return "No updates yet!"
    
class user_tasks_log(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(user_tasks,on_delete=models.CASCADE)
    note = models.TextField(max_length=2000,null=True,blank=True)
    is_close = models.BooleanField(default=False)
    added_at = models.DateTimeField(null=True,blank=True)