import os

import requests


def download(url: str, folder_path: str) -> None:
    """Download file from url and save it locally under `file_path`"""
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, url.split("/")[-1])
    with open(file_path, "wb") as file:
        response = requests.get(url)
        file.write(response.content)
        print(f"Downloaded {url} to {file_path}.")


def main():
    url = "https://qbank.eppo.int/bacteria/taxon/XANTPH/specimens"
    folder = "data"
    download(url, folder)


main()
