from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from pages.models import Document
from pages.views import index as index_page


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


class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index_page)

    def test_request_index_page_retunrs_correct_html(self):
        request = HttpRequest()
        response = index_page(request)
        expected_html = render_to_string('pages/index.html')
        self.assertEqual(response.content.decode(), expected_html)
