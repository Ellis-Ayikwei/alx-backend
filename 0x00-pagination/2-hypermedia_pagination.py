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

    def get_hyper(self, page_number: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get paginated data with hypermedia metadata.

        Args:
        page_number (int): The page to get. Defaults to 1.
        page_size (int): The number of items per page. Defaults to 10.

        Returns:
        Dict[str, Any]: A dictionary containing the paginated data and metadata.
        """
        if page_size <= 0:
            return {
                "page_size": 0,
                "page": page_number,
                "data": [],
                "next_page": None,
                "prev_page": page_number - 1 if page_number > 1 else None,
                "total_pages": 0,
            }

        data = self.get_page(page_number, page_size)
        total_items = len(self.dataset())
        total_pages =math.ceil(total_items / page_size)

        next_page = page_number + 1 if page_number < total_pages else None
        prev_page = page_number - 1 if page_number > 1 else None

        return {
            "page_size": len(data),
            "page": page_number,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
