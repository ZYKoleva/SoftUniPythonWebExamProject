from django.contrib.auth.models import User
from django.test import TestCase
from estate_app_auth.forms import RegisterForm


class RegisterFormTestCase(TestCase):
    def test_registerUsername_alreadyExists_raiseValidationError(self):
        User.objects.create(username="Pesho567", password='BrumDrun@123')

        secondUserForm = RegisterForm(
            {'username': 'Pesho567',
            'password1': 'BrumDrun@111',
            'password2': 'BrumDrun@111'}
        )
        self.assertFalse(secondUserForm.is_valid())

    def test_passwords_doesNotMatch_raiseValidationError(self):
        UserForm = RegisterForm(
            {'username': 'Pesho567',
             'password1': 'BrumDrun@123',
             'password2': 'BrumDrun@111'}
        )
        self.assertFalse(UserForm.is_valid())

    def test_userRegistered_withValidUsername_andPasswords(self):
        UserForm = RegisterForm(
            {'username': 'Pesho567',
             'password1': 'BrumDrun@123',
             'password2': 'BrumDrun@123'}
        )
        self.assertTrue(UserForm.is_valid())
        UserForm.save()
        registered_user = User.objects.get(username='Pesho567')
        self.assertIsNotNone(registered_user)
