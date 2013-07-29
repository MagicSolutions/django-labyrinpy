from datetime import datetime
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client

from models import Report, Message

data_for_report = {
    'msg_id': 1,
    'source': '16130',
    'dest': '359 88 66 66 66',
    'status': 'OK',
    'code': 0,
    'description': 'Message delivered',
    'timestamp': datetime(2013, 0o7, 22, 10, 0o4, 55)
}


class CreateReport(TestCase):

    def setUp(self):
        self.query_string = data_for_report.copy()
        self.client = Client()

    def tearDown(self):
        pass

    def test_report_has_been_created(self):
        Message.objects.create(destination="123", message_type="text", id=1)
        reports_before = Report.objects.all().count()
        self.client.get(reverse('create-report'), self.query_string)
        reports_after = Report.objects.all().count()
        self.assertTrue(reports_after > reports_before)

    def test_report_for_nonexistant_message(self):
        Message.objects.create(destination="unkn", message_type="text", id=2)
        respond = self.client.get(reverse('create-report'), self.query_string)
        self.assertEqual(404, respond.status_code)

    def test_report_for_message_that_already_has_report(self):
        Message.objects.create(destination='123', message_type='text', id=1)
        self.client.get(reverse('create-report'), self.query_string)
        respond = self.client.get(reverse('create-report'), self.query_string)
        reports_after = Report.objects.all().count()
        self.assertEqual((2, 200), (reports_after, respond.status_code))


class SendSMS(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_send_sms(self):
        pass