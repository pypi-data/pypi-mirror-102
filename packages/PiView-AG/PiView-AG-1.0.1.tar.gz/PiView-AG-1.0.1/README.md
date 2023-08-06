# PiView

A Raspberry Pi system information package.

![PiView Icon](PiView-0.25x.png)

PiView provides the details of the Raspberry Pi currently being interrogated. System information includes, but is not limited to:

- **CPU**: max load across cores, temperature, clock speed
- **GPU**: temperature
- **HARDWARE**: bluetooth, i2c, spi, camera statuses
- **HOST**: boot time, model, name, revision, serial number, uptime
- **NETWORK**: host name, interface names, ip addresses, mac addresses
- **STORAGE**: total disk capacity, free disk capacity, total RAM and free RAM

Also includes a small utility library with:

- conversion of bytes into Kilobytes, Megabytes, Gigabytes and up
- create list with a quartet of integer numbers representing the IPv4 Address

## Changes

See the [CHANGES](CHANGES.md) document for details of updates and changes.

## Requirements

This project requires a number of packages, including:

- psutils

Remaining packages are Python 'built-ins'.

## Usage

to be added...


## Acknowledgements

A very large thank you to Matt Hawkins upon whose code this package is based: [https://www.raspberrypi-spy.co.uk/](https://www.raspberrypi-spy.co.uk/).

The original code may be found as [mypi.py](https://github.com/tdamdouni/Raspberry-Pi-DIY-Projects/blob/master/MattHawkinsUK-rpispy-misc/python/mypi.py).

Thank you to Sander Huijsen for his contributions and guidance in all things Python.

## About the Author

Adrian Gould has been coding for over 40 years, starting his coding in Sinclair ZX-80 Basic and Machine Code, through Pascal, Modula-2, Occam, Prolog and many others to the current swathe of Python, C#, PHP, JS, and other languages today.

He believes that it is a continuous process to learn any (coding) language, and will always say he is not an expert.

He is a full time educator who lives and works in Perth, Western Australia.

## Copyright

Copyright Adrian Gould, 2021-. Licensed under
the [Open Software License version 3.0](./LICENSE.txt)
