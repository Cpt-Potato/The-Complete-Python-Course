import re
import logging
from bs4 import BeautifulSoup

from locators.books_page_locators import BooksPageLocators
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BooksPageLocators.BOOK}`.')
        book_tags = self.soup.select(BooksPageLocators.BOOK)
        return [BookParser(e) for e in book_tags]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(BooksPageLocators.NUMBER_OF_PAGES).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')
        matcher = re.search('Page [0-9]+ of ([0-9]+)', content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer: `{pages}`.')
        return pages
