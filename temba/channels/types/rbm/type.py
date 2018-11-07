import logging

from django.utils.translation import ugettext_lazy as _

from temba.contacts.models import RBM_SCHEME

from ...models import ChannelType
from .views import ClaimView


logger = logging.getLogger(__name__)


class RBMType(ChannelType):
    """
    A RBM channel
    """

    code = "RBM"
    category = ChannelType.Category.SOCIAL_MEDIA

    courier_url = r"^rbm/(?P<uuid>[a-z0-9\-]+)/receive"

    name = "RBM"
    icon = "icon-power-cord"

    claim_blurb = _(
        """Add an <a href="https://jibe.google.com/business-messaging/">RBM</a> bot to send and receive messages. 
        """
    )
    claim_view = ClaimView

    schemes = [RBM_SCHEME]
    max_length = 640
    attachment_support = True
    free_sending = True

    def deactivate(self, channel):
        logger.debug("hoop channel.deactivate(%r)" % (channel,))

    def activate_trigger(self, trigger):
        logger.debug("noop activate_trigger(%r)" % (trigger,))

    def deactivate_trigger(self, trigger):
        logger.debug("noop deactivate_trigger(%r)" % (trigger,))
