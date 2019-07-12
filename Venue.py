class Venue:
    def __init__(self, new_name = "Default Venue", new_lap_no=5, new_avg_lap_time=70, new_rain_prob=0.2):
        self.name = new_name
        self.lap_no = new_lap_no
        self.avg_lap_time = new_avg_lap_time
        self.rain_prob = new_rain_prob

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.name,self.lap_no, self.avg_lap_time, self.rain_prob)

    def get_avg_lap_time(self):
        return self.avg_lap_time

    def get_lap_no(self):
        return self.lap_no

    def get_name(self):
        return self.name

    def get_rain_prob(self):
        return self.rain_prob

    def set_avg_lap_time(self, new_avg_lap_time):
        try:
            valid_avg_lap_time(new_avg_lap_time)
            self.avg_lap_time = new_avg_lap_time
            return True
        except ValueError:
            return False

    def set_lap_no(self, new_lap_no):
        try:
            valid_lap_no(new_lap_no)
            self.lap_no = new_lap_no
            return True
        except ValueError:
            return False

    def set_name(self, new_name):
        try:
            valid_name(new_name)
            self.name = new_name
            return True
        except ValueError:
            return False

    def set_rain_prob(self, new_rain_prob):
        try:
            valid_rain_prob(new_rain_prob)
            self.rain_prob = new_rain_prob
            return True
        except ValueError:
            return False

def valid_avg_lap_time(new_avg_lap_time):
    if new_avg_lap_time < 60 or new_avg_lap_time > 90:
        raise ValueError("Average lap time cannot be less than 60 or greater than 90!")

def valid_lap_no(new_lap_no):
    if new_lap_no <= 0:
        raise ValueError("The number of laps cannot be less than or equal to 0!")

def valid_name(new_name):
    if len(new_name) == 0:
        raise ValueError("Venue name cannot be shorter than 0!")

def valid_rain_prob(new_rain_prob):
    if new_rain_prob <= 0 or new_rain_prob > 0.2:
        raise ValueError("Rain probability cannot be less than or equal to 0 or greater than 0.2!")