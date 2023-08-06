from django.db import models
from django.urls import reverse
from django_rq import get_queue
from rq import cancel_job

from dcim.models import Device, DeviceRole, Platform, Site
from ipam.fields import IPAddressField, IPNetworkField
from np_autodiscovery.np_transitions.models import ChangeLoggedModel

from np_autodiscovery.constants import *

class DiscoveryRequest(ChangeLoggedModel):
    pass

