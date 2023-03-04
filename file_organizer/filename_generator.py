import os.path
import re
from datetime import datetime

import uuid


def generate_new_filename(filename: str) -> str:
    date = now()
    guid = uuid.uuid4()
    file, ext = os.path.splitext(os.path.basename(filename))
    if not file:
        return f'{date:%Y-%m-%d}_{guid}{ext}'.lower()

    file = re.sub(r'\s', '-', file)
    return f'{date:%Y-%m-%d}_{file}_{guid}{ext}'.lower()


def now() -> datetime.date:
    return datetime.now()
