import time
from picarx_improved import Picarx

# marcus@picar14.engr.oregonstate.edu

def forward_to_backward(speed, steering_angle, action_time=1):
    """ Forward and Backward
    """
    movement = Picarx()
    movement.set_wheel_vel_scale(steering_angle)
    movement.set_dir_servo_angle(0)

    # Step 1: Forward with steering
    movement.set_dir_servo_angle(steering_angle)
    movement.forward(speed)
    time.sleep(action_time)
    movement.stop()

    # Step 2: Backward with steering
    movement.set_dir_servo_angle(steering_angle)
    movement.backward(speed)
    time.sleep(action_time)
    movement.stop()

    # Step 3: Reset car values
    movement.set_dir_servo_angle(0)


def parallel_park(speed, steering_angle):
    """Parallel Parking
    """
    movement = Picarx()
    movement.set_wheel_vel_scale(steering_angle)
    movement.set_dir_servo_angle(0)

    # Step 1: pull up moving forward
    movement.forward(speed)
    time.sleep(1)
    movement.stop()

    # Step 2: turn towards curb, then move backward
    movement.set_dir_servo_angle(steering_angle)
    movement.backward(speed)
    time.sleep(0.5)
    # movement.stop()

    # Step 3: straighten out, continue backward
    movement.set_dir_servo_angle(0)
    movement.backward(speed)
    time.sleep(0.5)
    # movement.stop()

    # Step 4: turn away from curb, continue backward
    movement.set_dir_servo_angle(-steering_angle)
    movement.backward(speed)
    time.sleep(0.5)
    movement.stop()

    # Step 5:
    movement.set_dir_servo_angle(0)
    movement.forward(speed)
    time.sleep(0.5)
    movement.stop()


def k_turn(speed, steering_angle):
    """Three point turn
    """
    movement = Picarx()
    movement.set_wheel_vel_scale(steering_angle)
    movement.set_dir_servo_angle(0)

    # Step 1: turn and move forward
    movement.set_dir_servo_angle(steering_angle)
    movement.forward(speed)
    time.sleep(1)
    movement.stop()

    # Step 2: turn opposite dir and backup
    movement.set_dir_servo_angle(-steering_angle)
    movement.backward(speed)
    time.sleep(1)
    movement.stop()

    # Step 3: turn opposite dir and go forward
    movement.set_dir_servo_angle(steering_angle)
    movement.forward(speed)
    time.sleep(1)
    movement.set_dir_servo_angle(0)
    movement.stop()


if __name__ == "__main__":
    # forward_to_backward(30, 0, 2)
    pass

