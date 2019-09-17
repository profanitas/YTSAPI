import sys, re
from xml.etree import ElementTree
import requests


class YTAPI():
    class CouldNotRetrieveTranscript(Exception):
        """
        Raised if transcript could not be retrieved.
        """
        ERROR_MESSAGE = (
            'Could not get the transcript for the video {video_url}! '
            'This usually happens if one of the following things is the case:\n'
            ' - Subtitles have been disabled by the uploader\n'
            ' - English transcript is not available\n'
            ' - The video is no longer available.\n\n'
            'If none of these things is the case, please create an issue at https://github.com/theabuseproject/ytapi/issues'
        )
        def __init__(self, video_id):
            super(YTAPI.CouldNotRetrieveTranscript, self).__init__(
                self.ERROR_MESSAGE.format(video_url=YTAPIFetcher.WATCH_URL.format(video_id=video_id))
            )
            self.video_id = video_id

    @classmethod
    def get_transcript(cls, video_id, proxies=None):
        """
        Retrieves the transcript for a single video.
        :param video_id: the youtube video id
        :type video_id: str
        :param proxies: a dictionary mapping of http and https proxies to be used for the network requests
        :type proxies: {'http': str, 'https': str} - http://docs.python-requests.org/en/master/user/advanced/#proxies
        :return: a list of dictionaries containing the 'text', 'start' and 'duration' keys
        :rtype: [{'text': str, 'start': float, 'end': float}]
        """
        try:
            return YTAPIParser(YTAPIFetcher(video_id, proxies).fetch()).parse()
        except Exception:
            raise YTAPI.CouldNotRetrieveTranscript(video_id)

class YTAPIFetcher():
    WATCH_URL = 'https://www.youtube.com/watch?v={video_id}'
    API_BASE_URL = 'https://www.youtube.com/api/{api_url}'
    LANGUAGE_REGEX = re.compile(r'(&lang=.*&)|(&lang=.*)')
    def __init__(self, video_id, proxies):
        self.video_id = video_id
        self.proxies = proxies

    def fetch(self):
        if self.proxies:
            fetched_site = requests.get(self.WATCH_URL.format(video_id=self.video_id), proxies=self.proxies).text
        else:
            fetched_site = requests.get(self.WATCH_URL.format(video_id=self.video_id)).text
        timedtext_url_start = fetched_site.find('timedtext')
        language = 'en'
        response = self.YTAPICall(fetched_site, timedtext_url_start, language)
        if response:
            return response
        return None

    def YTAPICall(self, fetched_site, timedtext_url_start, language='en'):
        url = self.API_BASE_URL.format(
            api_url=fetched_site[
                timedtext_url_start:timedtext_url_start + fetched_site[timedtext_url_start:].find('"')
            ].replace(
                '\\u0026', '&'
            ).replace(
                '\\', ''
            )
        )
        if language:
            url = re.sub(self.LANGUAGE_REGEX, '&lang={language}&'.format(language=language), url)
        if self.proxies:
            return requests.get(url, proxies=self.proxies).text
        else:
            return requests.get(url).text

class YTAPIParser():
    HTML_TAG_REGEX = re.compile(r'<[^>]*>', re.IGNORECASE)
    def __init__(self, plain_data):
        self.plain_data = plain_data
    def parse(self):
        return [
            {
                'text': re.sub(self.HTML_TAG_REGEX, '', unescape(xml_element.text)),
                'start': float(xml_element.attrib['start']),
                'duration': float(xml_element.attrib['dur']),
            }
            for xml_element in ElementTree.fromstring(self.plain_data)
            if xml_element.text is not None
        ]