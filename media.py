import webbrowser


class Movie():
    # Movie constructor defines all the needed details
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    # open a new popup window and play the movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
