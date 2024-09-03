#!/usr/bin/env python3
"""Defines the Class Server"""

import csv
import math
from typing import List, Dict, Any

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get items from the dataset, paginated.

        Args:
        page (int): The page to get. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
        List[List]: A list of lists, where each sublist contains an item from
        the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        if start_index > len(dataset):
            return []
        return dataset[start_index:end_index]



    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        hypermedia: Dict[str, Any] = {
            "page_size": page_size,
            "page_number": page,
            "data": self.get_page(page, page_size),
            "next_page_number": None,
            "previous_page_number": None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }

        if page > 1:
            hypermedia["previous_page_number"] = page - 1

        if len(hypermedia["data"]) == page_size:
            hypermedia["next_page_number"] = page + 1

        return hypermedia
