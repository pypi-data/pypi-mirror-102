# Vector - Python SDK

## Production, EscapePod and OSKR robots supported!

This is a fork of the original Anki Vector Python SDK. 
I have started this fork as an unofficial version to keep things running.

![Vector](docs/source/images/vector-sdk-alpha.jpg)

Learn more about Vector: https://www.anki.com/en-us/vector

Learn more about how Vector works: [Vector Bible](https://github.com/GooeyChickenman/victor/blob/master/documentation/Vector-TRM.pdf)

Learn more about the SDK: https://developer.anki.com/

SDK documentation: https://developer.anki.com/vector/docs/index.html

Forums: https://forums.anki.com/


## Getting Started

You can follow steps [here](https://developer.anki.com/vector/docs/index.html) to set up your Vector robot with the SDK.

### Install

To install his SDK fork run:

```
pip uninstall anki_vector
pip uninstall ikkez_vector
pip install cyb3r_vector_sdk
```

Upgrade with 
```
pip install cyb3r_vector_sdk --upgrade
```

### SDK Configuration

To condigure the SDK with **Prod**, or **Prod+OSKR** robot, run:

```
py -m anki_vector.configure
```

To condigure the SDK with **EscapePod**, or **EP+OSKR** robot, run:

```
py -m anki_vector.configure_pod
```

### Escape Pod usage

You can either use the ```anki_vector.configure_pod``` in order to save your authentication into the sdk_config.ini file, and use all the examples and your programs and as you have them, or you can use the Robot object with setting the escape_pod parameter to True, and passing the robot's ip address:

```
    with anki_vector.Robot(ip="192.168.0.148", escape_pod=True) as robot:
        robot.behavior.say_text("Hello Escape Pod")
```

### Documentation

You can generate a local copy of the SDK documetation by
following the instructions in the `docs` folder of this project.


## Privacy Policy and Terms and Conditions

Use of Vector and the Vector SDK is subject to Anki's [Privacy Policy](https://www.anki.com/en-us/company/privacy) and [Terms and Conditions](https://www.anki.com/en-us/company/terms-and-conditions).
