#!/usr/bin/env python3
"""Defines the Class Server"""

import csv
import math
from typing import List

index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page_number: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items from the dataset, paginated.

        Args:
        page_number (int): The page to get. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
        List[List]: A list of lists, where each sublist contains an item from
        the dataset.
        """
        assert isinstance(page_number, int) and page_number > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page_number, page_size)
        return self.dataset()[start_index:end_index]
