from django.db import models
from commons.utility import upload_image_path
from core.models import BaseModel, BaseModelWithAuthor
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from crm.models import ClientActivity, Customer

from hr.models import Employee

# Create your models here.

User = get_user_model()

# 1
class Currency(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    curr_code = models.CharField(max_length=255, null=True, blank=True)
    curr_symbol = models.CharField(max_length=255, null=True, blank=True)
    curr_type = models.CharField(max_length=255, null=True, blank=True)
    cent_name = models.CharField(max_length=255, null=True , blank=True)
    cent_name_en = models.CharField(max_length=255, null=True, blank=True)
    local = models.BooleanField(default=False)
    note = models.TextField(null=True,blank=True)
    active = models.BooleanField(default=True)

# 2
class ExchangeCurrency(BaseModelWithAuthor):
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    from_currency = models.ForeignKey(Currency, related_name='%(class)s_fromcurrency', null=True, blank=True, on_delete=models.CASCADE)
    to_currency = models.ForeignKey(Currency, related_name='%(class)s_tocurrency', null=True, blank=True, on_delete=models.CASCADE)
    rate = models.DecimalField(decimal_places=3, max_digits=8)

# 3
class Bank(BaseModel):
    class BankType(models.TextChoices):
        
        CASH = 'CA', _('Cash')
        BANK = 'BA', _('Bank')

    name = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    bank_type = models.CharField(max_length=255, choices=BankType.choices)
    info = models.TextField(null=True,blank=True)
    phones = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    website = models.CharField(max_length=255, null=True ,blank=True)
    logo = models.ImageField(upload_to=upload_image_path,null=True, blank=True)

# 4


class BankAccount(BaseModel):
    bank = models.ForeignKey(Bank, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True , blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    owner_phone_number = models.CharField(max_length=255, null=True, blank=True)
    owner_email = models.EmailField(max_length=255,null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=3, max_digits=11)

    class Meta:
       abstract = True

# 5
class CompanyBankAccount(BankAccount):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)

# 6
class CustomerBankAccount(BankAccount):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

# 7
class EWallet(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True,blank=True)
    contacts = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True ,blank=True)
    logo = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    active = models.BooleanField(default=True)

# 8
class EWalletAccount(BaseModel):
    ewallet = models.ForeignKey(EWallet, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True , blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=3, max_digits=11)

    class Meta:
       abstract = True

# 9
class CompanyEWalletAccount(EWalletAccount):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    passsword = models.CharField(max_length=255, null=True, blank=True)

# 10
class CustomerEWalletAccount(EWalletAccount):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

# 11
class ExchangerBroker(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    info = models.TextField(null=True,blank=True)
    contacts = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True ,blank=True)
    logo = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    active = models.BooleanField(default=True)

#12
class ExchangerBrokerAccount(BaseModel):
    broker = models.ForeignKey(ExchangerBroker, null=True, blank=True, on_delete=models.CASCADE)
    number = models.IntegerField(null=True , blank=True)
    email = models.EmailField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=3, max_digits=11)


    class Meta:
       abstract = True

# 13
class CompanyExchangerBrokerAccount(ExchangerBrokerAccount):
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    passsword = models.CharField(max_length=255, null=True, blank=True)

# 14
class CustomerExchangerBrokerAccount(ExchangerBrokerAccount):
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)

# 15
class BankAccountTransaction(BaseModelWithAuthor):
    class TransactionType(models.TextChoices):
        
        DEPOSIT = 'DP', _('Deposit')
        WITHDRAWAL = 'WI', _('Withdrawal')
        
    transaction_date = models.DateTimeField(null=True,blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    transaction_number = models.IntegerField(null=True , blank=True)
    transaction_type = models.CharField(max_length=255, choices=TransactionType.choices)
    customer_bank_account = models.ForeignKey(CustomerBankAccount, null=True, blank=True, on_delete=models.CASCADE)
    company_bank_account = models.ForeignKey(CompanyBankAccount, null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision_transfer = models.DecimalField(decimal_places=3, max_digits=8)
    commision_client = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    ref_activity = models.ForeignKey(ClientActivity, null=True, blank=True, on_delete=models.CASCADE)

# 16
class BankAccountTransfer(BaseModelWithAuthor):
    transaction_date = models.DateTimeField(null=True,blank=True)
    transaction_number = models.IntegerField(null=True , blank=True)
    from_bank_account = models.ForeignKey(CompanyBankAccount, related_name='%(class)s_frombankaccount', null=True, blank=True, on_delete=models.CASCADE)
    to_bank_account = models.ForeignKey(CompanyBankAccount, related_name='%(class)s_tobankaccount', null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision_transfer = models.DecimalField(decimal_places=3, max_digits=8)
    commision_client = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)

# 17
class EWalletAccountTransaction(BaseModelWithAuthor):
    class TransactionType(models.TextChoices):
        
        DEPOSIT = 'DP', _('Deposit')
        WITHDRAWAL = 'WI', _('Withdrawal')
        
    name = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True,blank=True)
    transaction_number = models.IntegerField(null=True , blank=True)
    transaction_type = models.CharField(max_length=255, choices=TransactionType.choices)
    customer_ewallet_account = models.ForeignKey(CustomerEWalletAccount, null=True, blank=True, on_delete=models.CASCADE)
    company_ewallet_account = models.ForeignKey(CompanyEWalletAccount, null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision_transfer = models.DecimalField(decimal_places=3, max_digits=8)
    commision_client = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    ref_activity = models.ForeignKey(ClientActivity, null=True, blank=True, on_delete=models.CASCADE)

# 18
class EWalletAccountTransfer(BaseModelWithAuthor):
    transfer_date = models.DateTimeField(null=True,blank=True)
    transfer_number = models.IntegerField(null=True , blank=True)
    from_ewallet_account = models.ForeignKey(CompanyEWalletAccount, related_name='%(class)s_fromewalletaccount', null=True, blank=True, on_delete=models.CASCADE)
    to_ewallet_account = models.ForeignKey(CompanyEWalletAccount, related_name='%(class)s_toewalletaccount', null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)

# 19
class ExchangerBrokerAccountTransaction(BaseModelWithAuthor):
    class TransactionType(models.TextChoices):
        
        DEPOSIT = 'DP', _('Deposit')
        WITHDRAWAL = 'WI', _('Withdrawal')
        
    name = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.DateTimeField(null=True,blank=True)
    transaction_number = models.IntegerField(null=True , blank=True)
    transaction_type = models.CharField(max_length=255, choices=TransactionType.choices)
    customer_broker_account = models.ForeignKey(CustomerExchangerBrokerAccount, null=True, blank=True, on_delete=models.CASCADE)
    company_broker_account = models.ForeignKey(CompanyExchangerBrokerAccount, null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision_transfer = models.DecimalField(decimal_places=3, max_digits=8)
    commision_client = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)
    ref_activity = models.ForeignKey(ClientActivity, null=True, blank=True, on_delete=models.CASCADE)

# 20
class ExchangerBrokerAccountTransfer(BaseModelWithAuthor):
    transfer_date = models.DateTimeField(null=True,blank=True)
    transfer_number = models.IntegerField(null=True , blank=True)
    from_broker_account = models.ForeignKey(CompanyExchangerBrokerAccount, related_name='%(class)s_frombrokeraccount', null=True, blank=True, on_delete=models.CASCADE)
    to_broker_account = models.ForeignKey(CompanyExchangerBrokerAccount, related_name='%(class)s_tobrokeraccount', null=True, blank=True, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, null=True, blank=True, on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=3, max_digits=8)
    commision = models.DecimalField(decimal_places=3, max_digits=8)
    note = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to=upload_image_path,null=True, blank=True)


