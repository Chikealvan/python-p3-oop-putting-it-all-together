#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return "Book checked out successfully"
        else:
            return "Book is already checked out"

    def check_in(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return "Book checked in successfully"
        else:
            return "Book is not checked out"

    def is_available(self):
        return not self.is_checked_out

        