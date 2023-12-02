from django.contrib import admin

from .models import Bank, BankAccountTransaction, BankAccountTransfer, CompanyBankAccount, CompanyEWalletAccount, CompanyExchangerBrokerAccount, Currency, CustomerBankAccount, CustomerEWalletAccount, CustomerExchangerBrokerAccount, EWallet, EWalletAccountTransaction, EWalletAccountTransfer, ExchangeCurrency, ExchangerBroker, ExchangerBrokerAccountTransaction, ExchangerBrokerAccountTransfer
# Register your models here.



admin.site.register(Currency)
admin.site.register(ExchangeCurrency)
admin.site.register(Bank)
admin.site.register(CompanyBankAccount)
admin.site.register(CustomerBankAccount)
admin.site.register(EWallet)
admin.site.register(CompanyEWalletAccount)

admin.site.register(CustomerEWalletAccount)
admin.site.register(ExchangerBroker)
admin.site.register(CompanyExchangerBrokerAccount)
admin.site.register(CustomerExchangerBrokerAccount)
admin.site.register(BankAccountTransaction)
admin.site.register(BankAccountTransfer)
admin.site.register(EWalletAccountTransaction)
admin.site.register(EWalletAccountTransfer)
admin.site.register(ExchangerBrokerAccountTransaction)
admin.site.register(ExchangerBrokerAccountTransfer)