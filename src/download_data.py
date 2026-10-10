"""Download the official public IBM course datasets, checking file lengths."""
from pathlib import Path
from urllib.request import urlopen
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCES = {
    'survey-data-with-duplicate.csv': 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VYPrOu0Vs3I0hKLLjiPGrA/survey-data-with-duplicate.csv',
    'jobs.json': 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json',
    'Programming_Languages.html': 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html',
}


def download_all(directory=None):
    directory = Path(directory) if directory else ROOT / 'data' / 'raw'
    directory.mkdir(parents=True, exist_ok=True)
    for name, url in SOURCES.items():
        target = directory / name
        temporary = target.with_suffix(target.suffix + '.download')
        with urlopen(url, timeout=90) as response, temporary.open('wb') as output:
            expected = response.headers.get('Content-Length')
            shutil.copyfileobj(response, output, length=1024 * 1024)
        if expected and temporary.stat().st_size != int(expected):
            raise ValueError(f'Incomplete download: {name}')
        temporary.replace(target)
        print(f'Downloaded {name}: {target.stat().st_size:,} bytes')


if __name__ == '__main__':
    download_all()
