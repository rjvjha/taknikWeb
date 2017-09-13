import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rkgyanamproject.settings')

import django
django.setup()

from taknik.models import Category, Page


def populate():
    
    aadhaar_cat = add_cat('Aadhaar', views=0, likes=0)

    add_page(cat=aadhaar_cat,
        title="e-Aadhaar by Unique Identification Authority of India",
        url="https://eaadhaar.uidai.gov.in")

    add_page(cat=aadhaar_cat,
        title="Check Aadhaar Status - Resident Portal",
        url="https://resident.uidai.net.in/check-aadhaar-status")

    add_page(cat=aadhaar_cat,
        title="Get Aadhaar - Resident Portal",
        url="https://resident.uidai.net.in/get-aadhaar")
    add_page(cat=aadhaar_cat,
        title="Update Data - Resident Portal",
        url="https://resident.uidai.net.in/update-data")

    ehospital_cat = add_cat("E-hospital", views=0, likes=0)

    add_page(cat=ehospital_cat,
        title="ORS Patient Portal",
        url="orf.gov.in/")

    add_page(cat=ehospital_cat,
        title="Appointment",
        url="https://ors.gov.in/copp/appointment.jsp")

    add_page(cat=ehospital_cat,
        title="AIIMS PATIENT PORTAL @NIC",
        url="https://14.139.245.36/esp/")

    digilocker_cat = add_cat("DigiLocker", views=0, likes=0)
 
    add_page(cat=digilocker_cat,
        title="DigiLocker",
        url="https://digitallocker.gov.in/")

    add_page(cat=digilocker_cat,
        title="Register for a DigiLocker",
        url="https://digitallocker.gov.in/Register.aspx")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save() 
    return p

def add_cat(name,views=0, likes=0):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting taknik population script..."
    populate()
