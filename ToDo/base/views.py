from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.
def home(request):
    todo_objects= Todo.objects.all()# query all object from class
    content={'todo':todo_objects}
    return render(request,"index.html",context=content)# context le chai web ma dekhauni kam garxa 
def create(request):
    if request.method=='POST':# url request hit gardah request method hit hunna so hamile if condiition lagako
      name=request.POST.get('name') # bracket ma vako name des status cahi key hunxa ahi
      description=request.POST.get('description')
      status=request.POST.get('status')
      Todo.objects.create(name=name,description=description,status=status)# name vayo key euta ani arko name value 
      return redirect(to='home')
    content={'method':'create'}
    return render(request,'create.html',context=content)
         
def edit(request,pk):
   todo_object = Todo.objects.get(id=pk)# edit le euta lai matra query garxa ani id vaneko tw specipic field ho ani pk chai value match huni object lai chai lerauxa table bata
   if request.method=='POST':
    new_name=request.POST.get('name')# hamile () brackeyt ma vako name arkai lekhdah pni hunxa ani create.html ma vako input ko name = name pni change gardah hunxa yo name chai as a key ho ani create.html ma value ko lagi matra ho
    description=request.POST.get('description')
    status=request.POST.get('status') # ani status ma chai name status xa value jun select gareko xa tei ho 
    todo_object.name=new_name# yo new_name vaneko chai variable call gareko(.name xa ni yo chai model ko field ho ani= name chai variable ho hamile mathi left hand ko j lekhyo tei lekhni ho aba name=request.POST.get('name') lai chai name variable ko name chai new_name lekhyo vani tala right part ko =name lai pni new_name rakhnu parni hunxa ) ani arko kura left ma chai jaba object ko attribute lai call garxau ni tyo attribute chai object ma  vako field nai ho right handside ma chai value pass garni ho
    # tesai garera yo key haru chai kaha bata aayo vani get gardah feri jati pni input xa  create.html ma tes ma vako name haru ho like name= name xa name= description xa ani status ma chai name status xa value jun select gareko xa tei ho  yehe bata ho key aako ani status ma chai hamile value rakhna mildae na  sidae option lai select garni ho yedi object ko status done xa vani done lai selected ani not done xa vani not selected wala code rakhxa so  selected chai render hunxa  select chai navako render hunna nai elif chai rakhnu parxa kina vani yo python o area hoina so keyword lai end garnu parxa
    todo_object.description=description
    todo_object.status=status
    todo_object.save()# yo save chai models.model ko method ho jun le chai database mai change gardinxa 
    return redirect(to='home')

   content={'method':'edit', 'object':todo_object} 
   return render(request,'create.html',context=content)