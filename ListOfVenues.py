import Venue

class ListOfVenues:
    def __init__(self, new_venues=[]):
        self.venues = new_venues

    def __str__(self):
        info = ""
        for i in self.venues:
            info += str(i)
        return info

    def get_venue(self, index):
        try:
            return self.venues[index]
        except IndexError:
            return Venue.Venue()

    def get_venues(self):
        return self.venues

    def set_venue(self, index, new_name, new_lap_no, new_avg_lap_time, new_rain_prob):
        flag = False
        try:
            flag = flag and self.venues[index].set_name(new_name)
            flag = flag and self.venues[index].set_lap_no(new_lap_no)
            flag = flag and self.venues[index].set_avg_lap_time(new_avg_lap_time)
            flag = flag and self.venues[index].set_rain_prob(new_rain_prob)
            return flag
        except IndexError:
            return flag

    def set_venues(self, new_venues):
        self.venues = new_venues
