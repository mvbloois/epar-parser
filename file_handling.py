import os
import glob

class FileHandler:
    @static_method
    def get_sorted_csv_files(directory):
    """
    Retrieve a list of CSV files in a directory sorted by modification time.

    :param directory: Path to the directory where CSV files are located
    :return: A list of file paths sorted by modification time (newest first)
    """
    try:
        directory = Path(directory)
        csv_files = list(directory.glob('*.csv'))
        if not csv_files:
            return []
        csv_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
        return csv_files
    except Exception as e:
        return []

@static_method
def find_newest_csv(directory):
    """
    Find the newest CSV file in the specified directory.

    :param directory: Path to the directory where CSV files are located
    :return: The path to the newest CSV file or None if no CSV files are found
    """
    csv_files = get_sorted_csv_files(directory)
    return csv_files[0] if csv_files else None

@static_method
def find_second_newest_csv(directory):
    """
    Find the second newest CSV file in the specified directory.

    :param directory: Path to the directory where CSV files are located
    :return: The path to the second newest CSV file or None if fewer than two CSV files are found
    """
    csv_files = get_sorted_csv_files(directory)
    return csv_files[1] if len(csv_files) > 1 else None
