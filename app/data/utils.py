import os
from pathlib import Path
from random import randint


BASE_DIR = Path(__file__).resolve().parent.parent


def fill_dir_with_photos(fill_path: str, template_path: str, count: int):
    """ The function fills the directory with photos. """
    is_valid_params = [
        os.path.isdir(fill_path),
        os.path.isfile(template_path),
        isinstance(count, int)
    ]
    assert all(is_valid_params), 'Parameters is not valid.'

    fill_path_len = len(os.listdir(fill_path))
    need_add_files = count - fill_path_len

    # Image in bytes
    with open(template_path, 'rb') as photo_bytes:
        photo_bytes_data = photo_bytes.read()

    # Add missing photos
    for _ in range(need_add_files):
        new_file_name = f'{fill_path}/{randint(0, 1_000_000)}.jpeg'

        # Create new duplecate in fill_path
        with open(new_file_name, 'wb') as file:
            file.write(photo_bytes_data)
