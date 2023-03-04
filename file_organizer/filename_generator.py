import os.path
import re
from datetime import datetime

import uuid


def generate_new_filename(filename: str) -> str:
    file, ext = os.path.splitext(os.path.basename(filename))
    if not file:
        return f'{now():%Y-%m-%d}_{uuid.uuid4()}{ext}'.lower()

    file = re.sub(r'\s', '-', file)
    return f'{now():%Y-%m-%d}_{file}_{uuid.uuid4()}{ext}'.lower()


def now() -> datetime.date:
    return datetime.now()
