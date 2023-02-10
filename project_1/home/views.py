from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import vish
import csv
import reportlab
# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# for searching
from django.db.models import Q

# to get id with help of js



def form(request):
	data= vish.objects.all()
	return render(request,'index.html',{'data':data})



def add(request):
	name=request.POST['name']
	email=request.POST['email']
	phone=request.POST['phone']
	vish.objects.create(name=name, email=email, phone=phone)
	data= vish.objects.all()
	return render(request,'index.html',{'data':data})	




def del_(request):
	id=request.GET['id']
	vish.objects.get(id=id).delete()
	data= vish.objects.all()
	return render(request,'index.html',{'data':data})




def upd(request):
	id=request.GET['id']
	data=vish.objects.get(id=id)
	return render(request,'upd.html',{'data':data})	




def upd_details(request):
	v_update=vish()
	v_update.id=request.POST['id']
	v_update.name=request.POST['name']
	v_update.email=request.POST['email']
	v_update.phone=request.POST['phone']
	v_update.save()
	data= vish.objects.all()
	return render(request,'index.html',{'data':data})


def search(request):
	search=request.POST['search']
	data= vish.objects.filter(Q(name=search) | Q(email=search) | Q(phone=search))
	return render(request,'index.html',{'data':data}) 

	

def write_csv(request):
	
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


def write_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=vishss.txt'
	# Designate The Model
	vish_data = vish.objects.all()

	# Create blank list
	lines = []
	# Loop Thu and output
	for vishs in vish_data:
		lines.append(f'{vishs.name}\n{vishs.phone}\n{vishs.email}\n')

	#lines = ["This is line 1\n", 
	#"This is line 2\n",
	#"This is line 3\n\n",
	#"John Elder Is Awesome!\n"]

	# Write To TextFile
	response.writelines(lines)
	return response



# Generate a PDF File vishs List
def write_pdf(request):
	# Create Bytestream buffer
	buf = io.BytesIO()
	# Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	# Add some lines of text
	#lines = [
	#	"This is line 1",
	#	"This is line 2",
	#	"This is line 3",
	#]
	
	# Designate The Model
	vish_data = vish.objects.all()

	# Create blank list
	lines = []

	for vishs in vish_data:
		lines.append(vishs.name)
		lines.append(vishs.phone)
		lines.append(vishs.email)
		lines.append(" ")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='vishs.pdf')


