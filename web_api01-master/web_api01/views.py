from django.http import HttpResponse
import os
from django.shortcuts import render
 
def generate_file(request):
    return_code=os.system('python /data/web_api01/web_api01/job/run.py')
    if return_code == 0: 
       return HttpResponse("job runs success!")
    else:
       return HttpResponse("job runs error!")

def front(request):
   return render(request, 'xj_front.html')
