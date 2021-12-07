from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import *
from .seriallizers import *
from .forms import *
from .permissions import IsAuthenticatedOrReadOnly

# template
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



# main
def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


# categorie
def category(request):
    categorie = categories.objects.all()
    if request.method == 'POST':
        error = ''
        form = categoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category') 
        else:
            error = "Форма было неверной"
            
    form = categoryForm()
            
    dataCategory = {
        'categorie' : categorie,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/category.html', {'dataCategory' : dataCategory})


# update button for categorie
def updateCategorie(request, pk):
    categorie = categories.objects.get(id = pk)
    form = categoryForm(instance=categorie)
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'artelApp/update.html', {'form': form, 'categorie': categorie})


# delete button for categorie
def deleteCategorie(request, pk):
    categorie = categories.objects.get(id = pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('category')
    return render(request, 'artelApp/delete.html', {'categorie': categorie})



# goods
def good(request):
    good = goods.objects.all()
    if request.method == 'POST':
        error = ''
        form = goodForm(request.POST, request.FILES) 
        cat = request.POST['cats'] # Biza oldin select ni tanlangan optionini topishimiz kere
        print(f"{cat=}")
        if form.is_valid():
            f = form.save(commit=False) # Keyin SAVE qilamiz
            f.cat_id = categories.objects.get(id=int(cat)) # Form ni CATEGORIY fieldini (FK) belgilimiz
            f.save() # Keyin SAVE qilamiz
            return redirect('good') 
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
            
    form = goodForm()
    categorie = categories.objects.all()        
                
    dataGood = {
        'good' : good,
        'form': form,
        'categorie' : categorie,
        # 'error': error,
    }
    return render(request, 'artelApp/good.html', {'dataGood' : dataGood})


# update button for goods
def updateGoods(request, pk):
    good = goods.objects.get(id = pk)
    form = goodForm(instance=good)
    if request.method == 'POST':
        form = goodForm(request.POST,  request.FILES, instance=good)
        if form.is_valid():
            form.save()
            return redirect('good')
    return render(request, 'artelApp/updateGood.html', {'form': form, 'good': good})


# delete button for categorie
def deleteGoods(request, pk):
    good = goods.objects.get(id = pk)
    if request.method == 'POST':
        good.delete()
        return redirect('good')
    return render(request, 'artelApp/deleteGood.html', {'good': good})


# feedbacks
def feedbacks(request):
    dataFeedback = feedback.objects.all()
    return render(request, 'artelApp/feedback.html', {'dataFeedback' : dataFeedback},)


# stocks
def stock(request):
    stock = stocks.objects.all()
    if request.method == 'POST':
        error = ''
        form = stockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stock') 
        else:
            error = "Форма было неверной"
            
    form = stockForm()
            
    dataStock = {
        'stock' : stock,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/stock.html', {'dataStock' : dataStock})


# update button for categorie
def updateCategorie(request, pk):
    categorie = categories.objects.get(id = pk)
    form = categoryForm(instance=categorie)
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'artelApp/update.html', {'form': form, 'categorie': categorie})


# delete button for categorie
def deleteCategorie(request, pk):
    categorie = categories.objects.get(id = pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('category')
    return render(request, 'artelApp/delete.html', {'categorie': categorie})



# reports
def report(request):
    languages = reportsOfLanguage.objects.all()
    categories = reportsOfCategory.objects.all()
    goods = reportsOfGood.objects.all()
    
    reports = {
        'languages': languages,
        'categories': categories,
        'goods': goods,
    }
    return render(request, 'artelApp/report.html', {'reports' : reports},)


class languageAPIView(ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = languageSerializer
    # permission_classes = (IsAuthenticated)


class categorieAPIView(ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = categorySerializer
    # permission_classes = (IsAuthenticated)
    # permission_classes = (IsAuthenticatedOrReadOnly, )        # from permisstion.py


class goodAPIView(ModelViewSet):
    queryset = goods.objects.all()
    serializer_class = goodSerializer
    # permission_classes = (IsAuthenticated)
    
    
class companiesAPIView(ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializer
    # permission_classes = (IsAuthenticated)
    
    
class infoAPIView(ModelViewSet):
    queryset = info.objects.all()
    serializer_class = infoSerializer
    # permission_classes = (IsAuthenticated)
    
    
class partnersAPIView(ModelViewSet):
    queryset = partners.objects.all()
    serializer_class = partnerSerializer
    # permission_classes = (IsAuthenticated)

class exportsAPIView(ModelViewSet):
    queryset = exports.objects.all()
    serializer_class = exportSerializer
    # permission_classes = (IsAuthenticated)

class ecologiesAPIView(ModelViewSet):
    queryset = ecology.objects.all()
    serializer_class = ecologySerializer
    # permission_classes = (IsAuthenticated)

class innovationsAPIView(ModelViewSet):
    queryset = innovations.objects.all()
    serializer_class = innovationSerializer
    # permission_classes = (IsAuthenticated)


class feedbacksAPIView(ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackSerializer
    # permission_classes = (IsAuthenticated)


class productBasesAPIView(ModelViewSet):
    queryset = product_bases.objects.all()
    serializer_class = productBaseSerializer
    # permission_classes = (IsAuthenticated)


class servicesAPIView(ModelViewSet):
    queryset = services.objects.all()
    serializer_class = serviceSerializer
    # permission_classes = (IsAuthenticated)


class reportOfLanguageAPIView(ModelViewSet):
    queryset = reportsOfLanguage.objects.all()
    serializer_class = reportOfLanguageSerializer
    # permission_classes = (IsAuthenticated)
    
    
class reportOfCategoryAPIView(ModelViewSet):
    queryset = reportsOfCategory.objects.all()
    serializer_class = reportsOfCategorySerializer
    # permission_classes = (IsAuthenticated)


class reportOfGoodAPIView(ModelViewSet):
    queryset = reportsOfGood.objects.all()
    serializer_class = reportsOfGoodSerializer
    # permission_classes = (IsAuthenticated)


class stocksAPIView(ModelViewSet):
    queryset = stocks.objects.all()
    serializer_class = stockSerializer
    # permission_classes = (IsAuthenticated)


class userAPIView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = userSerializer