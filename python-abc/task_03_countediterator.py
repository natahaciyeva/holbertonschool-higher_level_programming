#!/usr/bin/env python3

class CountedIterator:
    """Iterator that keeps track of how many items have been iterated."""

    def __init__(self, iterable):
        # Orijinal iteratoru saxlayırıq
        self.iterator = iter(iterable)
        # Sayğac (neçə element alınıb)
        self.count = 0

    def __next__(self):
        # Növbəti elementi əldə etməyə çalışırıq
        item = next(self.iterator)  # StopIteration təbii şəkildə burada baş verir
        # Hər dəfə element alındıqda say artır
        self.count += 1
        return item

    def get_count(self):
        """İndiyə qədər neçə element oxunduğunu qaytarır"""
        return self.count
