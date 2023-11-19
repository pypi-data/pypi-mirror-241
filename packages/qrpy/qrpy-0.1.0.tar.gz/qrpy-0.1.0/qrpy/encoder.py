from __future__ import annotations

from pathlib import Path
import qrcode


def encode_qr(data: str, save_path: Path | None = None) -> None:
    qr = qrcode.QRCode()
    qr.add_data(data)
    qr.make()

    if save_path:
        qr_image = qr.make_image()
        qr_image.save(save_path)
    else:
        qr.print_tty()
