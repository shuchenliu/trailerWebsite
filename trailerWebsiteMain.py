#!/usr/bin/python3

from video import Movies
from video import Shows
import fresh_tomatoes

# functions to gather actor information


def get_actors(*args):
    actorlist = {}
    for v in args:
        names = v.split()
        wiki = ""
        i = 0
        for name in names:
            if i == 0:
                wiki = name
            else:
                wiki += "_" + name
            i += 1

        actorlist[v] = "https://en.wikipedia.org/wiki/" + wiki

    return actorlist

# Movie: title, storyline, image, trailer, majorArtist, year


ab_actors = get_actors("Kevin Spacey", "Annette Bening", "Thora Birch")
american_beauty = Movies("American Beauty",
                         """Mid-age father falls
                          in love with daughter's classmate""",
                         "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",   # noqa
                         "https://www.youtube.com/watch?v=3ycmmJ6rxA8",
                         ab_actors,
                         "1999")

tg_actors = get_actors("Tom Cruise", "Kelly McGillis")
top_gun = Movies("Top Gun",
                 "Two American fighter-jet pilots compete with each other",
                 "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",  # noqa
                 "https://www.youtube.com/watch?v=qAfbp3YX9F0",
                 tg_actors,
                 "1986")


# Shows: title, storyline, image, trailer,
# majorArtist, duration, isCurrent, currentSeason


himym_actors = get_actors("Josh Radnor",
                          "Jason Segel",
                          "Cobie Smulders",
                          "Neil Patrick Harris",
                          "Alyson Hannigan")
himym = Shows("How I Met Your Mother",
              "Five friends in NYC and the love story of theirs",
              "https://upload.wikimedia.org/wikipedia/en/f/fc/Howimetyourmother.jpg",  # noqa
              "https://www.youtube.com/watch?v=yOe4_kdqsmU",
              himym_actors,
              "2004 - 2013",
              "No",
              "")

shml_actors = get_actors("William H. Macy",
                         "Emmy Rossum",
                         "Justin Chatwin",
                         "Ethan Cutkosky")
shameless = Shows("Shameless",
                  "The life of a family living in Southside of Chicago",
                  "http://www.sho.com/site/image-bin/images/408_7_0/408_7_0_prm-keyart_1700x1063.jpg",  # noqa
                  "https://www.youtube.com/watch?v=ITsirWLf-W8",
                  shml_actors,
                  "2011 - Current",
                  "Yes",
                  "6")

contents = [american_beauty, top_gun, himym, shameless]
fresh_tomatoes.open_movies_page(contents)
