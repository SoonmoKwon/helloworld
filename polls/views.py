# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from polls.models import Poll, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def home(request):
    data = {}
    data['name'] = 'kwon soonmo'
    return render(request, 'home.html', data)

def polls(request):
    data = {}
    data['polls'] = Poll.objects.all()
    return render(request, 'polls.html', data)

def polls_process(request):
    data = {}
    if request.method == "POST":
        choice_id = request.POST["choice"]
        print "Choice Id submitted %d" % int(choice_id)
        choice_obj = Choice.objects.get(id=choice_id)
        choice_obj.votes += 1
        choice_obj.save()
    return HttpResponseRedirect(reverse("polls_list"))

@csrf_exempt
def polls_radio(request):
    import json
    data = {}
    if request.method == "POST":
        radio_id = request.POST["radio_id"]
        print "we received radio ID: %s" % radio_id

        choice_id = int(radio_id[1:])
        choice_obj = Choice.objects.get(id=choice_id)
        choice_obj.votes += 1
        choice_obj.save()

        data["radio_id"] = "v%d" % choice_id
        data["votes"] = choice_obj.votes
    else:
        print "Invalid radio button request."

    return HttpResponse(json.dumps(data), mimetype="application/json")