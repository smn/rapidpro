from smartmin.views import SmartFormView

from django import forms
from django.utils.translation import ugettext_lazy as _

from ...models import Channel
from ...views import ClaimViewMixin


class ClaimView(ClaimViewMixin, SmartFormView):
    class Form(ClaimViewMixin.Form):
        name = forms.CharField(
            required=True, help_text=_("The name of the RBM Channel")
        )
        address = forms.CharField(required=True, help_text="The RBM Address")
        auth_token = forms.CharField(
            required=True,
            help_text=_("The authentication token"),
            widget=forms.Textarea,
        )
        send_url = forms.CharField(
            min_length=32,
            required=True,
            help_text=_("The URL to hit with RBM API calls"),
        )

    form_class = Form

    def form_valid(self, form):
        org = self.request.user.get_org()
        name = form.cleaned_data["name"]
        address = form.cleaned_data["address"]
        auth_token = form.cleaned_data["auth_token"]
        send_url = form.cleaned_data["send_url"]

        config = {
            Channel.CONFIG_SEND_URL: send_url,
            Channel.CONFIG_AUTH_TOKEN: auth_token,
        }
        self.object = Channel.create(
            org,
            self.request.user,
            None,
            self.channel_type,
            name=name,
            address=address,
            config=config,
        )

        return super().form_valid(form)
