from django.shortcuts import render

def home_page(request):

  if request.method == 'POST':
  	  item = request.POST.get('food')
  	  address = request.POST.get("address")

  	  return render(request,'waimai/home_page.html',{'food': item,'address': address})

  return render(request, 'waimai/home_page.html')  	  
# Create your views here.
