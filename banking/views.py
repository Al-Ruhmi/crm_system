from django.shortcuts import render
from .models import Bank, BankAccountTransaction, BankAccountTransfer, CompanyBankAccount, CompanyEWalletAccount, CompanyExchangerBrokerAccount, Currency, CustomerBankAccount, CustomerEWalletAccount, CustomerExchangerBrokerAccount, EWallet, EWalletAccountTransaction, EWalletAccountTransfer, ExchangeCurrency, ExchangerBroker, ExchangerBrokerAccountTransaction, ExchangerBrokerAccountTransfer
 #  BankAccount  , EWalletAccount  , ExchangerBrokerAccount
from rest_framework import viewsets 
from . import serializer

# Create your views here.

# ------------------------- Filters Manager API
# 1
class CurrencyFilterViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.filter_by_name('f')
    serializer_class = serializer.CurrencySerializer

# 2
class BankFilterViewset(viewsets.ModelViewSet):
    queryset = Bank.objects.filter_by_name('f')
    serializer_class = serializer.BankSerializer

# 3
class EWalletFilterViewset(viewsets.ModelViewSet):
    queryset = EWallet.objects.filter_by_name('f')
    serializer_class = serializer.EWalletSerializer

# 4
class ExchangerBroker(viewsets.ModelViewSet):
    queryset = ExchangerBroker.objects.filter_by_name('f')
    serializer_class = serializer.ExchangerBrokerSerializer

# ------------------------- Models Views API
# 1
class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = serializer.CurrencySerializer

# 2
class ExchangeCurrencyViewset(viewsets.ModelViewSet):
    queryset = ExchangeCurrency.objects.all()
    serializer_class = serializer.ExchangeCurrencySerializer

# 3
class BankViewset(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = serializer.BankSerializer


# 4
# class BankAccountViewset(viewsets.ModelViewSet):
#     queryset = BankAccount.objects.all()
#     serializer_class = serializer.BankAccountSerializer

# 5
class CompanyBankAccountViewset(viewsets.ModelViewSet):
    queryset = CompanyBankAccount.objects.all()
    serializer_class = serializer.CompanyBankAccountSerializer

# 6
class CustomerBankAccountViewset(viewsets.ModelViewSet):
    queryset = CustomerBankAccount.objects.all()
    serializer_class = serializer.CustomerBankAccountSerializer

# 7
class EWalletViewset(viewsets.ModelViewSet):
    queryset = EWallet.objects.all()
    serializer_class = serializer.EWalletSerializer

# 8
# class EWalletAccountViewset(viewsets.ModelViewSet):
#     queryset = EWalletAccount.objects.all()
#     serializer_class = serializer.EWalletAccountSerializer


# 9
class CompanyEWalletAccountViewset(viewsets.ModelViewSet):
    queryset = CompanyEWalletAccount.objects.all()
    serializer_class = serializer.CompanyEWalletAccountSerializer

# 10
class CustomerEWalletAccountViewset(viewsets.ModelViewSet):
    queryset = CustomerEWalletAccount.objects.all()
    serializer_class = serializer.CustomerEWalletAccountSerializer


# 11
# class ExchangerBrokerViewset(viewsets.ModelViewSet):
#     queryset = ExchangerBroker.objects.all()
#     serializer_class = serializer.ExchangerBrokerSerializer

# 12
# class ExchangerBrokerAccountViewset(viewsets.ModelViewSet):
#     queryset = ExchangerBrokerAccount.objects.all()
#     serializer_class = serializer.ExchangerBrokerAccountSerializer

# 13
class CompanyExchangerBrokerAccountViewset(viewsets.ModelViewSet):
    queryset = CompanyExchangerBrokerAccount.objects.all()
    serializer_class = serializer.CompanyExchangerBrokerAccountSerializer


# 14
class CustomerExchangerBrokerAccountViewset(viewsets.ModelViewSet):
    queryset = CustomerExchangerBrokerAccount.objects.all()
    serializer_class = serializer.CustomerExchangerBrokerAccountSerializer

# 15
class BankAccountTransactionViewset(viewsets.ModelViewSet):
    queryset = BankAccountTransaction.objects.all()
    serializer_class = serializer.BankAccountTransactionSerializer

# 16
class BankAccountTransferViewset(viewsets.ModelViewSet):
    queryset = BankAccountTransfer.objects.all()
    serializer_class = serializer.BankAccountTransferSerializer

# 17
class EWalletAccountTransactionViewset(viewsets.ModelViewSet):
    queryset = EWalletAccountTransaction.objects.all()
    serializer_class = serializer.EWalletAccountTransactionSerializer

# 18
class EWalletAccountTransferViewset(viewsets.ModelViewSet):
    queryset = EWalletAccountTransfer.objects.all()
    serializer_class = serializer.EWalletAccountTransferSerializer


# 19
class ExchangerBrokerAccountTransactionViewset(viewsets.ModelViewSet):
    queryset = ExchangerBrokerAccountTransaction.objects.all()
    serializer_class = serializer.ExchangerBrokerAccountTransactionSerializer

# 20
class ExchangerBrokerAccountTransferViewset(viewsets.ModelViewSet):
    queryset = ExchangerBrokerAccountTransfer.objects.all()
    serializer_class = serializer.ExchangerBrokerAccountTransferSerializer