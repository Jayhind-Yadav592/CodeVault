from django.test import TestCase
from django.utils import timezone
from .models import *

class KnowledgeCategoryModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = KnowledgeCategory._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = KnowledgeCategory._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = KnowledgeCategory._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = KnowledgeCategory._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = KnowledgeCategory._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = KnowledgeCategory._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_name(self):
        field = KnowledgeCategory._meta.get_field('name')
        self.assertIsNotNone(field)
    def test_field_type_name(self):
        field = KnowledgeCategory._meta.get_field('name')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_description(self):
        field = KnowledgeCategory._meta.get_field('description')
        self.assertIsNotNone(field)
    def test_field_type_description(self):
        field = KnowledgeCategory._meta.get_field('description')
        self.assertEqual(field.__class__.__name__, 'TextField')

class KnowledgeArticleModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = KnowledgeArticle._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = KnowledgeArticle._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = KnowledgeArticle._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = KnowledgeArticle._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = KnowledgeArticle._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = KnowledgeArticle._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_title(self):
        field = KnowledgeArticle._meta.get_field('title')
        self.assertIsNotNone(field)
    def test_field_type_title(self):
        field = KnowledgeArticle._meta.get_field('title')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_content(self):
        field = KnowledgeArticle._meta.get_field('content')
        self.assertIsNotNone(field)
    def test_field_type_content(self):
        field = KnowledgeArticle._meta.get_field('content')
        self.assertEqual(field.__class__.__name__, 'TextField')
    def test_field_existence_category(self):
        field = KnowledgeArticle._meta.get_field('category')
        self.assertIsNotNone(field)
    def test_field_type_category(self):
        field = KnowledgeArticle._meta.get_field('category')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_author(self):
        field = KnowledgeArticle._meta.get_field('author')
        self.assertIsNotNone(field)
    def test_field_type_author(self):
        field = KnowledgeArticle._meta.get_field('author')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_status(self):
        field = KnowledgeArticle._meta.get_field('status')
        self.assertIsNotNone(field)
    def test_field_type_status(self):
        field = KnowledgeArticle._meta.get_field('status')
        self.assertEqual(field.__class__.__name__, 'CharField')
    def test_field_existence_project_reference(self):
        field = KnowledgeArticle._meta.get_field('project_reference')
        self.assertIsNotNone(field)
    def test_field_type_project_reference(self):
        field = KnowledgeArticle._meta.get_field('project_reference')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_version(self):
        field = KnowledgeArticle._meta.get_field('version')
        self.assertIsNotNone(field)
    def test_field_type_version(self):
        field = KnowledgeArticle._meta.get_field('version')
        self.assertEqual(field.__class__.__name__, 'IntegerField')

class ArticleFeedbackModelDetailedTest(TestCase):
    def test_field_existence_id(self):
        field = ArticleFeedback._meta.get_field('id')
        self.assertIsNotNone(field)
    def test_field_type_id(self):
        field = ArticleFeedback._meta.get_field('id')
        self.assertEqual(field.__class__.__name__, 'UUIDField')
    def test_field_existence_created_at(self):
        field = ArticleFeedback._meta.get_field('created_at')
        self.assertIsNotNone(field)
    def test_field_type_created_at(self):
        field = ArticleFeedback._meta.get_field('created_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_updated_at(self):
        field = ArticleFeedback._meta.get_field('updated_at')
        self.assertIsNotNone(field)
    def test_field_type_updated_at(self):
        field = ArticleFeedback._meta.get_field('updated_at')
        self.assertEqual(field.__class__.__name__, 'DateTimeField')
    def test_field_existence_article(self):
        field = ArticleFeedback._meta.get_field('article')
        self.assertIsNotNone(field)
    def test_field_type_article(self):
        field = ArticleFeedback._meta.get_field('article')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_user(self):
        field = ArticleFeedback._meta.get_field('user')
        self.assertIsNotNone(field)
    def test_field_type_user(self):
        field = ArticleFeedback._meta.get_field('user')
        self.assertEqual(field.__class__.__name__, 'ForeignKey')
    def test_field_existence_is_helpful(self):
        field = ArticleFeedback._meta.get_field('is_helpful')
        self.assertIsNotNone(field)
    def test_field_type_is_helpful(self):
        field = ArticleFeedback._meta.get_field('is_helpful')
        self.assertEqual(field.__class__.__name__, 'BooleanField')
    def test_field_existence_comments(self):
        field = ArticleFeedback._meta.get_field('comments')
        self.assertIsNotNone(field)
    def test_field_type_comments(self):
        field = ArticleFeedback._meta.get_field('comments')
        self.assertEqual(field.__class__.__name__, 'TextField')


