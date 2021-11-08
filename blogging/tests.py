"""
tests
"""

# pylint: disable=C0103

from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User

from blogging.models import Post


class PostTestCase(TestCase):
    """
    test case
    """

    fixtures = ["blogging_test_fixture.json"]

    def setUp(self):
        """
        setup
        """
        self.user = User.objects.get(pk=1)

    def test_string_representation(self):
        """
        test string representation
        """
        expected = "This is a title"
        p1 = Post(title=expected)
        actual = str(p1)
        self.assertEqual(expected, actual)
