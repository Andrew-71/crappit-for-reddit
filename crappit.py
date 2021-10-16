import sys

from PyQt5 import uic  # The thing that makes design go brrr
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog

import praw  # For communications with Reddit
import ast  # I have no fucking idea what this does but it somehow makes class 'bot_info_file' work


# ==================================================================================================
# Hides user id and user secret from code
class reddit_info_file:
    def __init__(self, filename):  # Get dict with app info
        f = open(filename, 'r')
        self.data = ast.literal_eval(f.read())
        f.close()

    def r_id(self):  # return app id
        return self.data['app_id']

    def r_secret(self):  # return app secret
        return self.data['app_secret']


settings = reddit_info_file('logininfo.txt')
reddit = praw.Reddit(client_id=settings.r_id(), client_secret=settings.r_secret(),
                     user_agent='Unnoficial reddit client by u/AndreyRussian1')
# ==================================================================================================


class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_ui.ui', self)  # Load in UI

        self.configure_buttons()

    def configure_buttons(self):
        self.refresh_btn.clicked.connect(self.refresh_posts)

        # Connect vote buttons and disable them so that users can't vote on... nothing
        self.upvote_btn.clicked.connect(lambda: self.vote_post(True))
        self.downvote_btn.clicked.connect(lambda: self.vote_post(False))
        self.upvote_btn.setEnabled(False)
        self.downvote_btn.setEnabled(False)

        self.comment_btn.clicked.connect(self.comment_post)
        self.comment_btn.setEnabled(False)

        self.next_btn.clicked.connect(lambda: self.move_post(1))
        self.previous_btn.clicked.connect(lambda: self.move_post(-1))
        self.next_btn.setEnabled(False)
        self.previous_btn.setEnabled(False)

    def refresh_posts(self):
        self.posts = []
        for i in reddit.subreddit('LearnProgramming').hot(limit=5):
            self.posts.append(i.id)
        self.current_post = 0
        self.show_post(self.posts[0])
        self.next_btn.setEnabled(True)

        self.upvote_btn.setEnabled(True)
        self.downvote_btn.setEnabled(True)
        self.comment_btn.setEnabled(True)

    def vote_post(self, up_or_down):
        app_vote_error = error_window('Unable to vote', 'this means the post is deleted or archived')
        try:
            if up_or_down:
                self.current_post.upvote()
            else:
                self.current_post.downvote()
        except:
            app_vote_error.show()

    def comment_post(self):
        app_comment_error = error_window('Unable to comment', 'this means the post is deleted or locked')
        try:
            pass
        except:
            app_comment_error.show()

    def move_post(self, change):
        self.current_post += change

        self.previous_btn.setEnabled(False if self.current_post == 0 else True)
        self.next_btn.setEnabled(False if self.current_post == len(self.posts) else True)

        if self.current_post != 0 and self.current_post != len(self.posts):
            self.show_post(self.posts[self.current_post])

    def show_post(self, post_id):
        post = reddit.submission(id=post_id)
        self.body_text.setText(post.selftext)
        self.title_text.setText(post.title)
        self.username_text.setText(post.author.name)


class error_window(QDialog):
    def __init__(self, message, message_explain):
        super().__init__()
        uic.loadUi('error_ui.ui', self)  # Load in UI
        self.ok_btn.clicked.connect(lambda: self.hide())
        self.label.setText(message)  # Big text, error name
        self.label_2.setText(message_explain)  # Smaller text, explains what that means


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app_main_window = main_window()
    app_main_window.show()

    sys.exit(app.exec_())
