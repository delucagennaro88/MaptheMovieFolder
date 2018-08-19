def bytes_converter(bytes):
    if bytes < 0:
        raise ValueError("!!! bytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024

    bytes = float(bytes)
    unit = 'bytes'

    if (bytes / step_to_greater_unit) >= 1:
        bytes /= step_to_greater_unit
        unit = 'KB'

    if (bytes / step_to_greater_unit) >= 1:
        bytes /= step_to_greater_unit
        unit = 'MB'

    if (bytes / step_to_greater_unit) >= 1:
        bytes /= step_to_greater_unit
        unit = 'GB'

    if (bytes / step_to_greater_unit) >= 1:
        bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    bytes = round(bytes, precision)

    return str(bytes) + ' ' + unit