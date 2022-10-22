from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    """
        This class represents an user profile data. \n
        Attributes:
        -----------
        param user: owner of profile - user rel.
        param email: email field.

    """

    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    email = models.EmailField(verbose_name=_('email'), null=True)
    
    def __str__(self): 
        return self.user.username  
      
    
    class Meta:
        verbose_name = verbose_name=_("User profile")
        verbose_name_plural = verbose_name=_("User profile data")
        
class UserSettings(models.Model):
    """
        This class represents an user settings. \n
        Attributes:
        -----------
        param user: owner of settings - user rel.
        param some_parameter: str contains some parameter.

    """

    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    some_parameter = models.CharField(max_length=5, null=True)
    
    def __str__(self): 
        return self.user.username  
    
    class Meta:
        verbose_name = verbose_name=_("User settings")
        verbose_name_plural = verbose_name=_("User settings")
        
        