from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, is_staff=True,is_active=True,is_admin=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email = self.normalize_email(email),
            full_name=full_name
            )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email,full_name=None, password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
            )
        return user

    def create_superuser(self, email, full_name=None, password=None):
        user = self.create_user(email, full_name=full_name, password=password, is_staff=True,is_admin=True)
        return user