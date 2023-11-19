from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyzbar.pyzbar import Decoded

from pathlib import Path
from PIL import Image
from pyzbar.pyzbar import decode as pyzbar_decode


def decode_qr(image_path: Path) -> None:
    image = Image.open(image_path)

    decoded_objects: list[Decoded] = pyzbar_decode(image)

    for obj in decoded_objects:
        print(obj.data.decode("utf-8"))
