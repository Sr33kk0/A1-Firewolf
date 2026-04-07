
PRIORITY_HIGH = 1
PRIORITY_LOW = 0

DOWNLOAD_TIMEOUT_SECONDS = 3
DOWNLOAD_MAX_ATTEMPTS = 3


def get_current_time():
    """
    You may assume the time complexity of this method is always O(1).
    """
    from time import time
    return int(time()) - 1769930097


class DownloadManager:
    def __init__(self):
        pass
    
    def download_requested(self, address, good_for: int, priority: int):
        pass
        
    def get_next_download(self):
        pass
    
    def download_completed(self, identifier):
        pass

    def get_median_delay(self) -> float:
        pass


if __name__ == "__main__":
    """
    Write tests for your code here...
    """
    from time import sleep

    dm = DownloadManager()
    
    dm.download_requested("https://example.com/file1", 10, PRIORITY_LOW)
    dm.download_requested("https://example.com/file2", 10, PRIORITY_HIGH)

    # First download should be the high priority one, so a tuple of (id, "https://example.com/file2") is expected
    first_download = dm.get_next_download()
    assert first_download[1] == "https://example.com/file2"

    # If we wait a few seconds without acknowledging the first download as completed, it means it's timed out
    sleep(5)

    # Asking for the next download should give us the same high priority download again
    second_download = dm.get_next_download()
    assert second_download[1] == "https://example.com/file2"
