import unittest
from selenium import webdriver
from pastebin_pages.paste_creation_page import PasteCreationPage
from pastebin_pages.paste_page import PastePage

# nosetests test_pastebin.py

class TestPastebin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        

    def test_i_can_win(self):
        # Parameters
        title = 'helloweb'
        text = 'Hello from WebDriver'
        # Open page
        paste_creation_page = PasteCreationPage(self.driver)
        paste_creation_page.open()
        # Set parameters
        paste_creation_page.set_text(text)
        paste_creation_page.set_expiration_time_10_minutes()
        paste_creation_page.set_title(title)
        # Click 'Create'
        paste_creation_page.create_paste()
        # Assert
        created_paste = PastePage(self.driver)
        created_title = created_paste.get_title()
        self.assertTrue(created_title == title)

    def test_bring_it_on(self):
        # Parameters
        title = 'how to gain dominance among developers'
        highlight = 'Bash'
        text = 'git config --global user.name  "New Sheriff in Town"\n'
        text += 'git reset $(git commit-tree HEAD^{tree} -m "Legacy code"\\m)\n'
        text += 'git push origin master --force'
        # Open page
        paste_creation_page = PasteCreationPage(self.driver)
        paste_creation_page.open()
        # Set parameters
        paste_creation_page.set_title(title)
        paste_creation_page.set_text(text)
        paste_creation_page.set_bash_highlight()
        paste_creation_page.set_expiration_time_10_minutes()
        # Click 'Create'
        paste_creation_page.create_paste()
        # Assert
        created_paste = PastePage(self.driver)
        created_title = created_paste.get_title()
        created_highlight = created_paste.get_highlight()
        created_text = created_paste.get_text()
        condition = created_title == title
        condition = condition and (created_highlight == highlight)
        condition = condition and (created_text == text)
        self.assertTrue(condition)
    
    def tearDown(self):
        self.driver.quit()