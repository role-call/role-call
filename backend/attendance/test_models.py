from django.test import TestCase


class FooTest(TestCase):
    def test_foo_works(self):
        self.assertEqual("foo", "foo")