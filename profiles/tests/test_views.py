import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from profiles.models import Profile
from pytest_django.asserts import assertTemplateUsed


class TestProfilesViews:

    client = Client()

    @pytest.mark.django_db
    def test_profiles_index_view(self):
        response = self.client.get(reverse('profiles_index'))
        assert response.status_code == 200
        assertTemplateUsed(response, 'profiles_index.html')

    @pytest.mark.django_db
    def test_profile_details_view(self):
        temp_user = User.objects.create(
            username='TestUser',
            first_name='Benoit',
            last_name='Renou',
            email='mail@test.com'
        )
        Profile.objects.create(
            user=temp_user,
            favorite_city='Sao Paulo'
        )
        response = self.client.get(reverse(
            'profile',
            kwargs={'username': 'TestUser'}
        ))
        content = response.content.decode()
        expected_content = '<h1>TestUser</h1>'

        assert content.find(expected_content) != -1
        assert response.status_code == 200
        assertTemplateUsed(response, 'profile.html')
