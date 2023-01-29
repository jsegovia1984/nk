from django.shortcuts import render

# Create your views here.
def menu(request):
    data={
        "titulo":"Menu bar 1",
    }

    return(render(request,"menu.html",data))
