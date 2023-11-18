# revcolorsensor

This is a Python library that allows Raspberry Pi's to use the [REV Color Sensor](https://www.revrobotics.com/rev-31-1557/) without a Roborio/FRC project.

## Installation

```
pip3 install revcolorsensor
```

## pigpio

You will need to run the [`pigpio` daemon](https://abyz.me.uk/rpi/pigpio/) for this library to work.

Install with:

```
sudo apt-get install pigpiod
```

You can run this after booting up the Raspberry Pi:

```
sudo pigpiod
```

or, run this *once* and it will do it automatically on boot each time:

```
sudo systemctl enable pigpiod
```

## Resources

[API Docs](https://jasonli0616.github.io/revcolorsensor/revcolorsensor/)

[Examples](https://github.com/jasonli0616/revcolorsensor/tree/master/examples)

[Pypi](https://pypi.org/project/revcolorsensor/)