# qrpy

<p align="center">
    <img width="150" height="150" alt="A QR code"
    src="https://raw.githubusercontent.com/bradenhilton/qrpy/main/.assets/QR.png">
</p>

qrpy is a simple command-line program capable of encoding and decoding basic QR codes.

## Installation

```console
pip install qrpy
```

Note: You may need to additionally install zbar, as outlined in the
[installation steps](https://github.com/NaturalHistoryMuseum/pyzbar/tree/master#installation)
for pyzbar.

## Examples

```console
❯ qrpy encode --input "Hello world" --output "hello.png"
```

```console
❯ qrpy decode --input "hello.png"
Hello world
```

Omitting `--output` when encoding will print the QR code to the console.
