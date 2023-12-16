from app.email_service import send_email


def test_send_email():

    assert send_email("jja106@georgetown.edu", "YOUR REQUESTED RECIPE", "YOUR REQUESTED RECIPE") == 202