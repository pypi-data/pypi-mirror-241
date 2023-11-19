from __future__ import annotations

import argparse
from importlib.metadata import version
from pathlib import Path

from qrpy.decoder import decode_qr
from qrpy.encoder import encode_qr


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qrpy",
        description="QR Code Encoder and Decoder",
    )

    parser.add_argument(
        "--version",
        action="version",
        version=version("qrpy"),
        help="print program version and exit",
    )

    subparsers = parser.add_subparsers(dest="command")

    encode_parser = subparsers.add_parser("encode", help="encode help")
    encode_parser.add_argument(
        "-i",
        "--input",
        help="data to encode into a QR code",
        metavar="DATA",
        dest="input_data",
    )
    encode_parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="path to save the encoded QR code to",
        metavar="PATH",
        dest="output_path",
    )
    encode_parser.add_argument(
        "-y",
        "--overwrite",
        action="store_true",
        default=False,
        help="overwrite the existing file at output path",
        dest="overwrite",
    )

    decode_parser = subparsers.add_parser("decode", help="decode help")
    decode_parser.add_argument(
        "-i",
        "--input",
        type=Path,
        help="path to a QR image file",
        metavar="PATH",
        dest="input_path",
    )
    return parser


def main() -> None:
    try:
        parser = create_parser()
        args = parser.parse_args()

        if args.command == "encode":
            if (
                args.output_path
                and args.output_path.exists()
                and not args.overwrite
            ):
                response = input(
                    f"'{args.output_path.name}' already exists. "
                    f"Overwrite '{args.output_path.name}' (y/n)? ",
                )
                if response.lower().strip() != "y":
                    return
            encode_qr(args.input_data, args.output_path)
        elif args.command == "decode":
            decode_qr(args.input_path)
    except KeyboardInterrupt:
        raise SystemExit("\nKeyboardInterrupt") from None
