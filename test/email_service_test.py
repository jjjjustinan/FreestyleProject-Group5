from app.email_service import *


def test_send_email():

    assert send_email() == 202