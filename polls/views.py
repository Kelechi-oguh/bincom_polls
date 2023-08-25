from django.shortcuts import render, Http404, HttpResponse
from .models import PollingUnit, AnnouncedPuResults, Lga
from .forms import polling_unit_form, result_form

# Create your views here.

def home(request):
    context =  {
        "Question_1": "/unit/<int:polling_unit_uniqueid>/",
        "Question_2": "/lga/<int:lga_id>/",
        "Question_3": "/unit/new/"
    }
    return render(request, 'base.html', context)


# Question_1
def polling_unit_result(request, unitid):
    try:
        pu = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=unitid)
        context = {'unit': pu}
    except pu is None:
        raise Http404("Poll does not exist")
        context = {}
    finally:
        return render(request, 'pu_results.html', context)


# Question_2
def lga_result_sum(request, _id):
    try:
        lga = Lga.objects.get(lga_id=_id)

        pu = PollingUnit.objects.filter(lga_id=lga.lga_id)
        context = {
            "lga": lga
        }
        parties = {}
        for i in pu:
            pu_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=i.polling_unit_id)
            if pu_result.exists():
                for i in pu_result:
                    if i.party_abbreviation in parties:
                        parties[i.party_abbreviation] += i.party_score
                    else:
                        parties[i.party_abbreviation] = 0
                        parties[i.party_abbreviation] += i.party_score
        
        context["parties"] = parties
        
    except:
      raise Http404("Not found")
    finally:
        return render(request, 'lga_result.html', context)


# Question_3
def new_polling_unit(request):
    poll_form = polling_unit_form()
    result = result_form()
    context = {
        "poll": poll_form,
        "result": result
        }
    if request.method == 'POST':
        context = {}
        poll_form = polling_unit_form(request.POST)
        result = result_form(request.POST)
        if poll_form.is_valid():
            # poll_form.save()
            context['poll'] = poll_form
        if result.is_valid():
            # result.save()
            context['result'] = result_form

    return render(request, 'new.html', context=context)
