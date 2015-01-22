from django.test import TestCase
from django.core.urlresolvers import reverse

#Apps
from tiny.models import Link

class TinyAppTests(TestCase):
    
    def test_url_length(self):
        """ 
        Test short-url is acutally shorter that original url
        """
        
        url = 'www.google.com'
        link = Link(url=url)
        short_url = Link.shorten(link)

        self.assertLess(len(short_url), len(url))

    def test_recover_url(self):
        """ 
        Test whether we could recover original url form short url
        """
        
        url = 'http://www.google.com'
        link = Link(url=url)

        short_url = Link.shorten(link)
        link.save()

        # May be another user is trying to recover original url

        expand_url = Link.expand(short_url)

        self.assertEqual(url, expand_url)

    def test_check_form_element(self):
        """
        Test whether form element exists on homepage
        """

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_check_shorurl_generates(self):
        """
        Test shorturl is generated after submitting the form
        """

        url = 'http://www.google.com/'

        response = self.client.post(reverse('home'), {'url':url}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('link', response.context)
        link = response.context['link']
        short_url = Link.shorten(link)

        self.assertEqual(url, link.url)
        self.assertIn('short_url', response.content)

    def test_short_redirects_long(self):
        """
        test whether the short-url redirects to original url
        """

        url = 'https://www.google.com/'
        link = Link.objects.create(url=url)

        short_url = Link.shorten(link)
        response = self.client.get(reverse('redirect-url', kwargs={'short_url':short_url}))
        self.assertRedirects(response, url)
        
