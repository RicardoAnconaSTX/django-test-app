import pytest
from categories.models import Category
from categories.api.serializers import CategorySerializer
from unittest.mock import MagicMock

pytestmark = pytest.mark.django_db

def test_category_serializer_valid_data():
    data = {
        'title': 'Books',
        'slug': 'books',
        'published': True
    }
    serializer = CategorySerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data['title'] == 'Books'
    assert serializer.validated_data['slug'] == 'books'
    assert serializer.validated_data['published'] is True

def test_category_serializer_missing_field():
    data = {
        'slug': 'missing-title',
        'published': False
    }
    serializer = CategorySerializer(data=data)
    assert not serializer.is_valid()
    assert 'title' in serializer.errors


def test_category_serializer_output():
    mock_instance = MagicMock()
    mock_instance.title = 'Mock Title'
    mock_instance.slug = 'mock-slug'
    mock_instance.published = True

    serializer = CategorySerializer(mock_instance)
    data = serializer.data

    assert data['title'] == 'Mock Title'
    assert data['slug'] == 'mock-slug'
    assert data['published'] is True
