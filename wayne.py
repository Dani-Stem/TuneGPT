import sqlite3
import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QLineEdit, QCompleter, QGridLayout, QWidget, QScrollArea
import requests
from bs4 import BeautifulSoup
import random


con = sqlite3.connect('f_is_for.db')
cur = con.cursor()

# cur.execute(''' INSERT INTO f_words VALUES ('Front Door','Weezy F. Baby and the F is for front door Cause thats where I brang it'); ''')
# cur.execute('''DELETE FROM f_words WHERE Word = 'FEMA' ''')
# con.commit()

# for row in cur.execute('SELECT * FROM f_words WHERE id <= 6'):
#     print(row)

class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        def button_clicked(x):
            return lambda: (lyric_window(x))

        def lyric_window(x):
            for row in cur.execute(f"SELECT lyric FROM f_words WHERE word = '{x}'"):
                print(row)
                msg = QMessageBox()
                lyric0 = str(row).replace('(', ' ')
                lyric1 = lyric0.replace(',)', ' ')

                msg.setText(lyric1)
                l = msg.exec_()
            return lambda: print(x)

        # def search_button_clicked(self):
        #     print(checked)
        #     user_input = self.search_bar.text()


        def cust_button_clicked(final_bar):
            cust_msg = QMessageBox()
            final_bar0 = str(final_bar).replace('(', ' ')
            final_bar1 = final_bar0.replace(',)', ' ')
            cust_msg.setText(final_bar1)
            l = cust_msg.exec_()
            # return print(final_bar)

        self.setWindowTitle("Weezy F Baby")
        self.setFixedSize(QSize(400, 500))
        main_label = QLabel("and the F is for", self)
        main_label.move(20,20)
        main_label.setStyleSheet("font-weight: bold")

        sub_label = QLabel("click on a word below to", self)
        sub_label1 = QLabel("see the corresponding lyric.", self)
        sub_label2 = QLabel("or generate your own bars by", self)
        sub_label3 = QLabel("clicking the custom button", self)
        sub_label.move(125,35)
        sub_label1.move(116,55)
        sub_label2.move(110,75)
        sub_label3.move(118,95)


        URL = ('https://randomword.com/words/f.html')
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        words_list = []
        rhyme_word_list = []
        syn_word_list = []

        for res in soup.find_all("li"):
            word = res.get_text()
            words_list.append(word.strip())

        words_list_clean = random.choice(words_list)
        f_word_list = words_list_clean.split('\n')
        f_word = random.choice(f_word_list)

        print(str(f_word))

        rzURL = (f"https://www.rhymezone.com/r/rhyme.cgi?Word={f_word}&typeofrhyme=perfect&org1=syl&org2=l&org3=y")

        rzpage = requests.get(rzURL)
        rzsoup = BeautifulSoup(rzpage.content, "html.parser")

        for res0 in rzsoup.find_all(class_="r"):
            rz_word = res0.get_text()
            rhyme_word_list.append(rz_word.strip())

        rhyme_words_list_clean = random.choice(rhyme_word_list)
        f_rhyme_word_list = rhyme_words_list_clean.split('\n')
        rhyme_word = random.choice(f_rhyme_word_list)

        print(str(rhyme_word))

        synURL = (f'https://www.merriam-webster.com/thesaurus/{rhyme_word}')

        synpage = requests.get(synURL)
        synsoup = BeautifulSoup(synpage.content, "html.parser")

        for res1 in synsoup.find(class_="mw-list"):
            syn_word = res1.get_text()
            syn_word_list.append(syn_word.strip())

        syn_words_list_clean = random.choice(syn_word_list)
        f_syn_word_list = syn_words_list_clean.split('\n')
        syn_word = random.choice(f_syn_word_list)

        print(str(syn_word))

        names = ["We", "I", "They", "He", "She", "Jack", "Jim"]
        verbs = ["was", "is", "are", "were"]
        nouns = ["playing a game", "watching television", "talking", "dancing", "speaking"]
        a = (random.choice(names))
        b = (random.choice(verbs))
        c = (random.choice(nouns))

        final_bar = "weezy f baby and the f is for", f_word, a + " ", b + " ", c + " ", syn_word + " ", "like ", rhyme_word
        print(final_bar)

        cust_button = QPushButton(self)
        cust_button.setText("Custom Lyric")
        cust_button.resize(120, 50)
        cust_button.move(138, 145)
        cust_button.clicked.connect(cust_button_clicked(final_bar))

        # self.search_bar = QLineEdit(self)
        # self.search_bar.setPlaceholderText("search...")
        # self.search_bar.move(45, 105)
        # self.search_bar.resize(130, 25)
        # self.search_button = QPushButton(self)
        # self.search_button.clicked.connect(lambda checked: search_button_clicked)
        # self.search_button.setText('>>')
        # self.search_button.move(180, 105)
        # self.search_button.resize(30, 25)

        i = 0

        for row in cur.execute('SELECT Word FROM f_words WHERE id <= 6'):
            button = QPushButton(self)
            button.setText(row[0])
            button.move(58, 230+40*i)
            button.clicked.connect(button_clicked(row[0]))

            i+=1

        o = 0

        for rowo in cur.execute('SELECT Word FROM f_words WHERE id <= 12 and id > 6'):
            button = QPushButton(self)
            button.setText(rowo[0])
            button.move(158, 230 + 40 * o)
            button.clicked.connect(button_clicked(rowo[0]))

            o += 1

        p = 0

        for rowp in cur.execute('SELECT Word FROM f_words WHERE id <= 17 and id > 12'):
            main_label.move(150, 0)
            button = QPushButton(self)
            button.setText(rowp[0])
            button.move(258, 230 + 40 * p)
            button.clicked.connect(button_clicked(rowp[0]))

            p += 1

app = QApplication(sys.argv)
win = MainWin()
win.show()
app.exec()
con.close()
