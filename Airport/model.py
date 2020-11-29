class Model:

    def __init__(self, title, places, load_capacity):
        self.title = title
        self.places = places
        self.load_capacity = load_capacity

    def __repr__(self):
        return self.title