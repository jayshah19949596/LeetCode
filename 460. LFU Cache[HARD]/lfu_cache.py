from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_freq = defaultdict(int)  # key -> (frequency, value)
        self.freq_to_key = defaultdict(OrderedDict)  # frequency -> OrderedDict(key -> None)
        self.min_freq = 0

    def _insert(self, key, frequency, value):
        """Insert key into a specific frequency bucket."""
        self.key_to_freq[key] = (frequency, value)
        self.freq_to_key[frequency][key] = None

    def _increase_frequency(self, key):
        """Increase frequency of a key and move it to the next frequency bucket."""
        frequency, value = self.key_to_freq[key]

        # Remove from current frequency bucket
        del self.freq_to_key[frequency][key]

        # If this was the last key in the minimum frequency bucket, update min_frequency
        if frequency == self.min_freq and not self.freq_to_key[frequency]:
            self.min_freq += 1

        # Insert into next frequency bucket
        self._insert(key, frequency + 1, value)
        return value

    def get(self, key: int) -> int:
        if key in self.key_to_freq:
            return self._increase_frequency(key)
        return -1

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        # If key exists → update value + bump frequency
        if key in self.key_to_freq:
            self._increase_frequency(key)
            frequency, _ = self.key_to_freq[key]
            self.key_to_freq[key] = (frequency, value)
            return

        # Evict if at capacity
        if len(self.key_to_freq) == self.capacity:
            evict_key, _ = self.freq_to_key[self.min_freq].popitem(last=False)
            del self.key_to_freq[evict_key]

        # Insert new key with frequency 1
        self.min_freq = 1
        self._insert(key, 1, value)
