"""Zadanie 1 lista 4"""
import time


def time_decorator(method):
    """Dekorator liczacy czas wykonywanej funkcji"""

    def timer(*args, **kwargs):
        start_time = time.time()
        method_result = method(*args, **kwargs)
        end_time = time.time()

        print('%s  %2.4f ms' % \
              (method.__name__, (end_time - start_time) * 1000))
        return method_result

    return timer
