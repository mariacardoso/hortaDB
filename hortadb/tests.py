import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Species

class SpeciesModelTests(TestCase):

    def test_was_created_recently_with_future_species(self):
        """
        was_created_recently() returns False for species pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_species = Species(pub_date=time)
        self.assertIs(future_species.was_created_recently(), False)

    def test_was_created_recently_with_old_question(self):
        """
        was_created_recently() returns False for species whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_species = Species(pub_date=time)
        self.assertIs(old_species.was_created_recently(), False)

    def test_was_created_recently_with_recent_question(self):
        """
        was_created_recently() returns True for species whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_species = Species(pub_date=time)
        self.assertIs(recent_species.was_created_recently(), True)


def create_species(common_name, days):
    """
    Create a species with the given 'common_name' and add
    the given number of 'days' offset to now (negative for species published
    in the past, positive for species that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Species.objects.create(common_name=common_name, pub_date=time)


class SpeciesIndexViewTests(TestCase):
    def test_no_species(self):
        """
        If no species exist, an appropriate messasge is displayed.
        """
        response = self.client.get(reverse('hortadb:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No species are available.")
        self.assertQuerysetEqual(response.context['species_list'], [])

    def test_past_species(self):
        """
        Species with a pub_date in the past are displayed on the
        index page.
        """
        create_species(common_name="Past species.", days=-30)
        response = self.client.get(reverse('hortadb:index'))
        self.assertQuerysetEqual(
            response.context['species_list'],
            ['<Species: Past species.>']
        )

    def test_future_species(self):
        """
        Species with a pub_date in the future aren't displayed
        on the index page.
        """
        create_species(common_name="Future species.", days=30)
        response = self.client.get(reverse('hortadb:index'))
        self.assertContains(response, "No species are available.")
        self.assertQuerysetEqual(response.context['species_list'], [])

    def test_future_species_and_past_species(self):
        """
        Even if both past and future species exist, only past 
        species are displayed.
        """
        create_species(common_name="Future species.", days=30)
        create_species(common_name="Past species.", days=-30)
        response = self.client.get(reverse('hortadb:index'))
        self.assertQuerysetEqual(
            response.context['species_list'],
            ['<Species: Past species.>']
        )

    def test_two_past_species(self):
        """
        The species index page may display multiple species.
        """
        create_species(common_name="Past species 1.", days=-30)
        create_species(common_name="Past species 2.", days=-50)
        response = self.client.get(reverse('hortadb:index'))
        self.assertQuerysetEqual(
            response.context['species_list'],
            ['<Species: Past species 2.>', '<Species: Past species 1.>']
        )


class SpeciesDetailViewTests(TestCase):
    def test_future_species(self):
        """
        The detail view of a species with a pub_date in the future
        returns a 404 not found.
        """
        future_species = create_species(common_name='Future species', days=5)
        url = reverse('hortadb:detail', args=(future_species.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_species(self):
        """
        The detail view of a species with a pub_date in the past
        display's the species' text.
        """
        past_species = create_species(common_name='Past species', days=-5)
        url = reverse('hortadb:detail', args=(past_species.id,))
        response = self.client.get(url)
        self.assertContains(response, past_species.common_name)