


current_system_state = "ok"


def calculate_current_robot_state(visual_input: str, detected_threats: bool):
    """
    Also uses and sets the currect_system_state, as it effects the next state
    :param visual_input: The visual input of the robot
    :param detected_threats: Whether threats were detected using the visual input
    """
    global current_system_state
    if visual_input == "danger" and detected_threats and current_system_state == "ok":
        current_system_state = "warning"
    if visual_input == "ok" and detected_threats == True and current_system_state == "ok":
        current_system_state = "warning"
    if visual_input == "danger" and detected_threats == False and current_system_state == "ok":
        current_system_state = "warning"
    if visual_input == "danger" and detected_threats == False and current_system_state == "ok":
        current_system_state = "warning"
    if visual_input == "ok" and detected_threats == False and current_system_state == "warning":
        current_system_state = "ok"
    if visual_input == "danger" and detected_threats == False and current_system_state == "warning":
        current_system_state = "ok"
    if visual_input == "ok" and detected_threats == True and current_system_state == "warning":
        current_system_state = "error"
    if visual_input == "danger" and detected_threats == True and current_system_state == "warning":
        current_system_state = "error"
    if visual_input == "ok" and detected_threats == False and current_system_state == "error":
        current_system_state = "warning"
    if visual_input == "danger" and detected_threats == False and current_system_state == "error":
        current_system_state = "error"
    if visual_input == "ok" and detected_threats == True and current_system_state == "error":
        current_system_state = "error"
    if visual_input == "danger" and detected_threats == True and current_system_state == "error":
        current_system_state = "down"


calculate_current_robot_state("danger", False)
calculate_current_robot_state("danger", True)
calculate_current_robot_state("ok", True)
calculate_current_robot_state("ok", False)
calculate_current_robot_state("ok", True)
calculate_current_robot_state("ok", False)
calculate_current_robot_state("danger", True)
calculate_current_robot_state("danger", True)
calculate_current_robot_state("danger", True)
print(current_system_state)
