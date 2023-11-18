from .colorsensor import ColorSensorV3

def getColorSensor():
    """
    Get a color sensor on I2C port 1.

    Alternatively, create your own ColorSensorV3 object.
    You will most likely use the `getColor()` and `getProximity()` functions on this object.

    GitHub repo: https://github.com/jasonli0616/revcolorsensor
    """
    return ColorSensorV3(1)
