from django.shortcuts import render

# Create your views here.

from plyer import notification

def chucknoris(request):
   
    title = "chuck noris"
    message = "Chuck Noris invented irony by pissing a hole through a toilet."
    duration = 200

   
    notification.notify(title=title, message=message, timeout=duration)
    

    return render(request, 'chucknoris.html',{})
