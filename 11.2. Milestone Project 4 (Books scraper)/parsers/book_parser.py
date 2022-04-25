import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page (or part of it)
    and find properties of an item in it.
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return '<Book "{}", £{} ({} {})>'.format(self.name, self.price, self.rating, 'star' if self.rating == 1 else 'stars')

    @property
    def name(self):
        logger.debug('Finding book name...')
        return self.parent.select_one(BookLocators.NAME).attrs['title']

    @property
    def price(self):
        logger.debug('Finding book price...')
        book_price = self.parent.select_one(BookLocators.PRICE).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, book_price)
        return float(matcher.group(1))

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        book_rating = self.parent.select_one(BookLocators.RATING).attrs['class']
        rating_classes = [r for r in book_rating if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        return rating_number
