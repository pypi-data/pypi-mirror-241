from colorsensor import ColorSensorV3

def get_color_sensor():
    """
    Get a color sensor on I2C port 1.
    
    Alternatively, create your own ColorSensorV3 object.
    """
    return ColorSensorV3(1)
