from banking.views import BankAccountTransactionViewset, BankAccountTransferViewset, BankFilterViewset, BankViewset, CompanyBankAccountViewset, CompanyEWalletAccountViewset, CompanyExchangerBrokerAccountViewset, CurrencyFilterViewset, CurrencyViewset, CustomerBankAccountViewset, CustomerEWalletAccountViewset, CustomerExchangerBrokerAccountViewset, EWalletAccountTransactionViewset, EWalletAccountTransferViewset, EWalletFilterViewset, EWalletViewset, ExchangeCurrencyViewset, ExchangerBrokerAccountTransactionViewset, ExchangerBrokerAccountTransferViewset
from rest_framework import routers
 #  BankAccountViewset  , CustomerEWalletAccountFilterViewset  , EWalletAccountViewset  ,  ExchangerBrokerAccountViewset, ExchangerBrokerViewset

router_banking = routers.DefaultRouter()
# --------------- # ------------------------- Filters Views API Routers
# 1
router_banking.register('currencyfilter', CurrencyFilterViewset)
# 2
router_banking.register('bankfilter', BankFilterViewset)
# 3
router_banking.register('ewalletfilter', EWalletFilterViewset)
# 4
# router_banking.register('customewalletaccountfilter', CustomerEWalletAccountFilterViewset)

# --------------- # ------------------------- Models Views API Routers

# 1
router_banking.register('currency', CurrencyViewset)
# 2
router_banking.register('exchangecurrency', ExchangeCurrencyViewset)
# 3
router_banking.register('bank', BankViewset)
# 4
# router_banking.register('bankaccount', BankAccountViewset)
# 5
router_banking.register('companybankaccount', CompanyBankAccountViewset)
# 6
router_banking.register('customerbankaccount', CustomerBankAccountViewset)
# 7
router_banking.register('ewallet', EWalletViewset)
# 8
# router_banking.register('ewalletaccount', EWalletAccountViewset)
# 9
router_banking.register('companyewalletaccount', CompanyEWalletAccountViewset)
# 10
router_banking.register('customerewalletaccount', CustomerEWalletAccountViewset)
# 11
# router_banking.register('exchangebroker', ExchangerBrokerViewset)
# 12
# router_banking.register('exchangebrokeraccount', ExchangerBrokerAccountViewset)
# 13
router_banking.register('companyexchangebrokeraccount', CompanyExchangerBrokerAccountViewset)
# 14
router_banking.register('customerexchangebrokeraccount', CustomerExchangerBrokerAccountViewset)
# 15
router_banking.register('bankaccounttransaction', BankAccountTransactionViewset)
# 16
router_banking.register('bankaccounttransfer', BankAccountTransferViewset)
# 17
router_banking.register('ewalletaccounttransaction', EWalletAccountTransactionViewset)
# 18
router_banking.register('ewalletaccounttranfer', EWalletAccountTransferViewset)
# 19
router_banking.register('exchangebrokeraccounttransaction', ExchangerBrokerAccountTransactionViewset)
# 20
router_banking.register('exchangebrokeraccounttransfer', ExchangerBrokerAccountTransferViewset)