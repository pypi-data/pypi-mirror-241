from eveuniverse.models.universe_2 import EveSolarSystem

from django import forms

from drifters.app_settings import DRIFTERS_JOVE_OBSERVATORIES

from .models import Wormhole


class WormholeForm(forms.ModelForm):
    class Meta:
        model = Wormhole
        fields = ["system", "complex", "mass", "lifetime", "bookmarked_k", "bookmarked_w"]

    def __init__(self, user=None, **kwargs):
        self.region = kwargs.pop('region', None)
        self.system = kwargs.pop('system', None)
        super().__init__(**kwargs)
        if self.region:
            self.fields['system'].queryset = EveSolarSystem.objects.filter(name__in=DRIFTERS_JOVE_OBSERVATORIES, eve_constellation__eve_region=self.region)
        elif self.system:
            self.fields['system'].queryset = EveSolarSystem.objects.filter(id=self.system.id)
        else:
            self.fields['system'].queryset = EveSolarSystem.objects.filter(name__in=DRIFTERS_JOVE_OBSERVATORIES)
