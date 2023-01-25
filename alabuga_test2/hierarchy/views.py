from django.shortcuts import render
from .models import lords, soldiers, slaves_of_lords, slaves_of_soldiers

# Create your views here.
def hierarchy(request):
    lords_citizens = lords.objects.all()
    soldiers_citizens = soldiers.objects.all()
    slaves1_citizens = slaves_of_lords.objects.all()
    slaves2_citizens = slaves_of_soldiers.objects.all()
    return render(request, "hierarchy/hierarchy.html",
                    {
                        "lords_citizens": lords_citizens,
                        "soldiers_citizens": soldiers_citizens,
                        "slaves1_citizens": slaves1_citizens,
                        "slaves2_citizens": slaves2_citizens
                    }
                 )