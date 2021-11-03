import sys  # Used for... idk?
import re  # Used for formatting
import urllib.request
from PyQt5 import uic  # The thing that makes design load
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog  # All types of windows we use
import praw  # For communications with Reddit.
import prawcore  # For handling Reddit exceptions.
import pyperclip  # For copying link to post
import sqlite3  # For databases. I hate those things.


# ==================================================================================================
# Function for formatting text from weird reddit standard to HTML
# String as input, string as output

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

    # Don't question this totally not suspicious line of code.
    text = text.replace('Elon', '<a href="https://en.wikipedia.org/wiki/Criticism_of_Tesla,_Inc.">Elon</a>')

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
# Random functions

# Input is id of a post, returns username of OP formatted in link or [DELETED] if account is deleted
def user_with_link(post):
    try:
        user = post.author.name  # Name of author of post
        user = f'<a href="https://www.reddit.com/user/{user}">u/{user}</a>'  # Clicking on username opens profile
    except:  # TODO: Put the proper exception here
        user = 'u/[DELETED]'  # If we get error that means user is deleted
    return user


# Input is reddit credentials formatted as (id, username, password, api_id, api_secret),
# returns True if valid else False
def check_for_credentials(i):
    try:
        # Check for empty elements. If there are then info isn't valid.
        # This way we avoid calling Reddit for no reason.
        for j in i:
            if j == '':
                raise BaseException

        # Create reddit instance with given login credentials
        reddit_test = praw.Reddit(client_id=i[3],
                                  client_secret=i[4],
                                  user_agent='Test for credentials being valid in "Crappit for reddit" client',
                                  username=i[1],
                                  password=i[2])
        reddit_test.user.me()  # Attempt to get redditor instance of ourself.
        return True  # If previous line didn't cause an error then info is valid.

    except BaseException or prawcore.ResponseException:
        return False  # Yes, I am using try except as an if statement. This is fine.


# Input is string, outputs it with '\n' added in some places to fit it in window
def title_on_multiple_lines(title):
    new_title = ' '
    length = 0
    for i in title.split():
        if length + len(i) > 40:
            length = len(i)
            new_title += '\n '
        else:
            length += len(i)
        new_title += i + ' '
    return new_title


# ==================================================================================================
# Windows code

class MainWindow(QMainWindow):
    def __init__(self, login_info):
        super().__init__()
        self.setFixedSize(530, 700)  # Set fixed size. A sacrifice in order for image scaling to work.

        # Honestly, I am making reddit global here because most of code is inherited from when it was global
        # And I am not wasting 10 minutes adding 'self.' to all mentions of this variable.
        global reddit  # "gLoBal VarIAblE 'ReDdit' iS uNdEfiNed At tHe ModUle lEveL" yeah whatever

        # Create instance of reddit we will use to connect to the API
        reddit = praw.Reddit(client_id=login_info[3], client_secret=login_info[4],
                             user_agent='"Crappit", unofficial reddit client by u/AndreyRussian1',
                             password=login_info[2], username=login_info[1])
        self.user_id = login_info[0]  # Saving id for getting subreddits  TODO: IS THIS CORRECT, ME FROM THE FUTURE????

        uic.loadUi('main_ui.ui', self)  # Load in UI  TODO: Replace this shit with classes 1

        self.configure_buttons()  # Tell all buttons what they are supposed to do

        self.refresh_posts()  # Start by refreshing posts

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

        self.body_text.setOpenExternalLinks(True)  # Make it so the hyperlinks in text work.
        self.username_text.setOpenExternalLinks(True)  # Enable link to OP's profile

    def refresh_posts(self):
        user_subreddits = cur.execute(f"""SELECT Subreddit_name FROM Subreddits WHERE id = {self.user_id}""").fetchall()
        if len(user_subreddits) == 0:
            user_subreddits = ['all']
        else:
            user_subreddits = list(map(lambda x: x[0], user_subreddits))
        self.posts = []  # Empty the list with post ids  (or create it if we refresh for the first time)

        for i in reddit.subreddit('+'.join(user_subreddits)).hot(limit=50):
            if len(i.selftext) != 0 or 'i.redd.it' in i.url:
                self.posts.append(i.id)

        if len(self.posts) > 0:
            self.current_post = 0  # Set current post to 0  (or, once again, create this variable if its first refresh)
            self.show_post(self.posts[0])  # Show the first post we have in line
            self.next_btn.setEnabled(True)  # Enable forward button. How else will we get to next post? :)

            # Activate buttons used to interact with post
            self.upvote_btn.setEnabled(True)
            self.downvote_btn.setEnabled(True)
            self.comment_btn.setEnabled(True)
            self.share_btn.setEnabled(True)
            self.report_btn.setEnabled(True)
        else:
            self.title_text.setText('No posts found')
            self.body_text.setText('Wow, such empty!')

            # Deactivate buttons used to interact with post
            self.upvote_btn.setEnabled(False)
            self.downvote_btn.setEnabled(False)
            self.comment_btn.setEnabled(False)
            self.share_btn.setEnabled(False)
            self.report_btn.setEnabled(False)



    def vote_post(self, up_or_down):
        try:
            post = reddit.submission(id=self.posts[self.current_post])
            if up_or_down:  # If we wanna upvote
                post.upvote()  # Upvote!
            else:
                post.downvote()  # Otherwise downvote!
        except:  # TODO: make it proper error handling
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

        if len(post.selftext) == 0:
            try:
                urllib.request.urlretrieve(post.url, "crappit-image-hash.jpg")
                self.body_text.setText(f'<img src="crappit-image-hash.jpg" width = 520 height = 470>')
            except Exception as e:
                print(e)
        else:
            self.body_text.setText(format_text(post.selftext))

        # Show post title. Add a pin if its stickied and '(18+)' if its NSFW.
        self.title_text.setText(title_on_multiple_lines(('📌 ' if post.stickied else '') + ('(18+) ' if post.over_18 else '') + post.title))

        self.username_text.setText(user_with_link(post))

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

        self.comments_text_window.setOpenExternalLinks(True)

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


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('login_ui.ui', self)  # Load in UI  TODO: Replace this shit with classes 4
        self.setFixedSize(470, 350)  # Set size on perfect one.

        # Make links to registration work
        self.label_register.setOpenExternalLinks(True)
        self.label_api.setOpenExternalLinks(True)

        self.check_for_accounts()

        self.edit_1.clicked.connect(lambda: self.edit(1))
        self.edit_2.clicked.connect(lambda: self.edit(2))
        self.edit_3.clicked.connect(lambda: self.edit(3))

        self.login_btn.clicked.connect(self.open_reddit)

    def check_for_accounts(self):
        # Clear all username labels
        # Because if we deleted a profile
        # It would still be there
        self.username_1.setText('EMPTY SLOT')
        self.username_2.setText('EMPTY SLOT')
        self.username_3.setText('EMPTY SLOT')

        # Reset buttons for same reason.
        # First radiobutton is chosen by default. Not perfect but couldn't figure out how to uncheck them all
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.login_btn.setEnabled(False)

        # Delete invalid accounts
        logins = cur.execute("""SELECT * FROM Users""").fetchall()
        for i in logins:
            if 3 < i[0] or i[0] < 1 or not check_for_credentials(i):
                cur.execute(f"""DELETE FROM Users WHERE id = {i[0]}""")
                con.commit()

        # Find accounts
        logins = cur.execute("""SELECT * FROM Users""").fetchall()
        login_exists = False
        for i in logins:
            if i[0] == 1:
                self.username_1.setText(i[1])
                self.radioButton.setEnabled(True)
                if not login_exists:
                    self.radioButton.setChecked(True)
                    login_exists = True
                    self.login_btn.setEnabled(True)
            elif i[0] == 2:
                self.username_2.setText(i[1])
                self.radioButton_2.setEnabled(True)
                if not login_exists:
                    self.radioButton_2.setChecked(True)
                    login_exists = True
                    self.login_btn.setEnabled(True)
            else:
                self.username_3.setText(i[1])
                self.radioButton_3.setEnabled(True)
                if not login_exists:
                    self.radioButton_3.setChecked(True)
                    login_exists = True
                    self.login_btn.setEnabled(True)

    def edit(self, id_num):
        self.app_edit_window = LoginWindowEdit(id_num)
        self.app_edit_window.show()
        self.check_for_accounts()

    def open_reddit(self):
        if self.radioButton.isChecked():
            id_num = 1
        elif self.radioButton_2.isChecked():
            id_num = 2
        else:
            id_num = 3

        credentials = cur.execute(f"""SELECT * FROM Users WHERE id = {id_num}""").fetchone()
        self.app_main_window = MainWindow(credentials)
        self.app_main_window.show()
        self.hide()


class LoginWindowEdit(QWidget):
    def __init__(self, id_num):
        super().__init__()
        uic.loadUi('login_edit_ui.ui', self)  # Load ui TODO: replace with classes
        self.save_btn.clicked.connect(self.save)
        self.delete_btn.clicked.connect(self.delete)
        self.id_num = id_num

        data = cur.execute(f"""SELECT * FROM Users WHERE id = {id_num}""").fetchone()
        if data is not None:
            self.username.setText(data[1])
            self.password.setText(data[2])
            self.api_id.setText(data[3])
            self.api_secret.setText(data[4])

    def save(self):
        credentials = (self.id_num,
                       str(self.username.text()),
                       str(self.password.text()),
                       str(self.api_id.text()),
                       str(self.api_secret.text()))
        if check_for_credentials(credentials):
            cur.execute("""INSERT INTO Users VALUES(?, ?, ?, ?, ?)""", credentials)
            con.commit()
            login_window.check_for_accounts()
            self.hide()
        else:
            app_login_error = MessageWindow('Invalid credentials', 'Please check them and submit again')
            app_login_error.show()

    def delete(self):
        try:
            cur.execute(f"""DELETE FROM Users WHERE id = {self.id_num}""")
            con.commit()
            login_window.check_for_accounts()
            self.hide()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Connect to the database
    con = sqlite3.connect('Settings.db')
    cur = con.cursor()

    # Open login window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())