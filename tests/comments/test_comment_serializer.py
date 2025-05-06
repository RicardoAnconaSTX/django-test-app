import datetime
import pytest
from unittest.mock import MagicMock
from comments.api.serializers import CommentSerializer

testDate = datetime.datetime.now()
    # Mock user, category, and post instances
mock_user = MagicMock()
mock_user.id = 1

mock_post = MagicMock()
mock_post.id = 10

data = {
        'content': 'Test comment',
        'user': mock_user.id,
        'post': mock_post.id
    }

def test_comment_serializer_valid_data():

    # Mock the serializer's Meta queryset to accept mocked user/post
    serializer = CommentSerializer(data=data)
    serializer.fields['user'].queryset = MagicMock()
    serializer.fields['post'].queryset = MagicMock()

    assert serializer.is_valid(), serializer.errors
    assert serializer.validated_data['content'] == 'Test comment'

def test_comments_serialzer_missing_field():
    data = {
        'content': 'test'
    }

    serializer = CommentSerializer(data=data)
    assert not serializer.is_valid()
    assert 'user' in serializer.errors

def test_comments_serializer_output():
    mock_instance = MagicMock()
    mock_instance.content = 'Mock content'
    mock_instance.created_at = testDate
    mock_instance.user = 'Mock User'

    serializer = CommentSerializer(mock_instance)
    assert serializer.data['content'] == 'Mock content'


