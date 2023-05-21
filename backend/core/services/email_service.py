import os

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from core.services.jwt_service import ActivateToken, JWTService, PremiumAddToken, RecoveryPasswordToken

# from core.services.jwt_service import ActivateToken, JWTService


class EmailService:
    @staticmethod
    def send_email(to: str, template_name: str, context: dict, subject=''):
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(subject, from_email=os.environ.get('EMAIL_HOST_USER'),
                                     to=[to])

        msg.attach_alternative(html_content, 'text/html')
        msg.send()

    @classmethod
    def register_email(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f'http://localhost:3000/activate/{token}'
        cls.send_email(user.email, 'register.html', {'name': user.profile.name, 'url': url}, 'Register')

    @classmethod
    def recovery_password(cls, user):
        token = JWTService.create_token(user, RecoveryPasswordToken)
        url = f'http://localhost:3000/recovery_password/{token}'
        cls.send_email(user.email, 'recovery_password.html', {'name': user.profile.name, 'url': url}, 'Recovery')

    @classmethod
    def premium_add(cls, user):
        token = JWTService.create_token(user, PremiumAddToken)
        url = f'http://localhost:3000/premium_add/{token}'
        cls.send_email(user.email, 'premium_add.html', {'name': user.profile.name, 'url': url}, 'Premium')
