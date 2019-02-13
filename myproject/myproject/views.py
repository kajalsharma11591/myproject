from django.http import HttpResponse
def homepage(request):
    return HttpResponse("this is my homepage")

def kajal(request):
    college ="RIET"
    print(college)
    return HttpResponse("I am kajal from"+college)