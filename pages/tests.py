from django.contrib.auth.models import User
from django.test import TestCase
from pages.models import Document


class DocumentModelTest(TestCase):
    def test_saving_and_retrieving_documents(self):
        user = User(username='abc', password='bbb')
        user.save()
        document1 = Document(title='abcd', slug='a', user=user)
        document1.save()
        document2 = Document(title='abcde', slug='b', user=user)
        document2.save()

        saved_documets = Document.objects.all()
        self.assertEqual(saved_documets.count(), 2)

        saved_document1 = saved_documets[0]
        saved_document2 = saved_documets[1]
        self.assertEqual(saved_document1.title, 'abcd')
        self.assertEqual(saved_document2.title, 'abcde')
