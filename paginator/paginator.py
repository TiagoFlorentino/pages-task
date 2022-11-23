from typing import List


class Paginator:

    current_page: int = 0
    total_pages: int = 0
    boundaries: int = 0
    around: int = 0

    def __init__(
        self, current_page: int, total_pages: int, boundaries: int, around: int
    ):
        self.current_page = current_page
        self.total_pages = total_pages
        self.boundaries = boundaries
        self.around = around

    @staticmethod
    def is_positive(value: int):
        return value > 0

    def get_boundary_pages(self) -> List[int]:
        page_collection = []

        # Assumes the first page is always 1
        first_page = 1
        for value in range(self.boundaries):
            # Add values to the right of the first page given the boundaries
            page_to_add = first_page + value
            if self.is_positive(page_to_add):
                page_collection.append(page_to_add)

            # Add values to the left of the last page given the boundaries
            page_to_add = self.total_pages - value
            if self.is_positive(page_to_add):
                page_collection.append(page_to_add)
        return page_collection

    def get_current_boundary_pages(self) -> List[int]:
        page_collection = []
        for value in range(self.around + 1):
            # Add values to the left of the current page
            page_to_add = self.current_page - value
            if self.is_positive(page_to_add):
                page_collection.append(page_to_add)

            # Add values to the right of the current page
            page_to_add = self.current_page + value
            if self.is_positive(page_to_add):
                page_collection.append(page_to_add)

        if self.is_positive(self.current_page):
            page_collection.append(self.current_page)
        return page_collection

    def print_paginator(self) -> None:
        page_collection = self.get_boundary_pages() + self.get_current_boundary_pages()
        unique_page_collection: List[int] = [*set(page_collection)]

        to_print: str = ""
        for count, value in enumerate(unique_page_collection):
            if (
                count < len(unique_page_collection) - 1
                and unique_page_collection[count + 1] - value > 1
            ):
                to_print += f"{value} ... "
            else:
                to_print += f"{value} "

        print(to_print) if to_print else print("No results to print!")
