from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import user_tasks,user_tasks_log
from datetime import date, datetime
from django.contrib.auth.decorators import login_required

# show 1 : Active Tasks
# show 2 : Closed Tasks
# show 3 : Tasks I Created
@login_required(login_url='/')
def home(request,show):
    template = "tasks/home.html"
    context = {"show":show}

    if show == 1:
        context['tasks'] = user_tasks.objects.filter(assigned=request.user, status="Active")
    elif show == 2:
        context['tasks'] = user_tasks.objects.filter(assigned=request.user, status="Closed")
    else:
        context['tasks'] = user_tasks.objects.filter(user=request.user)

    return render(request,template,context)
    
@login_required(login_url='/')
def create_task(request):
    template = "tasks/new_task.html"
    context = {}

    context['users'] = User.objects.all()

    if request.method == "POST":
        if request.POST['note'] and request.POST['user'] and request.POST['priority'] and request.POST['deadline']:
            obj = user_tasks()
            obj.user = request.user
            obj.assigned = User.objects.get(pk=int(request.POST['user']))
            obj.desc = request.POST['note']
            obj.priority = request.POST['priority']
            temp = request.POST['deadline'].split('-')
            obj.deadline = date(year=int(temp[0]), month=int(temp[1]), day=int(temp[2]))
            obj.last_updated_at = datetime.now()
            obj.save()

            return redirect("/task-dashboard/3")

    return render(request,template,context)

@login_required(login_url='/')
def task_detail(request,id,show):
    template = "tasks/task_detail.html"
    context = {"closure":False}

    taskobj = user_tasks.objects.get(pk=int(id))
    context['taskobj'] = taskobj
    context['tasklogs'] = user_tasks_log.objects.filter(task=taskobj)
    context['show'] = show

    if request.method == "POST":
        obj = user_tasks_log()
        obj.user = request.user
        obj.task = taskobj
        obj.note = request.POST['note']
        obj.added_at = datetime.now()
        obj.save()
        taskobj.last_updated_at = obj.added_at
        taskobj.save()

        return redirect("/task-dashboard/{}".format(show))

    return render(request,template,context)

@login_required(login_url='/')
def task_close(request,id,show):
    template = "tasks/task_detail.html"
    context = {"closure":True}

    taskobj = user_tasks.objects.get(pk=int(id))
    context['taskobj'] = taskobj
    context['tasklogs'] = user_tasks_log.objects.filter(task=taskobj)
    context['show'] = show

    if request.method == "POST":
        obj = user_tasks_log()
        obj.user = request.user
        obj.task = taskobj
        obj.note = request.POST['note']
        obj.is_close = True
        obj.added_at = datetime.now()
        obj.save()
        taskobj.last_updated_at = obj.added_at
        taskobj.status = "Closed"
        taskobj.save()

        return redirect("/task-dashboard/{}".format(show))

    return render(request,template,context)