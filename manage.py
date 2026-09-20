"""Utility script của Django để thực thi các câu lệnh CLI quản trị ứng dụng parking_management."""

#!/usr/bin/env python
import os
import sys
from pathlib import Path

def main():
    """Khởi tạo môi trường Django và thực thi các lệnh quản trị command line."""
    # Set cwd and path to parking_management
    pkg_dir = Path(__file__).resolve().parent / "parking_management"
    if pkg_dir.exists():
        sys.path.insert(0, str(pkg_dir))
        os.chdir(str(pkg_dir))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()
