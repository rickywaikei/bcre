from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from listings.models import Listing

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing_title = request.POST['listing_title']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']
        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_connected:
                messages.error(request,"You already have been made an inquiry for this listing.")
                return redirect("/listings/"+listing_id)
        listing_obj = get_object_or_404(Listing,pk=listing_id)
        contact = Contact(
                        listing=listing_title,
                        listing_id=listing_obj,
                        name=name,
                        email=email,
                        phone=phone,
                        message=message,
                        user_id=user_id
                        )
        contact.save()
        # send_mail(
        #     "Listing Inquiry",
        #     "Inquiry for "+listing_title+". Sign into admin for more info",
        #     "admin@bcre.com",
        #     [realtor_email,"master@bcre.com"],
        #     fail_silently=False
        # )
        messages.success(request,"Your request submitted, realtor will get back to you soon.")
    return redirect("/listings/"+listing_id)
    