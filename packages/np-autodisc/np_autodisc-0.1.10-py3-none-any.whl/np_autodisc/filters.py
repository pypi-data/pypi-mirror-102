# filters.py

import django_filters
import netaddr
from django.db.models import Q

from dcim.models import DeviceRole, Platform, Site

from np_autodisc.constants import REQUEST_STATUS_CHOICES
from np_autodisc.models import DiscoveryRequest


