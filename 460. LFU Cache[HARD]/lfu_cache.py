from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.key_to_freq = defaultdict(tuple)  # key -> (frequency, value)
        self.freq_to_key = defaultdict(OrderedDict)  # frequency -> OrderedDict(key -> None)
        self.min_freq = 0

    def _insert_key(self, key, freq, value):
        """Insert key into a specific frequency bucket."""
        self.key_to_freq[key] = (freq, value)
        self.freq_to_key[freq][key] = None

    def _increase_frequency(self, key):
        """Increase frequency of a key and move it to the next frequency bucket."""
        freq, value = self.key_to_freq[key]

        # Remove from current frequency bucket
        del self.freq_to_key[freq][key]

        # If this was the last key in the minimum frequency bucket, update min_frequency
        if freq == self.min_freq and not self.freq_to_key[freq]:
            self.min_freq += 1

        # Insert into next frequency bucket
        self._insert_key(key, freq + 1, value)
        return value

    def get(self, key: int) -> int:
        if key in self.key_to_freq:
            return self._increase_frequency(key)
        return -1

    def put(self, key: int, value: int) -> None:

        # If key exists → update value + bump frequency
        if key in self.key_to_freq:
            self._increase_frequency(key)
            freq, _ = self.key_to_freq[key]
            self.key_to_freq[key] = (freq, value)
            
        else:
            # Evict if at capacity
            if len(self.key_to_freq) == self.cap:
                evict_key, _ = self.freq_to_key[self.min_freq].popitem(last=False)
                del self.key_to_freq[evict_key]

            # We know with certainty that the new minimum frequency becomes 1 after inserting a new key.
            self.min_freq = 1
            self._insert_key(key, 1, value)
