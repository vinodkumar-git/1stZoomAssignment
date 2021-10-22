from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Csv, Product
from .forms import CsvModelForm
import csv

# Create your views here.
def index(request):
    if request.method == "POST":
        searched = request.POST['searched']
        print("you seacrhed for:", searched)
        # products = Product.objects.all()
        # print(products)
        items = Product.objects.filter(name__contains=searched).order_by('name')[:20]
        # items = i.sort()
        print("result is:",items)
        return render(request,'index.html', {'items':items, 'searched':searched})
    else:
        return render(request,'index.html')

def upload_csv(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(active=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    product = row[1]
                    Product.objects.create(
                        name = product,
                    )
                    print(row)
            obj.active = True
            obj.save()
    return render(request, 'upload.html', {'form':form})
