from video import movies
from video import shows
import fresh_tomatoes
##function to gather actor information
def actors(*args):
    actorlist={}
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

## movie: title, storyline, image, trailer, majorArtist, year
ab_actors = actors("Kevin Spacey", "Annette Bening", "Thora Birch")
american_beauty = movies("American Beauty",
                        "Mid-age father falls in love with daughter's classmate",
                        "https://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
                        "https://www.youtube.com/watch?v=3ycmmJ6rxA8",
                        ab_actors,
                        "1999")

tg_actors = actors("Tom Cruise", "Kelly McGillis")
top_gun = movies("Top Gun",
                 "Two American fighter-jet pilots compete with each other",
                "https://upload.wikimedia.org/wikipedia/en/4/46/Top_Gun_Movie.jpg",
                "https://www.youtube.com/watch?v=qAfbp3YX9F0",
                tg_actors,
                "1986")


##shows: title, storyline, image, trailer, majorArtist, duration, isCurrent, currentSeason
himym_actors = actors("Josh Radnor",
                      "Jason Segel",
                      "Cobie Smulders",
                      "Neil Patrick Harris",
                      "Alyson Hannigan")
himym = shows("How I Met Your Mother",
              "Five friends in NYC and the love story of theirs",
              "https://upload.wikimedia.org/wikipedia/en/f/fc/Howimetyourmother.jpg",
              "https://www.youtube.com/watch?v=yOe4_kdqsmU",
              himym_actors,
              "2004 - 2013",
              "No",
              "")

shml_actors = actors("William H. Macy",
                     "Emmy Rossum",
                     "Justin Chatwin",
                     "Ethan Cutkosky")
shameless = shows("Shameless",
                  "The life of a family living in Southside of Chicago",
                  "http://www.sho.com/site/image-bin/images/408_7_0/408_7_0_prm-keyart_1700x1063.jpg",
                  "https://www.youtube.com/watch?v=ITsirWLf-W8",
                  shml_actors,
                  "2011 - Current",
                  "Yes",
                  "6")

contents = [american_beauty, top_gun, himym, shameless]
fresh_tomatoes.open_movies_page(contents)
