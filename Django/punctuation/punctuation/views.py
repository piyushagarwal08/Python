#ELITEMUS
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')



def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    '''fullcaps = request.GET.get('fullcaps','off')
    newlineremover = request.GET.get('newlineremover','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')'''

    if removepunc == "on":
        punctuations = '''!();:'"\,<>./?@#%^&#*"'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    else:
        return HttpResponse(djtext)
