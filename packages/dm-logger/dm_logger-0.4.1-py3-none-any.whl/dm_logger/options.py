from typing import Literal


class Options:
    logs_dir_path: str = "logs"
    file_name: str = "main.log"
    write_mode: Literal["a", "w"] = "w"
    max_MB: int = 5
    max_count: int = 10
    show_name_label: bool = False
    show_place_label: bool = False
    format_string: str = None
