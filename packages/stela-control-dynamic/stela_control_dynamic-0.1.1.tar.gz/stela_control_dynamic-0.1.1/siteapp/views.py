from decimal import Decimal
from unittest import result
from urllib import response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
import json
from django.utils.translation import gettext_lazy as _
from paypalcheckoutsdk.orders import OrdersGetRequest
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import stripe
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from accounts.models import UserBase
from django.utils import translation
from linkzone.context_processors import cart
from stela_control.models import Budget, StelaPayments
from linkzone.cart import Cart
from stela_control.models import (
    Content, Order, StelaSelection, 
    StelaItems, ControlFacturacion, FacturaItems, StelaPayments, 
    PathControl, BillingRecipt, TemplateSections,
    DataEmail, DynamicBullets, OrderItems, ItemServices, Modules, Support, 
    ChatSupport, SupportResponse, SitePolicy, Customer, Comments, PetData,
    Inventory, Contact, Booking
    )
from stela_control.models import DataEmail, Content, Team
from stela_control.forms import ContactForm, DataEmailForm, NewsletterForm
from django.core.mail import EmailMultiAlternatives
import datetime 
from django.contrib.sites.shortcuts import get_current_site
from django.utils.html import strip_tags
from django.conf import settings
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django import template

# Create your views here.
register = template.Library()
@register.filter(name='cash', is_safe=False)
def cash(val, precision=2):
    try:
        int_val = int(val)
    except ValueError:
        raise template.TemplateSyntaxError(
        f'Value must be an integer. {val} is not an integer')

    if int_val < 1000:
        return str(int_val)
    elif int_val < 1_000_000:
        return f'{ int_val/1000.0:.{precision}f}'.rstrip('0').rstrip('.') + 'K'
    else:
        return f'{int_val/1_000_000.0:.{precision}f}'.rstrip('0').rstrip('.') + 'M'

def home(request):
    user = request.user
    
    context = {
         'countdown': 'active'
    }

    return render(request, 'siteapp/index.html', context)

@login_required
def product_detail(request, slug):
    comments = Comments.objects.filter(status=True, product__slug=slug).order_by('-created_at')
    user = request.user 
    pets = PetData.objects.filter(owner=user.id)
    service = Inventory.objects.get(slug=slug)
    form = DataEmailForm()
    
    if request.method == 'POST':
            form = DataEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if DataEmail.objects.filter(email=email).exists():
                    form.save(commit=False)
                    return redirect('site:home')
                    
                else:
                    form.save()
                    messages.success(request, "successful subscription, thank you")
                    return HttpResponseRedirect(reverse('siteapp:home'))

    context ={
        'comments': comments,
        'pets':pets,
        'pricing': pricing,
        'service': service,
        'form': form
          }
    
    return render(request, 'siteapp/sections/costumer/product_detail.html', context)

def gallery(request):
    # galleries = Gallery.objects.filter(status="Published")
    form = DataEmailForm()
    
    if request.method == 'POST':
            form = DataEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if DataEmail.objects.filter(email=email).exists():
                    form.save(commit=False)
                    return redirect('siteapp:home')
                    
                else:
                    form.save()
                    messages.success(request, "successful subscription, thank you")
                    return HttpResponseRedirect(reverse('siteapp:home'))

    context ={
        # 'galleries': galleries,
        'form': form,
    }
    return render(request, 'siteapp/sections/media/gallery.html', context)

def userGallery(request, id):
    # galleries = Gallery.objects.filter(status="Published")
    # get_gallery = Gallery.objects.get(id=id)
    # collage = ImageGallery.objects.filter(parent_id=id)
    form = DataEmailForm()
    
    if request.method == 'POST':
            form = DataEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if DataEmail.objects.filter(email=email).exists():
                    form.save(commit=False)
                    return redirect('siteapp:home')
                    
                else:
                    form.save()
                    messages.success(request, "successful subscription, thank you")
                    return HttpResponseRedirect(reverse('siteapp:home'))
    context ={
        # 'galleries': galleries,
        # 'get_gallery': collage,
        'form': form
    }
    return render(request, 'siteapp/sections/gallery.html', context)

def blog_detail(request, slug):
    user = request.user
    user_id = user.id
    admin = UserBase.objects.get(id=user_id, is_staff=True)
    # blog = News.objects.get(status='Publish', slug=slug)
    # commentform = CommentForm()
    # comments = Comments.objects.filter(post_id=blog.id, status='Published')
    form = DataEmailForm()
    
    if request.method == 'POST':
            form = DataEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if DataEmail.objects.filter(email=email).exists():
                    form.save(commit=False)
                    return redirect('siteapp:home')
                    
                else:
                    form.save()
                    messages.success(request, "successful subscription, thank you")
                    return HttpResponseRedirect(reverse('siteapp:home'))
    

    context = {
      'admin': admin,
    #   'blog': blog,
    #   'commentsform': commentform,
    #   'comments': comments,
      'form': form
    }
    if request.method == 'POST':  
        # form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
        #    comment.post = blog
           comment.save()

           messages.success(request, "Your review was send in minutes will be published")
        #    return HttpResponseRedirect(reverse('siteapp:blog_detail', args=[blog.slug]))

    return render(request, 'siteapp/sections/media/single-blog.html', context)

def pricing(request):
    lang=request.LANGUAGE_CODE
    owner = request.user.is_superuser
    services = Inventory.objects.filter(owner=owner, status="Active", lang=lang)
    context = {
      'services': services
    }
    
    return render(request, 'siteapp/sections/costumer/pricing.html', context)

def new_message(request):
    form = ContactForm()
    newsletter = DataEmailForm()
    context = {
      'form': form,
      'newsletter':newsletter
    }
    
    if request.method == 'POST':
       form = ContactForm(request.POST)
       if form.is_valid():
          form.save()
          user_email = form.cleaned_data['email']
          subject = form.cleaned_data['subject']
          full_name = form.cleaned_data['name']
          current_site = get_current_site(request)
          html_content = render_to_string('emails/transactionals/message_recieve.html', {
                            'name': full_name,
                            'domain': current_site.domain,
                            })
          text_content = strip_tags(html_content)

          email = EmailMultiAlternatives(
               'We have received your message',
               text_content,
               settings.DEFAULT_EMAIL,
               [user_email]
           
           )
          email.attach_alternative(html_content, "text/html")
          email.send()
          
          user = request.user
          html_content = render_to_string('stela_control/emails-template/message_notification.html', {
                            'name': full_name,
                            'email': user_email,
                            'subject': subject,
                            'created': datetime.datetime.now()
                            })
          text_content = strip_tags(html_content)

          email = EmailMultiAlternatives(
               'They have sent you a message',
               text_content,
               settings.STELA_EMAIL,
               [settings.DEFAULT_EMAIL]
           
           )
          email.attach_alternative(html_content, "text/html")
          email.send()

          if Contact.objects.filter(email=user_email,newsletter=True):

             if DataEmail.objects.filter(email=user_email).exists():
                pass
             else:
                DataEmail.objects.create (
                         email=user_email,
                )

          messages.success(request, "Your message has been sent")
          return HttpResponseRedirect(reverse('siteapp:contact'))

    return render(request, 'siteapp/sections/media/contact.html', context)

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        price = str(request.POST.get('price'))
        serviceid = str(request.POST.get('service'))
        catalog=Inventory.objects.get(pk=serviceid)
        selection = StelaSelection.objects.filter(
            integration=catalog,
            status="Pending"
            )

        if selection.exists():
            selection.delete()
            
        get_select=StelaSelection.objects.create(
            integration=catalog,
            amount=price
            )
        cart.service_add(selectid=get_select.pk)
        cart_count = cart.__len__()
        response = JsonResponse({'count':cart_count})
        return response

def reorder(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        orderid = str(request.POST.get('orderid'))
        orderitems = OrderItems.objects.filter(order_id=orderid)
        for order in orderitems:
            select = StelaSelection.objects.get(
                pk=order.stela_selection.pk, 
                status="Payeed"
            )
            cart.service_add(selectid=select.id)

        cart_count = cart.__len__()
        response = JsonResponse({'count':cart_count})
        return response

# def extra_add(request):
#     user = request.user

#     if request.POST.get('action') == 'post':
#         extraid = str(request.POST.get('extraid'))
#         pet_id = str(request.POST.get('petid'))
#         price = str(request.POST.get('price'))
#         service = str(request.POST.get('service'))

#         if UserSelection.objects.filter(user_id=user.id, service_id=service, pet_id=pet_id, price_id=price, status='Pending').exists():
#             parent = UserSelection.objects.get(user_id=user.id, service_id=service, pet_id=pet_id, price_id=price, status='Pending')
            
#             if ExtraSelection.objects.filter(service_id=extraid, parent_id=parent.id).exists():
#                 response = JsonResponse({'success': 'return something'})
#                 return response

#             ExtraSelection.objects.create(service_id=extraid, parent_id=parent.id)
#             response = JsonResponse({'success': 'return something'})
#             return response
#         else:
#             response = JsonResponse({'error': 'Please select a service'})
#             return response
     
def query(request):
    form = DataEmailForm()
    if request.method == 'POST':
            form = DataEmailForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                if DataEmail.objects.filter(email=email).exists():
                    form.save(commit=False)
                    return redirect('site:home')
                    
                else:
                    form.save()
                    messages.success(request, "successful subscription, thank you")
                    return HttpResponseRedirect(reverse('siteapp:home'))

    if request.POST.get('answer') == 'registered user':
       response = JsonResponse({'member': 'Return Something'})
       return response

    if request.POST.get('answer') == 'new user':
       response = JsonResponse({'newcomer': 'Return Something'})
       return response
        
    return render(request, 'siteapp/sections/costumer/site-query.html', {'form':form})

def checkout(request):
    
    return render(request, 'siteapp/sections/checkout/cart.html')

def getDate(request):
    cart = Cart(request)
    user=request.user
    if request.POST.get('action') == 'post':
        date = (request.POST.get('date'))
        get_date = Booking.objects.filter(user_id=user.id, date=date, dateConfirm=False)
        
        if get_date.exists():
            get_date.delete()

        if not date:
            response = JsonResponse({'empty': 'Please select a date.'})
            return response

        dateConfirmed = Booking.objects.filter(date=date, dateConfirm=True).count()

        if dateConfirmed == 10:
            response = JsonResponse({'booked': 'Dates booked, please select another one.'})
            return response
        else:
            Booking.objects.create(
                date=date,
                user=user
            )
            cart.date_add(userid=user.id)
            response = JsonResponse({'success': 'The selected date is available.'})
            return response

def changeDate(request):
    
    if request.POST.get('action') == 'post':
        order_id = (request.POST.get('orderid'))
        date = (request.POST.get('date'))
        print(order_id)
        order = Order.objects.filter(id=order_id)
        if not date:
            response = JsonResponse({'empty': 'Please select a date.'})
            return response

        dateConfirmed = Booking.objects.filter(date=date, dateConfirm=True).count()

        if dateConfirmed == 10:
            response = JsonResponse({'booked': 'Dates booked, please select another one.'})
            return response
        else:
            order.update(appointment_date=date)
            response = JsonResponse({'success': 'The selected date is available.'})
            return response

def order_placed(request):
    user = request.user
    order = Order.objects.filter(user_id=user.id).latest('id')
    context = {
        'order': order
    }
    return render(request, 'siteapp/sections/checkout/order_placed.html', context)

def aboutUs(request):
    policies = SitePolicy.objects.filter(status="Publish", policy="About us")
    context = {
        'policies': policies
    }
    return render(request, 'siteapp/sections/docs/about.html', context)

def terms(request):
    policies = SitePolicy.objects.filter(status="Publish")
    context = {
        'policies': policies
    }
    return render(request, 'siteapp/sections/docs/terms.html', context)


def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if DataEmail.objects.filter(email=email).exists():
                response = JsonResponse({'success': 'Este email esta registrado.'})         
            else:
                form.save()
                response = JsonResponse({'success': 'Registro exitoso, gracias.'})
        else:
            print(form.errors)
            response = JsonResponse({'alert': 'Proceso fallido, por favor, ingrese un correo electrónico válido.'})
    return response
