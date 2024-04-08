from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.
challenges={
    "january":"Task 1",
    "february":"Task 2",
    "march":"Task 3",
    "april":"Task 4",
    "may":"Task 5",
    "june":"Task 6",
    "july":"Task 7",
    "august":"Task 8",
    "september":"Task 9",
    "october":"Task 10",
    "november":"Task 11",
    "december":"Task 12",
}

def index(request):
    list_items=""
    months=list(challenges.keys())
    for month in months:
        capitalised_month=month.capitalize()
        path=reverse("monthly_challenge",args=[month])
        list_items+= f"<li> <a href=\"{path}\"> {capitalised_month} </a> </li>"
    
    return HttpResponse(f"<ul>{list_items}</ul>")




def monthly_challenges_number(request,month):
    months=list(challenges.keys())
    if month>len(months):
        return HttpResponseNotFound("Month not found")
    redirect_month = months[month-1]
    redirect_path = reverse("monthly_challenge",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request,month):
    try:
        challenge_text=challenges[month]
        return render(request,"challenges/task.html",{
            "text":challenge_text,
            "month":month.capitalize()
        })
    except:
        return HttpResponseNotFound("This month isn't supported")


