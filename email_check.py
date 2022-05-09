from django.core.exceptions import ValidationError
from django.core.validators import validate_email

value = "bharatc@spanidea.com"

try:
    validate_email(value)
except ValidationError as e:
    print("bad email, details:", e)
else:
    print("good email")
