class video():
    def __init__(self, title, storyline, image, trailer, majorArtist):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = image
        self.trailer_youtube_url = trailer
        self.majorArtist = majorArtist


class movies(video):
    def __init__(self, title, storyline, image, trailer, majorArtist, year):
        video.__init__(self, title, storyline, image, trailer, majorArtist)
        self.year = year


class shows(video):
    def __init__(self, title, storyline, image, trailer, majorArtist, duration, isCurrent, currentSeason):
        video.__init__(self, title, storyline, image, trailer, majorArtist)
        self.duration = duration
        self.isCurrent = isCurrent
        if isCurrent == "Yes":
            self.currentSeason = currentSeason
            ##self.currentEpisode = currentEpisode
        else:
            self.currentSeason = "Complete"
