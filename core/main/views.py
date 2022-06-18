from django.shortcuts import render
from django.views.generic import ListView, DeleteView 
from .models import Homepage, HomePagePictures, HomePageCategory1, HomePageCategory2, HomePageCategory3, HomePageCategory4, HomePageCategory5, Category, Shoose
# Create your views here.


class HomepageListView(ListView): 
    template_name = 'index.html' 
 
    def get(self, request): 
        homes = Homepage.objects.all() 
        homes_pic = HomePagePictures.objects.all()
        t_shirt = HomePageCategory1.objects.all()
        blazers = HomePageCategory2.objects.all()
        sunglass = HomePageCategory3.objects.all()
        kids = HomePageCategory4.objects.all()
        polo_shirt = HomePageCategory5.objects.all()
        cats = Category.objects.all()
        return render(request, self.template_name, {
            'homes':homes,
            'homes_pic':homes_pic,
            't_shirt':t_shirt,
            'blazers':blazers,
            'sunglass':sunglass,
            'kids':kids,
            'polo_shirt':polo_shirt,
            'cats':cats,





            })




def contact(request):
    return render(request, 'contact-us.html')
