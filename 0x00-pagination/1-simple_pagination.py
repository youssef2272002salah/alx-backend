#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""

from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    Args:
        page (int): the current page

        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of the start and end index for the given page
    """
    nextPageStartIndex = page * page_size
    return (nextPageStartIndex - page_size, nextPageStartIndex)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get items for the given page number
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        startIndex, endIndex = index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
