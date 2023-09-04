class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count
        self.current_page = 1  # Initialize the current page to 1

    def set_page_count(self, page_count):
        if isinstance(page_count, int) and page_count >= 0:
            self._page_count = page_count
        else:
            print("Page count must be a non-negative integer")

    def get_page_count(self):
        return self._page_count

    page_count = property(get_page_count, set_page_count)

    def turn_page(self, num_pages=1):
        if self.current_page + num_pages <= self._page_count:
            self.current_page += num_pages
            print(f"Turning {num_pages} pages...current page: {self.current_page}")
        else:
            print("You've reached the end of the book!")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Total Page Count: {self.page_count}")
        print(f"Current Page: {self.current_page}")

# Example usage:
book1 = Book("Sample Book", 100)
book1.display_info()

book1.turn_page()  # Turn one page
book1.display_info()

book1.turn_page(5)  # Turn five more pages
book1.display_info()

book1.turn_page(50)  # Try to turn 50 pages, which exceeds the page count
book1.display_info()
