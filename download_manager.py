from data_structures.array_list import ArrayList
from data_structures.array_sorted_list import ArraySortedList
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
    def __init__(self, id, address, current_time, good_for: int, priority: int):
        self.id = id
        self.address = address
        self.expiry_time = get_current_time() + good_for
        self.priority = priority
        self.attempt = 0
        self.completed = False
        self.last_attempt_time = 0
        self.start_time = current_time
        self.delay = 0

class DownloadManager:
    def __init__(self):
        self.all_files = ArrayList()
        self.high_priority = LinkedQueue()
        self.low_priority = LinkedQueue()
        self.active_downloads = LinkedQueue()
        self.delays = ArraySortedList()

    def download_requested(self, address, good_for: int, priority: int):
        current_time = get_current_time()
        id = len(self.all_files)
        file = File(id, address, current_time, good_for, priority)
        self.all_files.append(file)

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

            elif current_time - file.last_attempt_time >= DOWNLOAD_TIMEOUT_SECONDS:
                self.active_downloads.serve()
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)

                new_delay = current_time - file.start_time
                self.delays.remove(file.delay)
                self.delays.add(new_delay)
                file.delay = new_delay

                return (file.id, file.address)
            
            else:
                break

        while not self.high_priority.is_empty():
            file = self.high_priority.serve()

            if current_time <= file.expiry_time:
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)

                new_delay = current_time - file.start_time
                self.delays.add(new_delay)
                file.delay = new_delay

                return (file.id, file.address)

        while not self.low_priority.is_empty():
            file = self.low_priority.serve()

            if current_time <= file.expiry_time:
                file.attempt += 1
                file.last_attempt_time = current_time
                self.active_downloads.append(file)

                new_delay = current_time - file.start_time
                self.delays.add(new_delay)
                file.delay = new_delay

                return (file.id, file.address)

        return (None, None)
    
    def download_completed(self, identifier):
        file = self.all_files[identifier]
        file.completed = True

    def get_median_delay(self) -> float:
        n = len(self.delays)

        if n == 0:
            return 0
        
        mid = n // 2

        if n % 2 != 0:
            return self.delays[mid]
        else:
            return (self.delays[mid] + self.delays[mid - 1]) / 2

if __name__ == "__main__":
    """
    Write tests for your code here...
    """
    from time import sleep

    dm = DownloadManager()
    
    dm.download_requested("1high", 10, PRIORITY_HIGH)
    dm.download_requested("2high", 10, PRIORITY_HIGH)
    dm.download_requested("1low", 10, PRIORITY_LOW)

    # First download should be the high priority one, so a tuple of (id, "https://example.com/file2") is expected
    first_download = dm.get_next_download()
    print(first_download)
    assert first_download[1] == "1high"
    second_download = dm.get_next_download()
    print(second_download)
    assert second_download[1] == "2high"
    third_download = dm.get_next_download()
    print(third_download)
    assert third_download[1] == "1low"
    fourth_download = dm.get_next_download()
    print(fourth_download)

    # If we wait a few seconds without acknowledging the first download as completed, it means it's timed out
    sleep(3)

    # Asking for the next download should give us the same high priority download again
    fifth_download = dm.get_next_download()
    print(fifth_download)

    dm.download_completed(2)
    # sleep(5)
    sixth_download = dm.get_next_download()
    print(sixth_download)
    print(dm.delays)
