from rest_framework import serializers
from .models import Bank, BankAccount, BankAccountTransaction, BankAccountTransfer, CompanyBankAccount, CompanyEWalletAccount, CompanyExchangerBrokerAccount, Currency, CustomerBankAccount, CustomerEWalletAccount, CustomerExchangerBrokerAccount, EWallet, EWalletAccount, EWalletAccountTransaction, EWalletAccountTransfer, ExchangeCurrency, ExchangerBroker, ExchangerBrokerAccount, ExchangerBrokerAccountTransaction, ExchangerBrokerAccountTransfer

# 1
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

# 2
class ExchangeCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeCurrency
        fields = '__all__'

# 3
class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'

# 4
class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

# 5
class CompanyBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBankAccount
        fields = '__all__'

# 6
class CustomerBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerBankAccount
        fields = '__all__'

# 7
class EWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWallet
        fields = '__all__'

# 8
class EWalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWalletAccount
        fields = '__all__'

# 9
class CompanyEWalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEWalletAccount
        fields = '__all__'

# 10
class CustomerEWalletAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerEWalletAccount
        fields = '__all__'

# 11
class ExchangerBrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangerBroker
        fields = '__all__'

# 12
class ExchangerBrokerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangerBrokerAccount
        fields = '__all__'

# 13
class CompanyExchangerBrokerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyExchangerBrokerAccount
        fields = '__all__'

# 14
class CustomerExchangerBrokerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerExchangerBrokerAccount
        fields = '__all__'

# 15
class BankAccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountTransaction
        fields = '__all__'

# 16
class BankAccountTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountTransfer
        fields = '__all__'

# 17
class EWalletAccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWalletAccountTransaction
        fields = '__all__'

# 18
class EWalletAccountTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = EWalletAccountTransfer
        fields = '__all__'

# 19
class ExchangerBrokerAccountTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangerBrokerAccountTransaction
        fields = '__all__'

# 20
class ExchangerBrokerAccountTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangerBrokerAccountTransfer
        fields = '__all__'