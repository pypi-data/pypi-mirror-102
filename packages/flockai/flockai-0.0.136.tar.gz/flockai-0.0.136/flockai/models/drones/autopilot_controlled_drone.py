import abc

from flockai.interfaces.drone import IDrone


class AutopilotControlledDrone(IDrone, abc.ABC):
    def __init__(self, devices):
        super().__init__(devices)
        self.target = [5, 5]
        self.prev_distance = self.get_distance_from_target()

    def set_flight_plan(self, plan):
        pass

    def update_flight_plan(self, plan):
        pass

    def abort_flight_plan(self):
        pass

    def get_flight_plan(self):
        pass

    def move(self, direction=1):
        """
        Return forward or backward disturbance for moving
        :param direction: 1 for forward, -1 for backward, 0 for stable
        :return:
        """
        pitch_disturbance = 2 * direction
        return pitch_disturbance

    def rotate(self, direction=1):
        """
        Return left or right disturbance for rotation
        :param direction: 1 for right, -1 for left, 0 for stable
        :return:
        """
        yaw_disturbance = 1.3 * direction

    def should_move_forward(self, target):
        pass

    def get_coordinates(self):
        gps = self.devices['gps']['device']
        return gps.getValues()

    def get_distance_from_target(self):
        coordinates = self.get_coordinates()
        distances = [abs(coordinates[0] - self.target[0]), abs(coordinates[2] - self.target[1])]
        return distances

    def target_has_reached(self):
        distance = [d // 1 for d in self.get_distance_from_target()]
        return not any(distance)

    def on_track(self):
        new_distance = self.get_distance_from_target()
        return all([self.prev_distance[0] > new_distance[0], self.prev_distance[1] > new_distance[1]])

    def get_input(self):
        """
        Input is based on if we are getting closer to the target
        In case we are on the target no input is given
        :return:
        """
        if self.target_has_reached():
            return 0, 0, 0
        if self.on_track():
            return 0, 2, 0

        return 0, 2, 0.5

        # # Transform the keyboard input to disturbances on the stabilization algorithm.
        # roll_disturbance = 0
        # pitch_disturbance = 2
        # yaw_disturbance = 0
        #
        # return roll_disturbance, pitch_disturbance, yaw_disturbance
