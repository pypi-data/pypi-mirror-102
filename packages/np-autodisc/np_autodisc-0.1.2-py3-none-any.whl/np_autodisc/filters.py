# filters.py

import django_filters
import netaddr
from django.db.models import Q

from dcim.models import DeviceRole, Platform, Site

from np_autodiscovery.constants import REQUEST_STATUS_CHOICES
from np_autodiscovery.models import DiscoveryRequest


