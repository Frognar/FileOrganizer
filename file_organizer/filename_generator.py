import os.path
import re
from datetime import datetime

import uuid


def generate_new_filename(filename: str) -> str:
    file, ext = os.path.splitext(os.path.basename(filename))
    if not file:
        return f'{now():%Y-%m-%d}_{generate_identifier()}{ext}'.lower()

    file = re.sub(r'\s', '-', file)
    return f'{now():%Y-%m-%d}_{file}_{generate_identifier()}{ext}'.lower()


def now() -> datetime.date:
    return datetime.now()


def generate_identifier() -> str:
    return str(uuid.uuid4())
