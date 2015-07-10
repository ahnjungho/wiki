from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
from pages.models import Category
from pages.models import Document
from pages.views import index as index_page


class CategoryModelTest(TestCase):
    def test_saving_and_retrieving_category(self):
        category1 = Category(name='Book', slug='book')
        category1.save()
        category2 = Category(name='Movie', slug='movie')
        category2.save()

        saved_categories = Category.objects.all()
        self.assertEqual(saved_categories.count(), 2)

        saved_category1 = saved_categories[0]
        saved_category2 = saved_categories[1]
        self.assertEqual(saved_category1.name, 'Book')
        self.assertEqual(saved_category2.name, 'Movie')
        self.assertEqual(saved_category2.__str__(), 'Movie')


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

    def test_document_markdown(self):
        user = User(username='abc', password='bbb')
        user.save()
        document1 = Document(title='abcd',
                             slug='a',
                             user=user,
                             content='abcd')
        document1.save()

        saved_document1 = Document.objects.first()

        self.assertEqual(saved_document1.markdown(), '<p>abcd</p>')

    def test_document_category(self):
        user = User(username='abc', password='bbb')
        user.save()
        category = Category(name='Book', slug='book')
        category.save()
        document1 = Document(title='abcd',
                             slug='a',
                             user=user,
                             category=category,
                             content='abcd')
        document1.save()

        saved_document1 = Document.objects.first()

        self.assertEqual(saved_document1.category.name, 'Book')


class IndexPageTest(TestCase):
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index_page)

    def test_request_index_page_retunrs_correct_html(self):
        request = HttpRequest()
        response = index_page(request)
        expected_html = render_to_string('pages/index.html')
        self.assertEqual(response.content.decode(), expected_html)
