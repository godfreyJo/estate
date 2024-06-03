from django.test import TestCase, Client
from django.core.mail import outbox
from django.core.exceptions import ImproperlyConfigured

from.models import Enquiry


class SendEnquiryEmailTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = '/api/send-enquiry-email/'
        self.test_data = {
            "subject": "Test Enquiry",
            "name": "John Doe",
            "email": "johndoe@example.com",
            "message": "This is a test enquiry."
        }

    def test_send_enquiry_email_network_error(self):
        # Mock the send_mail function to raise a network error
        def mock_send_mail(*args, **kwargs):
            raise ImproperlyConfigured("Network error")

        from django.core.mail import send_mail
        send_mail = mock_send_mail

        # Send the POST request
        response = self.client.post(self.url, self.test_data, format='json')

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the response data
        self.assertEqual(response.data, {"fail": "Enquiry was not sent. Please try again"})

        # Check that no email was sent
        self.assertEqual(len(outbox), 0)

        # Check that no Enquiry object was created
        self.assertEqual(Enquiry.objects.count(), 0)