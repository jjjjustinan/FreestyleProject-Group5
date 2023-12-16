from app.email_service import send_email


def test_send_email():

    assert send_email() == 202