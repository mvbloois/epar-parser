import requests
from config import DOWNLOAD_URL, OUTPUT_PATH

class DownloadManager:
    @staticmethod
    def download_file(url=DOWNLOAD_URL, output_path=OUTPUT_PATH):
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
