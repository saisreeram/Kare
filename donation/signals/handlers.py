from paypal.standard.ipn.signals import valid_ipn_received, invalid_ipn_received
from django.dispatch import receiver


def show_me_the_money(sender, **kwargs):
    print(sender)
    print("may be")

                #pk = ipn_obj.invoice
                #dsr = DatasetRequest.objects.get(pk=pk)
                #dsr.is_paid = True
                #dsr.save()
def do_not_show_me_the_money(sender, **kwargs):
    print("may be not")


valid_ipn_received.connect(show_me_the_money)