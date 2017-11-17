#!/usr/bin/python3


class Video(object):
    '''
    Base class for video
    '''
    def __init__(self, title, storyline, image, trailer, majorArtists):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        self.majorArtists = majorArtists


class Movies(Video):
    '''
    Sub-class Movies, inheriting Video class
    '''
    def __init__(self, title, storyline, image, trailer, majorArtists, year):
        super().__init__(title, storyline, image, trailer, majorArtists)
        self.year = year


class Shows(Video):
    '''
    Sub-class Shows, inheriting Video class
    '''
    def __init__(self,
                 title,
                 storyline,
                 image,
                 trailer,
                 majorArtists,
                 duration,
                 isCurrent,
                 currentSeason):
        super().__init__(title, storyline, image, trailer, majorArtists)
        self.duration = duration
        self.isCurrent = isCurrent

        if isCurrent == "Yes":
            self.currentSeason = currentSeason
        else:
            self.currentSeason = "Complete"
