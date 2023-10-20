from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)  # This assertion will always pass
