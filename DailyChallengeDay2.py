class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.pageSize = int(pageSize)  # Ensure the pageSize is an integer
        self.totalItems = len(self.items)
        self.totalPages = (self.totalItems // self.pageSize) + (1 if self.totalItems % self.pageSize > 0 else 0)
        self.currentPage = 1

    def getVisibleItems(self):
        """Returns the list of items visible on the current page."""
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def prevPage(self):
        """Moves to the previous page."""
        self.currentPage = max(1, self.currentPage - 1)  # Ensure we don't go below page 1
        return self

    def nextPage(self):
        """Moves to the next page."""
        self.currentPage = min(self.totalPages, self.currentPage + 1)  # Ensure we don't exceed the total pages
        return self

    def firstPage(self):
        """Moves to the first page."""
        self.currentPage = 1
        return self

    def lastPage(self):
        """Moves to the last page."""
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        """Moves to a specific page number."""
        pageNum = int(pageNum)  # Ensure the page number is an integer
        self.currentPage = max(1, min(pageNum, self.totalPages))  # Ensure it's within the valid range
        return self

# Example usage:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

# Display the current page items
print(p.getVisibleItems())  # ["a", "b", "c", "d"]

# Navigate through the pages
p.nextPage()
print(p.getVisibleItems())  # ["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]

p.firstPage()
print(p.getVisibleItems())  # ["a", "b", "c", "d"]

p.goToPage(2)
print(p.getVisibleItems())  # ["e", "f", "g", "h"]