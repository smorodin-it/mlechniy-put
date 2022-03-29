from django.shortcuts import render

# Create your views here.
# TODO: Implement dev/prod logic


def participant_view(request):
    return render(request=request, template_name="dist/apps/participant/index.html")
