from django.shortcuts import render

# Create your views here.

def note_doc(request):
    return render(request, 'notes/notes.html')


def api_doc(request):
    return render(request, 'v1/api.html')