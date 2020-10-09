from django.test import TestCase


class TwillioSMSSmokeTests(TestCase):
    """
    Lets make sure we can import the model
    """

    def test_user_model_importable(self):
        try:
            from twiliosms.models import TwilioSMS
        except Exception as e:
            self.fail(e)


class TwillioSettingsSmokeTest(TestCase):
    """
    Lets make sure we can import the model
    """

    def test_user_model_importable(self):
        try:
            from twiliosms.models import TwilioSettings
        except Exception as e:
            self.fail(e)


class TwillioNumberSmokeTest(TestCase):
    """
    Lets make sure we can import the model
    """

    def test_user_model_importable(self):
        try:
            from twiliosms.models import TwilioNumber
        except Exception as e:
            self.fail(e)
