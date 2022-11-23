from typing import List


def print_pages(
    current_page: int, total_pages: int, boundaries: int, around: int
) -> None:
    page_collection: List[int] = []
    for value in range(boundaries):
        initial_page = 1
        last_page = total_pages

        page_to_add = initial_page + value
        if page_to_add not in page_collection:
            page_collection.append(page_to_add)

        page_to_add = last_page - value
        if page_to_add not in page_collection:
            page_collection.append(page_to_add)

    for value in range(around + 1):
        page_to_add = current_page - value
        if page_to_add not in page_collection:
            page_collection.append(page_to_add)
        page_to_add = current_page + value
        if page_to_add not in page_collection:
            page_collection.append(page_to_add)

    if current_page not in page_collection:
        page_collection.append(current_page)

    page_collection.sort()
    to_print = ""
    for count, value in enumerate(page_collection):
        if count < len(page_collection) - 1 and page_collection[count + 1] - value > 1:
            to_print += f"{value} ... "
        else:
            to_print += f"{value} "
    print(to_print)


if __name__ == "__main__":
    print_pages(current_page=4, total_pages=5, boundaries=1, around=0)
    print_pages(current_page=4, total_pages=10, boundaries=2, around=2)
