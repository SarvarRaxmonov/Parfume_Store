import uuid


def generate_device_id():
    device_id = uuid.uuid4()
    device_id_str = str(device_id).replace("-", "")

    return device_id_str
