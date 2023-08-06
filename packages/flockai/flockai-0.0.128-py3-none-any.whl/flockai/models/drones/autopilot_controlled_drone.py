import abc

from flockai.interfaces.drone import IDrone


class AutopilotControlledDrone(IDrone, abc.ABC):
    def __init__(self, devices):
        super().__init__(devices)

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

    def get_input(self):
        # Transform the keyboard input to disturbances on the stabilization algorithm.
        roll_disturbance = 0
        pitch_disturbance = 2
        yaw_disturbance = 0

        return roll_disturbance, pitch_disturbance, yaw_disturbance
