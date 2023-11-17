#!/usr/bin/env python
# coding: utf-8

import base64
import os
from typing import Dict, Any, List  # noqa: F401
import subprocess
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from xrpl.core.binarycodec.main import decode
from xrpld_publisher.utils import (
    read_json,
    read_txt,
    from_date_to_effective,
    from_days_to_expiration,
)
from xrpld_publisher.models import Validator, VL, Blob


class PublisherClient(object):
    vl_path: str = ""
    vl: VL = None

    def __init__(cls, manifest: str = None, vl_path: str = None) -> None:
        if vl_path:
            try:
                cls.vl_path = vl_path
                vl_dict: Dict[str, Any] = read_json(vl_path)
                cls.vl = VL.from_json(vl_dict)
                cls.vl.blob.sequence += 1
                pass
            except Exception as e:
                raise e

        if manifest:
            cls.vl_path: str = "vl.json"
            cls.vl = VL()
            cls.vl.manifest = manifest
            cls.vl.blob = Blob()
            cls.vl.blob.sequence = 1
            pass

    def add_validator(cls, manifest: str):
        if not cls.vl:
            raise ValueError("invalid vl")

        if not cls.vl.blob:
            raise ValueError("invalid blob")

        encoded = base64.b64decode(manifest).hex()
        decoded: Dict[str, Any] = decode(encoded)
        public_key: str = decoded["PublicKey"].upper()
        # Check if the validator is already in the list
        for validator in cls.vl.blob.validators:
            if validator.pk == public_key:
                raise ValueError("Validator is already in the list")

        new_validator: Validator = Validator()
        new_validator.pk = public_key
        new_validator.manifest = manifest
        cls.vl.blob.validators.append(new_validator)

    def remove_validator(cls, public_key: str):
        if not cls.vl:
            raise ValueError("invalid VL")

        if not cls.vl.blob:
            raise ValueError("invalid Blob")

        validators = cls.vl.blob.validators
        # Find the validator with the specified public key
        for validator in validators:
            if validator.pk == public_key:
                validators.remove(validator)
                break
        else:
            raise ValueError("validator not found")

        cls.vl.blob.validators = validators

    def sign_unl(
        cls, pk: int, path: str, effective: str = None, expiration: int = None
    ):
        if not cls.vl:
            raise ValueError("invalid vl")

        if len(cls.vl.blob.validators) == 0:
            raise ValueError("must have at least 1 validator")

        if not effective:
            effective: int = from_date_to_effective("01/01/2000")

        if not expiration:
            expiration: int = from_days_to_expiration(time.time(), 30)

        out = open(path, "w")
        vl_manifests: List[str] = [v.manifest for v in cls.vl.blob.validators]
        args = [
            os.getenv("BIN_PATH"),
            "sign",
            "--private_key",
            pk,
            "--sequence",
            str(cls.vl.blob.sequence),
            "--expiration",
            str(expiration),
            "--manifest",
            cls.vl.manifest,
            "--manifests",
            ",".join(vl_manifests),
        ]
        subprocess.call(args, stdout=out)
        return read_txt(path)
