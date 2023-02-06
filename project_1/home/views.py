from django.shortcuts import render
from django.http import HttpResponse
from .models import vish
import csv


def form(request):
	return render(request,'form.html')

def add_vish(request):
	name=request.POST['name']
	email=request.POST['email']
	phone=request.POST['phone']
	vish.objects.create(name=name, email=email, phone=phone)
	return render(request,'form.html')
		
	
def write(request):
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=vish_data.csv'
		
		# Create a csv writer
	writer = csv.writer(response)


		# Designate The Model
	vish_data = vish.objects.all()

		# Add column headings to the csv file
	writer.writerow(['Name', 'Email', 'Phone'])

		# Loop Thu and output
	for vishs in vish_data:
		writer.writerow([vishs.name, vishs.email, vishs.phone])

	return response

# Create your views here.
