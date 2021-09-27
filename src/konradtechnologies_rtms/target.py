

class RadarTarget(object):
    def __init__(self, distance, rcs, velocity, azimuth, elevation):
        """
        Creates a static radar target

        :param distance: Simulated object distance, in meters
        :param rcs: Simulated object RCS, in dBsm
        :param velocity: Simulated object velocity, in m/sec
        :param azimuth: Simulated object azimuth, in deg
        :param elevation: Simulated object elevation, in deg
        """
        self.distance = distance
        self.rcs = rcs
        self.velocity = velocity
        self.azimuth = azimuth
        self.elevation = elevation

    def __str__(self):
        return "Distance: {} m\n" \
               "RCS: {} dBsm\n" \
               "Velocity: {} m/sec\n" \
               "Azimuth: {} deg\n" \
               "Elevation: {} deg".format(self.distance, self.rcs, self.velocity, self.azimuth, self.elevation)
