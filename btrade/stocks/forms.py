from django import forms
from django.contrib.auth.models import User
from stocks.models import BuyReceipt, SellReceipt

class BuyStockForm(forms.ModelForm):
    # TODO: Add a dynamic total field = price_bought_at * stocks price
    class Meta:
        model = BuyReceipt
        fields = (
            'owner',
            'units',
            'price_bought_at',
            'coin_type',
            )

        exclude = ('owner', 'coin_type', 'price_bought_at')

    def save(self, commit=True):
        buy_receipt = super(BuyStockForm, self).save(commit=False)
        buy_receipt.units = self.cleaned_data['units']

        if commit:
            buy_receipt.save()

        return buy_receipt

class SellStockForm(forms.ModelForm):
    # TODO: Prepopulate and hide owner field.
    # TODO: Add total field that is equal to price_bought_at * stocks price
    # TODO: Pass stock object to form through foreign key?
    class Meta:
        model = SellReceipt
        fields = (
            'owner',
            'units',
            'price_sold_at',
            'coin_type',
            )

        exclude = ('owner', 'coin_type', 'price_sold_at')

    def save(self, commit=True):
        sell_receipt = super(SellStockForm, self).save(commit=False)
        sell_receipt.units = self.cleaned_data['units']

        if commit:
            sell_receipt.save()

        return sell_receipt
