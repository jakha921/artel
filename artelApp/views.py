from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import *
from .seriallizers import *
from .forms import *
from .permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required



# main
@login_required(login_url='/admin/login/')
def index(request):
    return render(request, 'artelApp/index.html')


# categorie
@login_required(login_url='/admin/login/')
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
@login_required(login_url='/admin/login/')
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
@login_required(login_url='/admin/login/')
def deleteCategorie(request, pk):
    categorie = categories.objects.get(id = pk)
    if request.method == 'POST':
        categorie.delete()
        return redirect('category')
    return render(request, 'artelApp/delete.html', {'categorie': categorie})



# goods
@login_required(login_url='/admin/login/')
def good(request):
    good = goods.objects.all()
    if request.method == 'POST':
        error = ''
        form = goodForm(request.POST, request.FILES) 
        cat = request.POST['category_id'] # Biza oldin select ni tanlangan optionini topishimiz kere
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
@login_required(login_url='/admin/login/')
def updateGoods(request, pk):
    good = goods.objects.get(id = pk)
    form = goodForm(instance=good)
    if request.method == 'POST':
        form = goodForm(request.POST,  request.FILES, instance=good)
        cat = request.POST['category_id']
        print(f"{cat=}") 
        if form.is_valid():
            f = form.save(commit=False)
            f.cat_id = categories.objects.get(id=int(cat))
            form.save()
            return redirect('good')
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
                
    categorie = categories.objects.all() 
                
    dataGood = {
        'good' : good,
        'form': form,
        'categorie' : categorie,
        # 'error': error,
    }
    return render(request, 'artelApp/updateGood.html', {'dataGood' : dataGood})


# delete button for categorie
@login_required(login_url='/admin/login/')
def deleteGoods(request, pk):
    good = goods.objects.get(id = pk)
    if request.method == 'POST':
        good.delete()
        return redirect('good')
    return render(request, 'artelApp/deleteGood.html', {'good': good})


# good_image
@login_required(login_url='/admin/login/')
def goodImage(request):
    goodImage = good_images.objects.all()
    if request.method == 'POST':
        error = ''
        form = goodImageForm(request.POST, request.FILES) 
        good = request.POST['good_id']
        print(f"{good=}")
        if form.is_valid():
            f = form.save(commit=False)
            f.good_id = goods.objects.get(id=int(good))
            f.save()
            return redirect('goodImage') 
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
            
    form = goodImageForm()
    good = goods.objects.all() 
                
    dataGoodImage = {
        'goodImage' : goodImage,
        'form': form,
        'good' : good,
        # 'error': error,
    }
    return render(request, 'artelApp/goodImage.html', {'dataGoodImage' : dataGoodImage})


# update button for goods
@login_required(login_url='/admin/login/')
def updateGoodImage(request, pk):
    goodImage = good_images.objects.get(id = pk)
    form = goodImageForm(instance=goodImage)
    if request.method == 'POST':
        form = goodImageForm(request.POST,  request.FILES, instance=goodImage)
        cat = request.POST['good_id']
        print(f"{cat=}") 
        if form.is_valid():
            f = form.save(commit=False)
            f.cat_id = goods.objects.get(id=int(cat))
            f.save()
            return redirect('goodImage')
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
                


    good = goods.objects.all() 
                
    dataGoodImage = {
        'goodImage' : goodImage,
        'form': form,
        'good' : good,
        # 'error': error,
    }
    return render(request, 'artelApp/updateGoodImage.html', {'dataGoodImage' : dataGoodImage})


# delete button for goodImage
@login_required(login_url='/admin/login/')
def deleteGoodImage(request, pk):
    goodImage = good_images.objects.get(id = pk)
    if request.method == 'POST':
        goodImage.delete()
        return redirect('goodImage')
    return render(request, 'artelApp/deleteGoodImage.html', {'goodImage': goodImage})


# GoodSection
@login_required(login_url='/admin/login/')
def goodSections(request):
    goodSection = good_section.objects.all()
    if request.method == 'POST':
        error = ''
        form = goodSectionForm(request.POST, request.FILES)
        good = request.POST['good_id']
        print(f"{good=}")
        if form.is_valid():
            f = form.save(commit=False)
            f.good_id = goods.objects.get(id=int(good))
            f.save()
            return redirect('goodSections') 
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
            
    form = goodSectionForm()
    good = goods.objects.all() 
                
    dataGoodSection = {
        'goodSection' : goodSection,
        'form': form,
        'good' : good,
        # 'error': error,
    }
    return render(request, 'artelApp/goodSection.html', {'dataGoodSection' : dataGoodSection})


# update button for goods
@login_required(login_url='/admin/login/')
def updateGoodSections(request, pk):
    goodSection = good_section.objects.get(id = pk)
    form = goodSectionForm(instance=goodSection)
    if request.method == 'POST':
        form = goodSectionForm(request.POST,  request.FILES, instance=goodSection)
        cat = request.POST['good_id']
        print(f"{cat=}") 
        if form.is_valid():
            f = form.save(commit=False)
            f.cat_id = goods.objects.get(id=int(cat))
            f.save()
            return redirect('goodSections')
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
                
    good = goods.objects.all() 
                
    dataGoodSection = {
        'goodSection' : goodSection,
        'form': form,
        'good' : good,
        # 'error': error,
    }
    return render(request, 'artelApp/updateGoodSection.html', {'dataGoodSection' : dataGoodSection})


# delete button for goodImage
@login_required(login_url='/admin/login/')
def deleteGoodSections(request, pk):
    goodSection = good_section.objects.get(id = pk)
    if request.method == 'POST':
        goodSection.delete()
        return redirect('goodSections')
    return render(request, 'artelApp/deleteGoodSection.html', {'goodSection': goodSection})


# GoodSection
@login_required(login_url='/admin/login/')
def goodSectionDescriptions(request):
    goodSectionDescription = good_section_description.objects.all()
    if request.method == 'POST':
        error = ''
        form = goodSectionDescriptionForm(request.POST, request.FILES)
        good = request.POST['good_section_id']
        print(f"{good=}")
        if form.is_valid():
            f = form.save(commit=False)
            f.good_section_id = good_section.objects.get(id=int(good))
            f.save()
            return redirect('goodSectionDescriptions') 
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
            
    form = goodSectionDescriptionForm()
    goodSection = good_section.objects.all() 
                
    dataGoodSectionDescription = {
        'goodSectionDescription' : goodSectionDescription,
        'form': form,
        'goodSection' : goodSection,
        # 'error': error,
    }
    return render(request, 'artelApp/goodSectionDescription.html', {'dataGoodSectionDescription' : dataGoodSectionDescription})


# update button for goods
@login_required(login_url='/admin/login/')
def updateGoodSectionDescriptions(request, pk):
    goodSectionDescription = good_section_description.objects.get(id = pk)
    form = goodSectionDescriptionForm(instance=goodSectionDescription)
    if request.method == 'POST':
        form = goodSectionDescriptionForm(request.POST,  request.FILES, instance=goodSectionDescription)
        cat = request.POST['good_section_id']
        print(f"{cat=}") 
        if form.is_valid():
            f = form.save(commit=False)
            f.cat_id = good_section.objects.get(id=int(cat))
            f.save()
            return redirect('goodSectionDescriptions')
        else:
            error = "Форма было неверной"
            print(f"{error=}")
            for field in form:
                print(f"Field Error: {field.name} | {field.errors}")
                
    goodSection = good_section.objects.all() 
                
    dataGoodSectionDescription = {
        'goodSectionDescription' : goodSectionDescription,
        'form': form,
        'goodSection' : goodSection,
        # 'error': error,
    }
    return render(request, 'artelApp/updateGoodSectionDescription.html', {'dataGoodSectionDescription' : dataGoodSectionDescription})


# delete button for goodImage
@login_required(login_url='/admin/login/')
def deleteGoodSectionDescriptions(request, pk):
    goodSectionDescription = good_section_description.objects.get(id = pk)
    if request.method == 'POST':
        goodSectionDescription.delete()
        return redirect('goodSectionDescriptions')
    
    return render(request, 'artelApp/deleteGoodSectionDescription.html', {'goodSectionDescription': goodSectionDescription})


# feedbacks
@login_required(login_url='/admin/login/')
def feedbacks(request):
    dataFeedback = feedback.objects.all()
    return render(request, 'artelApp/feedback.html', {'dataFeedback' : dataFeedback},)


# stocks
@login_required(login_url='/admin/login/')
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
@login_required(login_url='/admin/login/')
def updateStocks(request, pk):
    stock = stocks.objects.get(id = pk)
    form = stockForm(instance=stock)
    if request.method == 'POST':
        form = categoryForm(request.POST, request.FILES, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    return render(request, 'artelApp/updateStock.html', {'form': form, 'stock': stock})


# delete button for categorie
@login_required(login_url='/admin/login/')
def deleteStocks(request, pk):
    stock = stocks.objects.get(id = pk)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock')
    return render(request, 'artelApp/deleteStock.html', {'stock': stock})


# reports
@login_required(login_url='/admin/login/')
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


# company
@login_required(login_url='/admin/login/')
def companies(request):
    companies = company.objects.all()
    if request.method == 'POST':
        error = ''
        form = companiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('companies') 
        else:
            error = "Форма было неверной"
            
    form = companiesForm()
            
    dataCompanies = {
        'companies' : companies,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/companies.html', {'dataCompanies' : dataCompanies})


# update button for companies
@login_required(login_url='/admin/login/')
def updateCompanies(request, pk):
    companies = company.objects.get(id = pk)
    form = companiesForm(instance=companies)
    if request.method == 'POST':
        form = companiesForm(request.POST, request.FILES, instance=companies)
        if form.is_valid():
            form.save()
            return redirect('companies')
    return render(request, 'artelApp/updateCompanies.html', {'form': form, 'companies': companies})


# delete button for categorie
@login_required(login_url='/admin/login/')
def deleteCompanies(request, pk):
    companies = company.objects.get(id = pk)
    if request.method == 'POST':
        companies.delete()
        return redirect('companies')
    return render(request, 'artelApp/deleteCompanies.html', {'companies': companies})


# Info
@login_required(login_url='/admin/login/')
def infos(request):
    infos = info.objects.all()
    if request.method == 'POST':
        error = ''
        form = infosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('infos') 
        else:
            error = "Форма было неверной"
            
    form = infosForm()
            
    dataInfos = {
        'infos' : infos,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/infos.html', {'dataInfos' : dataInfos})


# update button for companies
@login_required(login_url='/admin/login/')
def updateInfos(request, pk):
    infos = info.objects.get(id = pk)
    form = infosForm(instance=infos)
    if request.method == 'POST':
        form = infosForm(request.POST, request.FILES, instance=infos)
        if form.is_valid():
            form.save()
            return redirect('infos')
    return render(request, 'artelApp/updateInfos.html', {'form': form, 'infos': infos})


# delete button for categorie
@login_required(login_url='/admin/login/')
def deleteInfos(request, pk):
    infos = info.objects.get(id = pk)
    if request.method == 'POST':
        infos.delete()
        return redirect('companies')
    return render(request, 'artelApp/deleteInfos.html', {'infos': infos})


# partners
@login_required(login_url='/admin/login/')
def partner(request):
    partner = partners.objects.all()
    if request.method == 'POST':
        error = ''
        form = partnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partner') 
        else:
            error = "Форма было неверной"
            
    form = partnerForm()
            
    dataPartner = {
        'partner' : partner,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/partner.html', {'dataPartner' : dataPartner})


# update button for partner
@login_required(login_url='/admin/login/')
def updatePartner(request, pk):
    partner = partners.objects.get(id = pk)
    form = partnerForm(instance=partner)
    if request.method == 'POST':
        form = partnerForm(request.POST, request.FILES, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner')
    return render(request, 'artelApp/updatePartner.html', {'form': form, 'partner': partner})


# delete button for partner
@login_required(login_url='/admin/login/')
def deletePartner(request, pk):
    partner = partners.objects.get(id = pk)
    if request.method == 'POST':
        partner.delete()
        return redirect('partner')
    return render(request, 'artelApp/deletePartner.html', {'partner': partner})


# exports
@login_required(login_url='/admin/login/')
def export(request):
    export = exports.objects.all()
    if request.method == 'POST':
        error = ''
        form = exportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('export') 
        else:
            error = "Форма было неверной"
            
    form = exportForm()
            
    dataExport = {
        'export' : export,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/export.html', {'dataExport' : dataExport})


# update button for export
@login_required(login_url='/admin/login/')
def updateExport(request, pk):
    export = exports.objects.get(id = pk)
    form = exportForm(instance=export)
    if request.method == 'POST':
        form = exportForm(request.POST, request.FILES, instance=export)
        if form.is_valid():
            form.save()
            return redirect('export')
    return render(request, 'artelApp/updateExport.html', {'form': form, 'export': export})


# delete button for export
@login_required(login_url='/admin/login/')
def deleteExport(request, pk):
    export = exports.objects.get(id = pk)
    if request.method == 'POST':
        export.delete()
        return redirect('export')
    return render(request, 'artelApp/deleteExport.html', {'export': export})


# ecology
@login_required(login_url='/admin/login/')
def ecologies(request):
    ecologies = ecology.objects.all()
    if request.method == 'POST':
        error = ''
        form = ecologyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ecologies') 
        else:
            error = "Форма было неверной"
            
    form = ecologyForm()
            
    dataEcology = {
        'ecologies' : ecologies,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/ecologies.html', {'dataEcology' : dataEcology})


# update button for ecology
@login_required(login_url='/admin/login/')
def updateEcology(request, pk):
    ecologies = ecology.objects.get(id = pk)
    form = ecologyForm(instance=ecologies)
    if request.method == 'POST':
        form = ecologyForm(request.POST, request.FILES, instance=ecologies)
        if form.is_valid():
            form.save()
            return redirect('ecologies')
    return render(request, 'artelApp/updateEcology.html', {'form': form, 'ecologies': ecologies})


# delete button for ecology
@login_required(login_url='/admin/login/')
def deleteEcology(request, pk):
    ecologies = ecology.objects.get(id = pk)
    if request.method == 'POST':
        ecologies.delete()
        return redirect('ecologies')
    return render(request, 'artelApp/deleteEcology.html', {'ecologies': ecologies})


# innovations
@login_required(login_url='/admin/login/')
def innovation(request):
    innovation = innovations.objects.all()
    if request.method == 'POST':
        error = ''
        form = innovationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('innovation') 
        else:
            error = "Форма было неверной"
            
    form = innovationForm()
            
    dataInnovation = {
        'innovation' : innovation,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/innovation.html', {'dataInnovation' : dataInnovation})


# update button for innovations
@login_required(login_url='/admin/login/')
def updateInnovation(request, pk):
    innovation = innovations.objects.get(id = pk)
    form = innovationForm(instance=innovation)
    if request.method == 'POST':
        form = innovationForm(request.POST, request.FILES, instance=innovation)
        if form.is_valid():
            form.save()
            return redirect('innovation')
    return render(request, 'artelApp/updateInnovation.html', {'form': form, 'innovation': innovation})


# delete button for innovation
@login_required(login_url='/admin/login/')
def deleteInnovation(request, pk):
    innovation = innovations.objects.get(id = pk)
    if request.method == 'POST':
        innovation.delete()
        return redirect('innovation')
    return render(request, 'artelApp/deleteInnovation.html', {'innovation': innovation})


# productBases
@login_required(login_url='/admin/login/')
def productBases(request):
    productBases = product_bases.objects.all()
    if request.method == 'POST':
        error = ''
        form = productBaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productBases') 
        else:
            error = "Форма было неверной"
            
    form = productBaseForm()
            
    dataProductBases = {
        'productBases' : productBases,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/productBases.html', {'dataProductBases' : dataProductBases})


# update button for productBases
@login_required(login_url='/admin/login/')
def updateProductBases(request, pk):
    productBases = product_bases.objects.get(id = pk)
    form = productBaseForm(instance=productBases)
    if request.method == 'POST':
        form = productBaseForm(request.POST, request.FILES, instance=productBases)
        if form.is_valid():
            form.save()
            return redirect('productBases')
    return render(request, 'artelApp/updateProductBases.html', {'form': form, 'productBases': productBases})


# delete button for productBase
@login_required(login_url='/admin/login/')
def deleteProductBases(request, pk):
    productBase = product_bases.objects.get(id = pk)
    if request.method == 'POST':
        productBase.delete()
        return redirect('productBases')
    return render(request, 'artelApp/deleteProductBases.html', {'productBase': productBase})


# services
@login_required(login_url='/admin/login/')
def service(request):
    service = services.objects.all()
    if request.method == 'POST':
        error = ''
        form = serviceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service') 
        else:
            error = "Форма было неверной"
            
    form = serviceForm()
            
    dataService = {
        'service' : service,
        'form': form,
        # 'error': error,
    }
    return render(request, 'artelApp/service.html', {'dataService' : dataService})


# update button for service
@login_required(login_url='/admin/login/')
def updateService(request, pk):
    service = services.objects.get(id = pk)
    form = serviceForm(instance=service)
    if request.method == 'POST':
        form = serviceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service')
    return render(request, 'artelApp/updateService.html', {'form': form, 'service': service})


# delete button for service
@login_required(login_url='/admin/login/')
def deleteService(request, pk):
    service = services.objects.get(id = pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service')
    return render(request, 'artelApp/deleteService.html', {'service': service})




class languageAPIView(ModelViewSet):
    queryset = languages.objects.all()
    serializer_class = languageSerializer


class categorieAPIView(ModelViewSet):
    queryset = categories.objects.all()
    serializer_class = categorySerializer


class goodAPIView(ModelViewSet):
    queryset = goods.objects.all()
    serializer_class = goodSerializer

class goodImageAPIView(ModelViewSet):
    queryset = good_images.objects.all()
    serializer_class = goodImageSerializer


class companiesAPIView(ModelViewSet):
    queryset = company.objects.all()
    serializer_class = companySerializer


class partnersAPIView(ModelViewSet):
    queryset = partners.objects.all()
    serializer_class = partnerSerializer

class exportsAPIView(ModelViewSet):
    queryset = exports.objects.all()
    serializer_class = exportSerializer

class ecologiesAPIView(ModelViewSet):
    queryset = ecology.objects.all()
    serializer_class = ecologySerializer

class innovationsAPIView(ModelViewSet):
    queryset = innovations.objects.all()
    serializer_class = innovationSerializer


class feedbacksAPIView(ModelViewSet):
    queryset = feedback.objects.all()
    serializer_class = feedbackSerializer
    # permission_classes = (IsAuthenticated)


class productBasesAPIView(ModelViewSet):
    queryset = product_bases.objects.all()
    serializer_class = productBaseSerializer


class servicesAPIView(ModelViewSet):
    queryset = services.objects.all()
    serializer_class = serviceSerializer


class reportOfLanguageAPIView(ModelViewSet):
    queryset = reportsOfLanguage.objects.all()
    serializer_class = reportOfLanguageSerializer
    
    
class reportOfCategoryAPIView(ModelViewSet):
    queryset = reportsOfCategory.objects.all()
    serializer_class = reportsOfCategorySerializer
    # permission_classes = (IsAuthenticated)


class reportOfGoodAPIView(ModelViewSet):
    queryset = reportsOfGood.objects.all()
    serializer_class = reportsOfGoodSerializer


class stocksAPIView(ModelViewSet):
    queryset = stocks.objects.all()
    serializer_class = stockSerializer


class userAPIView(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = userSerializer
    # permission_classes = (IsAuthenticated)
    