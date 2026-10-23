from sudoku import Sudoku
import time
import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Sudokku:
    def __init__(self, link):
        self.link = link
        self.rows_list = []
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)
        self.row_list = []


    def OpenPage(self):
        
        td_rows = self.driver.find_elements(By.TAG_NAME, 'td')
        for td_row in td_rows:
            if td_row.text == '':
                self.rows_list.append(0)
            else:
                self.rows_list.append(int(td_row.text))
        board_size = int(len(self.rows_list)**0.5)
        for i in range (0, board_size):
            self.row_list.append(self.rows_list[board_size * i: board_size*(i+1)])
        return self.row_list

    def SolveSudoku(self):
        puzzle = Sudoku(3, 3, board=self.row_list)
        puzzle.solve().board