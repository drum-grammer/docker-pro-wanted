import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):
    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")


OCR_API_URL = get_secret("OCR_API_URL")
OCR_SECRET_KEY = get_secret("OCR_SECRET_KEY")


if __name__ == "__main__":
    print(OCR_API_URL)
    print(OCR_SECRET_KEY)