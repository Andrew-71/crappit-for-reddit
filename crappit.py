import sys  # Used for... idk?
import re  # Used for formatting
from PyQt5 import uic  # The thing that makes design load
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog  # All types of windows we use
import praw  # For communications with Reddit.
import ast  # I have no fucking idea what this does but it somehow makes class 'RedditInfoFile' work
import pyperclip  # For copying link to post


# ==================================================================================================
# Hides user login information from code
# TODO: make this spaghetti of a code have login system
# In fact I should better rewrite this completely...

class RedditInfoFile:
    def __init__(self, filename):  # Get dict with app info
        f = open(filename, 'r')
        self.data = ast.literal_eval(f.read())
        f.close()

    def r_id(self):  # return app id
        return self.data['app_id']

    def r_secret(self):  # return app secret
        return self.data['app_secret']


settings = RedditInfoFile('LoginInfo.txt')
reddit = praw.Reddit(client_id=settings.r_id(), client_secret=settings.r_secret(),
                     user_agent='Unofficial reddit client by u/AndreyRussian1')


# ==================================================================================================
# Function for formatting text from weird reddit standard to HTML

def format_text(text):
    pattern_link = re.compile(r'\[.*?\]\[.*?\]')  # Pattern to find links  (weird format)
    pattern_link_normal = re.compile(r'\[.*?\]\(.*?\)')  # Pattern to find links (classic format)
    pattern_bold = re.compile(r'\*{2}(.*?)\*{2}')  # Pattern to find bold text
    pattern_italics = re.compile(r'\*(.*?)\*')  # Pattern to find italics

    formatted_text = ''  # Output

    if pattern_link.search(text):  # If there are weird links in text that means lowest paragraph has definitions
        link_meaning = {}
        for i in text.split('\n\n')[-1].split('\n'):
            link = i.strip().split(']: ')
            if len(link) == 0 or len(link[0]) == 0 or len(link[1]) == 0:
                continue
            link_meaning[link[0][1:]] = link[1]
        text = text.rsplit('\n\n', maxsplit=1)[0]  # Remove links definitions from actual text

    # Replace all WEIRD in-text links with HTML hyperlinks  [text][link_key]
    for i in pattern_link.findall(text):
        link = i[1:-1].split('][')
        text = text.replace(i, f'<a href="{link_meaning[link[1]]}">{link[0]}</a>')

    # Replace all NORMAL in-text links with HTML hyperlinks  [text](link)
    for i in pattern_link_normal.findall(text):
        link = i[1:-1].split('](')  # Warning. Don't touch this. Might stop working even if you don't change anything.
        text = text.replace(i, f'<a href="{link[1]}">{link[0]}</a>')

    # Make bold text bold  (**text**)
    for i in pattern_bold.findall(text):
        text = text.replace(f'**{i}**', f'<b>{i}</b>')

    # Make italics text italics  (*text*)
    for i in pattern_italics.findall(text):
        text = text.replace(f'*{i}*', f'<i>{i}</i>')

    # Make big text big  (#text)
    for line in text.split('\n'):
        if len(line) != 0 and line[0] == '#':
            formatted_line = f'<span style="font-size: 24px">{line}</span>'
        else:
            formatted_line = line
        formatted_line = formatted_line.replace('#', '')  # Remove '#' symbol from the line
        formatted_text += f'<p>{formatted_line}</p>'  # Put the line in paragraph to make it appear as separate line

    return formatted_text  # Output pretty, formatted text that looks good


# ==================================================================================================
# Main window code

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_ui.ui', self)  # Load in UI  TODO: Replace this shit with classes 1
        self.configure_buttons()  # Tell all buttons what they are supposed to do
        self.body_text.setOpenExternalLinks(True)  # Make it so the hyperlinks in text work.

    def configure_buttons(self):

        self.refresh_btn.clicked.connect(self.refresh_posts)  # Connect refresh button

        # Connect vote buttons. True for upvote and False for downvote.
        self.upvote_btn.clicked.connect(lambda: self.vote_post(True))
        self.downvote_btn.clicked.connect(lambda: self.vote_post(False))

        self.comment_btn.clicked.connect(self.comment_post)  # Connect comment button. It shows window with comments.

        # Connect buttons for moving between posts. 1 == forward, -1 == backwards.
        self.next_btn.clicked.connect(lambda: self.move_post(1))
        self.previous_btn.clicked.connect(lambda: self.move_post(-1))

        # Connect button for copying link to post. Also this line breaks pep8 by 1 symbol which is annoying. Won't fix.
        self.share_btn.clicked.connect(lambda: pyperclip.copy(str(reddit.submission(self.posts[self.current_post]).url)))



    def refresh_posts(self):
        self.posts = []  # Empty the list with post ids  (or create it if we refresh for the first time)
        for i in reddit.subreddit('LearnProgramming').hot(limit=50):
            self.posts.append(i.id)
        self.current_post = 0  # Set current post to 0  (or, once again, create this variable if its first refresh)
        self.show_post(self.posts[0])  # Show the first post we have in line
        self.next_btn.setEnabled(True)  # Enable forward button. How else will we get to next post? :)

        # Activate this whole load of buttons that are disabled on startup to avoid errors
        self.upvote_btn.setEnabled(True)
        self.downvote_btn.setEnabled(True)
        self.comment_btn.setEnabled(True)
        self.share_btn.setEnabled(True)
        self.report_btn.setEnabled(True)

    def vote_post(self, up_or_down):
        try:
            if up_or_down:  # If we wanna upvote
                self.current_post.upvote()  # Upvote!
            else:
                self.current_post.downvote()  # Otherwise downvote!
        except:
            # If we get an error, that means the post is deleted or archived, so we notify the user.
            # Now we COULD check if the post is too old and is archived,
            # but thanks to new stupid archival system that doesn't work. Thanks Reddit very cool.
            app_vote_error = MessageWindow('Unable to vote', 'this means the post is deleted or archived')
            app_vote_error.show()

    def comment_post(self):
        try:
            self.comments = CommentsWindow(str(self.posts[self.current_post]))  # Create window with comments
            self.comments.show()
        except Exception as e:
            app_comment_error = MessageWindow('Unable to view comments', f'Unexpected error: {e}')
            app_comment_error.show()

    def move_post(self, change):
        self.current_post += change  # We change currently chosen index in list of post IDs by 1 or -1
        self.previous_btn.setEnabled(False if self.current_post == 0 else True)  # If first disable going back
        self.next_btn.setEnabled(False if self.current_post >= (len(self.posts) - 1) else True)  # If last can't forward
        self.show_post(self.posts[self.current_post])  # Show new current post

    def show_post(self, post_id):
        post = reddit.submission(id=post_id)  # Get id of submission we should show
        self.body_text.setText(format_text(post.selftext))

        # Show post title. Add a pin if its stickied and '(18+)' if its NSFW.
        self.title_text.setText(' ' + ('📌 ' if post.stickied else '') + ('(18+) ' if post.over_18 else '') + post.title)

        try:
            user = post.author.name  # Name of author of post
        except:
            user = '[DELETED]'  # If we get error that means user is deleted
        self.username_text.setText(' u/' + user)

        try:
            score = post.score  # Get score of post
            if score > 1000 or score < -1000:  # If its above 1000 or below -1000 round it up to save space
                score = f'{score // 1000}k'
        except:
            score = 'vote'  # If we got an error that means score is hidden so we put 'vote' like on the Reddit website
        self.score_label.setText(str(score))


class CommentsWindow(QWidget):
    def __init__(self, post_id):
        super().__init__()
        uic.loadUi('comments_ui.ui', self)  # Load in UI  TODO: Replace this shit with classes 2

        self.post_id = post_id
        self.show_comments()
        self.new_comment_btn.clicked.connect(self.create_comment)

    def show_comments(self):
        post = reddit.submission(id=self.post_id)  # Get id of submission we should show
        comments_text = ''  # This is output text
        post.comments.replace_more(limit=0)  # Remove non-top level comments
        for i in post.comments:
            try:
                user = i.author.name  # Name of author of comment
            except:
                user = '[DELETED]'  # If we get error that means user is deleted
            try:
                body = i.body  # Get body of comment
            except:
                body = '[REMOVED]'  # If we get error that means comment is removed

            comments_text += f'<p><b>u/{user}</b></p>'  # Show username in bold
            comments_text += f'<p>{format_text(body)}</p>'  # Then comment's body
            comments_text += '<br>'  # This is pretty useless but it increases distance between comments and I like that

        self.comments_text_window.setText(comments_text)  # Show comments

    def create_comment(self):
        pass


class MessageWindow(QDialog):  # Class of windows for telling the user (or me) something
    def __init__(self, message, message_explain):
        super().__init__()
        uic.loadUi('message_ui.ui', self)  # Load in UI  TODO: Replace this shit with classes 3
        self.ok_btn.clicked.connect(lambda: self.hide())  # "Ok" button that just closes window. For convenience.
        self.label.setText(message)  # Big text, message title
        self.label_2.setText(message_explain)  # Smaller text, more info


if __name__ == '__main__':
    app = QApplication(sys.argv)

    app_main_window = MainWindow()
    app_main_window.show()

    sys.exit(app.exec_())
