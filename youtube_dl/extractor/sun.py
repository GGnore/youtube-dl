# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor

# python -m youtube_dl https://www.thesun.co.uk/tvandshowbiz/2261604/orlando-bloom-and-katy-perry-post-adorable-instagram-video-together-celebrating-thanksgiving-after-split-rumours/
# python test/test_download.py TestDownload.test_SunExtractor


class SunExtractorIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?thesun\.co\.uk/(?P<id>.+)'
    _TEST = {
            'url': 'https://www.thesun.co.uk/tvandshowbiz/2261604/orlando-bloom-'
                   'and-katy-perry-post-adorable-instagram-video-'
                   'together-celebrating-thanksgiving-after-split-rumours/',

            'md5': '5b77ff23fb86980dd85dfbe2b95b50f8',

            'info_dict': {
                'id': '2261604',
                'ext': 'mp4',
                'title': 'Orlando Bloom and Katy Perry post adorable Instagram '
                         'video together celebrating Thanksgiving after split rumours',
                #'thumbnail': 're:^https?://.*\.jpg$',
                # TODO more properties, either as:
                # * A value
                # * MD5 checksum; start the string with md5:
                # * A regular expression; start the string with re:
                # * Any Python type (for example int or float)
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        # with open("hello.html", mode="w") as f:
        #     for l in webpage:
        #         f.writelines(l)

        video_title = "lol"
        url_end = self._search_regex(r'thesun-ooyala-player-(.+?)\"', webpage, 'url')
        video_url = "https://clips.news.co.uk/thesun/" + url_end + "/DOcJ-FxaFrRg4gtDEwOnI5OjAwMTvlg2"

        return {
            'id':       video_id,
            'title':    video_title,
            'url':      video_url,
            'ext':      'mp4'
        }