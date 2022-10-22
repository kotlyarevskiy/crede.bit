from django.shortcuts import render
from django.utils.translation import gettext_lazy as _



def index(request):

    return render(request, 'index.html', {'title': _('Main page'), 
                                         'content_title': _('Main page'),
                                         'active': '', 
                                         })
    
def about(request):
    return render(request, "about.html", {'title': _('About'), 
                                         'content_title': _('About'),
                                         'active': 'about', 
                                         })

def contacts(request):
    return render(request, "contacts.html", {'title': _('Contacts'), 
                                         'content_title': _('Contacts'),
                                         'active': 'contacts', 
                                         })
    
