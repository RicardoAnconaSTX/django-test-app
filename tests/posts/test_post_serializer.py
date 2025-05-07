from unittest.mock import patch, MagicMock
from posts.api.serializers import PostSerializer
mock_user = MagicMock()
mock_user.username = 'mockuser'
mock_category = MagicMock()
mock_category.title = 'MockCategory'
mock_post = MagicMock()
mock_post.title = 'Mock Post'
mock_post.content = 'Some content here.'
mock_post.slug = 'mock-post'
#mock_post.miniature = 'posts/images/mock.jpg'
mock_post.created_at = '2025-05-06T00:00:00Z'
mock_post.published = True
mock_post.user = mock_user
mock_post.category = mock_category
def test_post_serializer_valid_data():
    serializer = PostSerializer(instance=mock_post)
    data = serializer.data
    assert data['title'] == 'Mock Post'
    assert data['slug'] == 'mock-post'
    assert data['created_at'] == '2025-05-06T00:00:00Z'
    assert data['published'] is True
    assert data['user']['username'] == 'mockuser'
    assert data['category']['title'] == 'MockCategory'
    assert data['content'] == 'Some content here.'

    
def test_post_serialzer_missing_field():
    data = {
        'title': 'test'
    }

    serializer = PostSerializer(data=data)
    assert not serializer.is_valid()
    assert 'content' in serializer.errors
