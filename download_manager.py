from data_structures.array_list import ArrayList
from data_structures.linked_queue import LinkedQueue

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

class File:
    def __init__(self, id, address, good_for: int, priority: int):
        self.id = id
        self.address = address
        self.expiry_time = get_current_time() + good_for
        self.priority = priority
        self.attempt = 0
        self.completed = False
        self.last_attempt_time = 0

class DownloadManager:
    def __init__(self):
        self.all_file = ArrayList()
        self.high_priority = LinkedQueue()
        self.low_priority = LinkedQueue()
        self.active_downloads = LinkedQueue()

    def download_requested(self, address, good_for: int, priority: int):
        id = len(self.all_file)
        file = File(id, address, good_for, priority)
        self.all_file.append(file)

        if priority == PRIORITY_HIGH:
            self.high_priority.append(file)
        else:
            self.low_priority.append(file)
        
    def get_next_download(self):
        current_time = get_current_time()

        while not self.active_downloads.is_empty():
            file = self.active_downloads.peek()

            if file.completed:
                self.active_downloads.serve()

            elif current_time > file.expiry_time or file.attempt >= DOWNLOAD_MAX_ATTEMPTS:
                self.active_downloads.serve()

            elif current_time - file.last_attempt_time > DOWNLOAD_TIMEOUT_SECONDS:
                self.active_downloads.serve()
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)

                return (file.id, file.address)
            
            else:
                break

        while not self.high_priority.is_empty():
            file = self.high_priority.serve()

            if current_time <= file.expiry_time:
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)

                return (file.id, file.address)

        while not self.low_priority.is_empty():
            file = self.low_priority.serve()

            if current_time <= file.expiry_time:
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)
                return (file.id, file.address)

        return (None, None)
    
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
    print(first_download)
    assert first_download[1] == "https://example.com/file2"

    # If we wait a few seconds without acknowledging the first download as completed, it means it's timed out
    sleep(5)

    # Asking for the next download should give us the same high priority download again
    second_download = dm.get_next_download()
    print(second_download)
    assert second_download[1] == "https://example.com/file2"
