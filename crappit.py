import sys  # Used for... idk?
import re  # Used for formatting.
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QMessageBox  # All types of windows we use.
import praw  # For communications with Reddit.
import prawcore  # For handling Reddit exceptions.
import urllib.request  # Handles download of images for image posts.
import pyperclip  # For copying link to post.
import sqlite3  # For databases. I hate those things.
import time  # For displaying time since submission was posted

import app_ui  # Import UI


# ==================================================================================================
# Function for formatting text from weird reddit standard to HTML
# String as input, string as output

def format_text(text):
    pattern_link = re.compile(r'\[.*?\]\[.*?\]')  # Pattern to find links  (weird format)
    pattern_link_normal = re.compile(r'\[.*?\]\(.*?\)')  # Pattern to find links (normal format)
    pattern_bold = re.compile(r'\*{2}(.*?)\*{2}')  # Pattern to find bold text
    pattern_italics = re.compile(r'\*(.*?)\*')  # Pattern to find italics

    formatted_text = ''  # Output

    if pattern_link.search(text):  # If there are weird links in text that means lowest paragraph has definitions
        link_meaning = {}  # Dictionary with all links and their meaning
        for i in text.split('\n\n')[-1].split('\n'):
            link = i.strip().split(']: ')  # Split line into name of link and it's website
            if len(link) == 0 or len(link[0]) == 0 or len(link[1]) == 0:  # If one of them is empty skip it.
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
        if len(line) != 0 and line[0] == '#':  # If we find '#' at start of line that means that this line is big
            formatted_line = f'<span style="font-size: 24px">{line}</span>'  # Make it   B I G
        else:
            formatted_line = line  # Else just use standard sized line

        formatted_line = formatted_line.replace('#', '')  # Remove '#' symbol from the line
        formatted_text += f'<p>{formatted_line}</p>'  # Put the line in paragraph to make it appear as separate line

    return formatted_text  # Output pretty, formatted text that looks good


# ==================================================================================================
# Random functions

# Input is id of a post, returns username of OP formatted in link or [DELETED] if account is deleted
def user_with_link(post):
    try:
        user = post.author.name  # Name of author of post
        user = f' <a href="https://www.reddit.com/user/{user}">u/{user}</a>'  # Clicking on username opens profile

    # TODO: Reconsider putting specific exception.
    except:  # User is deleted. I tried putting specific exception here (prawcore.NotFound) but it doesn't seem to work
        user = 'u/[DELETED]'
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
        reddit_test.user.me()  # Attempt to call API and get redditor instance of ourself.
        return True  # If previous line didn't cause an error then info is valid.

    except BaseException or prawcore.ResponseException:
        return False  # Yes, I am using try except as an if statement. This is fine.


# Input is string, outputs it with '\n' added in some places to fit it in window
def text_on_multiple_lines(text, line_len):
    new_text = ''  # Output text
    length = 0  # Length of current line

    for i in text.split():
        if length + len(i) > line_len:  # If new word wouldn't fit on the line
            length = len(i) + 1  # Change length to new line
            new_text += '\n'  # Switch to next line
        else:
            length += len(i) + 1  # Else increase length
        new_text += i + ' '  # Add word to current line

    return new_text  # Return new text, now complete with \n (tm)


# Input is reddit post, returns "d h m" type string with time since post was submitted
def time_since_post(post):
    time_minutes = round((time.time() - post.created_utc) / 60)  # Get minutes since post was submitted

    if time_minutes == 0:  # If they are 0 pretend its 1 for ease of perception
        time_minutes = 1

    # Get days
    return_time = [time_minutes // 1440]
    time_minutes -= 1440 * return_time[0]

    # Get hours
    return_time.append(time_minutes // 60)
    time_minutes -= 60 * return_time[1]

    # Get minutes
    return_time.append(time_minutes)

    # Return formatted string. If there are no days, hours or minutes then don't show that slot.
    return f'{(str(return_time[0]) + "d ") if return_time[0] != 0 else ""}' \
           f'{(str(return_time[1]) + "h ") if return_time[1] != 0 else ""}' \
           f'{(str(return_time[2]) + "m") if return_time[2] != 0 else ""}'


# Input is a post, returns True if upvoted False if downvoted None if neither
# Homemade and stupid alternative to ".likes" attribute that existed before :(
def check_vote(post):
    if post in reddit.user.me().upvoted():
        return True
    if post in reddit.user.me().downvoted():
        return False
    return None


# ==================================================================================================
# Windows code

class MainWindow(QMainWindow, app_ui.MainUi):
    def __init__(self, login_info):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(550, 760)  # Set fixed size. A sacrifice in order for image scaling to work.

        # Honestly, I am making reddit global here because most of code is inherited from when it was global
        # And I am not wasting 10 minutes adding 'self.' to all mentions of this variable.
        global reddit  # "gLoBal VarIAblE 'ReDdit' iS uNdEfiNed At tHe ModUle lEveL" yeah whatever

        # Create instance of reddit we will use to connect to the API
        reddit = praw.Reddit(client_id=login_info[3], client_secret=login_info[4],
                             user_agent='"Crappit", unofficial reddit client by u/AndreyRussian1',
                             password=login_info[2], username=login_info[1])

        self.user_id = login_info[0]  # Saving id for getting subreddits and other stuff (tm)

        # Get sorting method
        self.sorting_method = [cur.execute(f"""SELECT sort FROM Sorting WHERE id = {self.user_id}""").fetchone()[0]]

        # If above ^^^ is top or controversial then a timeframe comes with it
        if self.sorting_method[0] in {'top', 'controversial'}:
            self.sorting_method.append(cur.execute(f"""SELECT sort_time FROM Sorting 
            WHERE id = {self.user_id}""").fetchone()[0])

        self.configure_buttons()  # Tell all buttons what they are supposed to do

        self.refresh_posts()  # Start by refreshing posts

    def configure_buttons(self):

        self.refresh_btn.clicked.connect(self.refresh_posts)  # Connect refresh button

        # Connect vote buttons. True for upvote and False for downvote.
        self.upvote_btn.clicked.connect(lambda: self.vote_post(True))
        self.downvote_btn.clicked.connect(lambda: self.vote_post(False))

        self.comment_btn.clicked.connect(self.comments_post)  # Connect comments button. It shows window with comments.

        # Connect buttons for moving between posts. 1 == forward, -1 == backwards.
        self.next_btn.clicked.connect(lambda: self.move_post(1))
        self.previous_btn.clicked.connect(lambda: self.move_post(-1))

        # Connect button for copying link to post. Also this line breaks pep8 by 1 symbol which is annoying. Won't fix.
        self.share_btn.clicked.connect(lambda: pyperclip.copy(str(reddit.submission(self.posts[self.current_post]).url)))

        self.body_text.setOpenExternalLinks(True)  # Make it so the hyperlinks in text work.
        self.username_text.setOpenExternalLinks(True)  # Enable link to OP's profile
        self.subreddit_text.setOpenExternalLinks(True)  # Enable links to subreddits

        # Connect buttons for controlling what posts you see
        self.sorting_btn.clicked.connect(self.sort_selection)
        self.subreddit_btn.clicked.connect(self.subreddit_select)

        self.submit_btn.clicked.connect(self.create_post)  # Connect post creation button

    def refresh_posts(self):
        # Get subreddits user is subscribed to
        user_subreddits = cur.execute(f"""SELECT Subreddit_name FROM Subreddits WHERE id = {self.user_id}""").fetchall()

        self.update_sort()

        # If there aren't any default to r/all. Else format them properly.
        if len(user_subreddits) == 0:
            user_subreddits = ['all']
        else:
            user_subreddits = list(map(lambda x: str(x[0]), user_subreddits))

        self.posts = []  # Empty the list with post ids  (or create it if we refresh for the first time)

        # Yes. This is, in fact, most efficient method.
        # Because Reddit doesn't let you parse through posts with sorting as a parameter
        # So we need to call different methods

        # Also you know what, screw this
        # Any posts that don't have text aren't recognised
        # Wanna know why? Because there is almost no way to differentiate them from videos
        if self.sorting_method[0] == 'hot':
            for i in reddit.subreddit('+'.join(user_subreddits)).hot(limit=50):
                # Only choose text posts and officially hosted images
                if len(i.selftext) > 0 or 'i.redd.it' in i.url:
                    self.posts.append(i.id)
        elif self.sorting_method[0] == 'new':
            for i in reddit.subreddit('+'.join(user_subreddits)).new(limit=50):
                # Only choose text posts and officially hosted images
                if len(i.selftext) > 0 or 'i.redd.it' in i.url:
                    self.posts.append(i.id)
        elif self.sorting_method[0] == 'rising':
            for i in reddit.subreddit('+'.join(user_subreddits)).rising(limit=50):
                # Only choose text posts and officially hosted images
                if len(i.selftext) > 0 or 'i.redd.it' in i.url:
                    self.posts.append(i.id)
        elif self.sorting_method[0] == 'top':
            for i in reddit.subreddit('+'.join(user_subreddits)).top(self.sorting_method[1], limit=50):
                # Only choose text posts and officially hosted images
                if len(i.selftext) > 0 or 'i.redd.it' in i.url:
                    self.posts.append(i.id)
        elif self.sorting_method[0] == 'controversial':
            for i in reddit.subreddit('+'.join(user_subreddits)).controversial(self.sorting_method[1], limit=50):
                # Only choose text posts and officially hosted images
                if len(i.selftext) > 0 or 'i.redd.it' in i.url:
                    self.posts.append(i.id)

        if len(self.posts) > 0:  # If there is at least 1 post
            self.current_post = 0  # Set current post to 0  (or, once again, create this variable if its first refresh)
            self.show_post(self.posts[0])  # Show the first post we have in line

            if len(self.posts) > 1:  # If there are 2 or more posts
                self.next_btn.setEnabled(True)  # Enable forward button. How else will we get to next post? :)

            # Activate buttons used to interact with posts
            self.toggle_interaction_buttons(True)

        else:
            # Just show the message that there weren't any posts

            self.title_text.setText('No posts found')  # Tell user there aren't any posts
            self.body_text.setText('Wow, such empty!')  # Reddit website reference
            self.username_text.setText('')
            self.subreddit_text.setText('')
            self.time_text.setText('')

            # Deactivate buttons used to interact with posts... because there aren't any
            self.toggle_interaction_buttons(False)

    def toggle_interaction_buttons(self, value):
        self.upvote_btn.setEnabled(value)
        self.downvote_btn.setEnabled(value)
        self.comment_btn.setEnabled(value)
        self.share_btn.setEnabled(value)

    def vote_post(self, up_or_down):
        try:
            post = reddit.submission(id=self.posts[self.current_post])
            vote = check_vote(post)
            if up_or_down:  # If we wanna upvote
                if vote is None:
                    post.upvote()  # Upvote!
                    self.colour_button('red')
                else:
                    post.clear_vote()
                    self.colour_button()
            else:
                if vote is None:
                    post.downvote()  # Otherwise downvote!
                    self.colour_button('blue')
                else:
                    post.clear_vote()
                    self.colour_button()
        except Exception as e:
            # If we get an error, that means the post is deleted or archived, so we notify the user.
            # Now we COULD check if the post is too old and is archived,
            # but thanks to new stupid archival system that doesn't work. Thanks Reddit very cool.
            app_vote_error = MessageWindow('Unable to vote', f'Exception: {e}')
            app_vote_error.show()

    def comments_post(self):
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

        # If it's an image show it else show the body text
        if 'i.redd.it' in post.url:
            # This code screws over tall and wide images, but it's a sacrifice I am willing to take
            urllib.request.urlretrieve(post.url, "crappit-image-hash.jpg")
            self.body_text.setText(f'<img src="crappit-image-hash.jpg" width = 520 height = 470>')
        else:
            self.body_text.setText(format_text(post.selftext))

        # Show post title. Add a pin if its stickied and '(18+)' if its NSFW.
        self.title_text.setText(text_on_multiple_lines((('📌 ' if post.stickied else '') +
                                                       ('(18+) ' if post.over_18 else '') + post.title), 40))

        # Show username of OP. If post is distinguished then it's has shield.
        user = user_with_link(post)
        self.username_text.setText(f'{user} {"🛡" if post.distinguished else ""}')

        try:
            score = post.score  # Get score of post
            if score > 1000 or score < -1000:  # If its above 1000 or below -1000 round it up to save space
                score = f'{score // 1000}k'
        except:
            score = 'vote'  # If we got an error that means score is hidden so we put 'vote' like on the Reddit website
        self.score_label.setText(str(score))

        # Display state of vote button on this post
        vote = check_vote(post)
        if vote is None:
            self.colour_button()
        elif vote:
            self.colour_button('red')
        else:
            self.colour_button('blue')

        self.subreddit_text.setText(f'<a href="https://www.reddit.com/r/r/{str(post.subreddit)}">'
                                    f'r/{str(post.subreddit)}</a>')
        self.time_text.setText(f'Posted {time_since_post(post)} ago')

    def sort_selection(self):
        self.sort_window = SortingSelectWindow(self.user_id)
        self.sort_window.show()

    def update_sort(self):
        # Get sorting method
        self.sorting_method = [cur.execute(f"""SELECT sort FROM Sorting WHERE id = {self.user_id}""").fetchone()[0]]

        # If above ^^^ is top or controversial then a timeframe comes with it
        if self.sorting_method[0] in {'top', 'controversial'}:
            self.sorting_method.append(cur.execute(f"""SELECT sort_time FROM Sorting 
            WHERE id = {self.user_id}""").fetchone()[0])

    def subreddit_select(self):
        self.subreddit_select_window = SubredditSelectWindow(self.user_id)
        self.subreddit_select_window.show()

    def create_post(self):
        self.post_create_window = SubmitWindow()
        self.post_create_window.show()

    def colour_button(self, colour='white'):
        if colour == 'blue':
            self.downvote_btn.setStyleSheet("background-color: blue")
            self.upvote_btn.setStyleSheet("background-color: white")
        elif colour == 'red':
            self.downvote_btn.setStyleSheet("background-color: white")
            self.upvote_btn.setStyleSheet("background-color: red")
        else:
            self.downvote_btn.setStyleSheet("background-color: white")
            self.upvote_btn.setStyleSheet("background-color: white")


class SubmitWindow(QWidget, app_ui.SubmitPostUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(530, 480)
        self.submit_btn.clicked.connect(self.submit)

    def submit(self):
        sub_name = self.sub_name.text()
        title = self.post_title.toPlainText()
        body = self.post_text.toPlainText()

        # Here we are using nested try excepts. Generally a bad practise, but here it's to avoid having PRAW errors
        # Which are super ambiguous. Like seriously why can't they have normal errors.
        try:
            try:
                if sub_name[:2] == 'r/':
                    sub_name = sub_name[2:]

                reddit.subreddits.search_by_name(sub_name, exact=True)  # Try accessing subreddit
            except:
                raise Exception("Subreddit doesn't exist")
            try:
                reddit.validate_on_submit = True  # To make praw shut up.
                reddit.subreddit(sub_name).submit(title, body)
                self.hide()
            except:
                raise Exception("You are probably banned or subreddit is archived")
        except Exception as e:
            app_submit_post_error = MessageWindow("Unable to submit", str(e))
            app_submit_post_error.show()


#  This window doesn't use the most efficient methods of working,
#  However it is fine as it deals with simple things and will likely be rarely used.
#  You know what, just don't touch below code. It's fine as it is.
class SortingSelectWindow(QWidget, app_ui.SortingSelectUi):
    def __init__(self, id_num):
        super().__init__()
        self.setupUi(self)
        self.id_num = id_num
        self.save_btn.clicked.connect(self.save)

        # Find currently selected sorting method
        current = cur.execute(f"""SELECT * FROM Sorting WHERE id = {id_num}""").fetchone()[1:]
        if current[0] == 'hot':
            self.hot.setChecked(True)
        elif current[0] == 'new':
            self.new_sort.setChecked(True)
        elif current[0] == 'rising':
            self.rising.setChecked(True)
        elif current[0] == 'top':
            if current[1] == 'week':
                self.t_week.setChecked(True)
            elif current[1] == 'year':
                self.t_year.setChecked(True)
            else:
                self.t_all.setChecked(True)
        else:
            if current[1] == 'week':
                self.c_week.setChecked(True)
            else:
                self.c_all.setChecked(True)

    def save(self):
        if self.hot.isChecked():
            out = (self.id_num, 'hot', 'no time')

        elif self.new_sort.isChecked():
            out = (self.id_num, 'new', 'no time')

        elif self.rising.isChecked():
            out = (self.id_num, 'rising', 'no time')

        elif self.t_week.isChecked():
            out = (self.id_num, 'top', 'week')

        elif self.t_year.isChecked():
            out = (self.id_num, 'top', 'year')

        elif self.t_all.isChecked():
            out = (self.id_num, 'top', 'all')

        elif self.c_week.isChecked():
            out = (self.id_num, 'controversial', 'week')

        else:
            out = (self.id_num, 'controversial', 'all')

        cur.execute("""REPLACE INTO Sorting VALUES (?, ?, ?)""", out)
        con.commit()
        login_window.app_main_window.refresh_posts()  # Refresh main window with new sorting (or old one)
        self.hide()


class CommentsWindow(QWidget, app_ui.CommentsUi):
    def __init__(self, post_id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(430, 470)

        self.post_id = post_id  # Save id of post we are submitting to
        self.show_comments()  # Show comments
        self.new_comment_btn.clicked.connect(self.create_comment)  # Connect button for creating a comment

        self.comments_text_window.setOpenExternalLinks(True)  # Make links to user profiles and websites work

    def show_comments(self):
        post = reddit.submission(id=self.post_id)  # Get id of submission we should show
        comments_text = ''  # This is output text
        post.comments.replace_more(limit=0)  # Remove non-top level comments
        for i in post.comments:
            # Get username of OP.
            # If post is distinguished then it has shield next to it.
            # If it's stickied put pin next to it
            user = user_with_link(i)
            if i.stickied:
                user = '📌 ' + user
            if i.distinguished:
                user = user + ' 🛡'

            try:
                body = i.body  # Get body of comment
            except:
                body = '[REMOVED]'  # If we get error that means comment is removed

            try:
                score = i.score  # Get score of post
                if score > 1000 or score < -1000:  # If its above 1000 or below -1000 round it up to save space
                    score = f'{score // 1000}k'
            except:
                score = 'vote'  # If we got an error that means score is hidden so we put 'vote' like on the website

            comments_text += f'<p><b>{user}</b>\t{score} votes</p>'  # Show username in bold
            comments_text += f'<p>{format_text(body)}</p>'  # Then comment's body
            comments_text += '<br>'  # This is pretty useless but it increases distance between comments and I like that

        self.comments_text_window.setText(comments_text)  # Show comments

    def create_comment(self):
        self.comment_creator = CommentCreationWindow(self.post_id)
        self.comment_creator.show()


class CommentCreationWindow(QWidget, app_ui.SubmitCommentUi):
    def __init__(self, post_id):
        super().__init__()
        self.setupUi(self)
        self.submit_btn.clicked.connect(self.submit)  # Connect button for submission
        self.setFixedSize(350, 530)
        self.post_id = post_id

    def submit(self):
        # The post could be deleted or locked, or the user might even be banned
        # So instead of checking all possibilities we just try to submit
        try:
            post = reddit.submission(id=self.post_id)
            text = self.comment_text.toPlainText()
            post.reply(text)
            self.hide()
        except:
            app_submit_comment_error = MessageWindow('Unable to submit comment', 'The post might be locked or deleted'
                                                                                 '\nOr you might even be banned')
            app_submit_comment_error.show()
            self.hide()


# Class of windows for telling the user (or me) something.
# Custom made alternative to QMessageBox because that widget is horrendous looking
class MessageWindow(QDialog, app_ui.MessageUi):
    def __init__(self, message, message_explain):
        super().__init__()
        self.setupUi(self)
        self.ok_btn.clicked.connect(lambda: self.hide())  # "Ok" button that just closes window. For convenience.

        self.setFixedSize(400, 175)  # Set fixed size

        self.label.setText(message)  # Big text, message title
        message_explain = text_on_multiple_lines(message_explain, 45)  # Format message to fit the screen (on 2 lines)
        self.label_2.setText(message_explain)  # Smaller text, more info


class SubredditSelectWindow(QWidget, app_ui.SubredditSelectUi):
    def __init__(self, id_num):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(450, 630)
        self.id_num = id_num

        self.subreddits = []
        self.refresh()

        self.add_btn.clicked.connect(self.add_sub)
        self.remove_btn.clicked.connect(self.remove_sub)
        self.done_btn.clicked.connect(self.done)

        self.import_btn.clicked.connect(self.import_subs)
        self.export_btn.clicked.connect(self.export_subs)

    def add_sub(self):
        sub_name = str(self.subreddit_name.text())
        try:
            if len(sub_name) >= 3:
                if sub_name[:2] == 'r/':
                    sub_name = sub_name[2:]

                sub_name = sub_name.lower().capitalize()  # Format subreddit name to not have duplicates

                reddit.subreddits.search_by_name(sub_name, exact=True)  # Try accessing subreddit

                if len(cur.execute(f"""SELECT * FROM Subreddits WHERE id = ? and Subreddit_name = ?""",
                                   (self.id_num, sub_name)).fetchall()) < 1:
                    cur.execute("""INSERT INTO Subreddits VALUES (?, ?)""",
                                (self.id_num, str(sub_name)))
                    con.commit()
                    self.refresh()

            else:
                raise Exception
        except Exception as e:
            print(e)
            app_subreddit_add_error = MessageWindow('Unable to add subreddit', 'Please check your spelling')
            app_subreddit_add_error.show()

    def refresh(self):
        self.subreddits = sorted(list(map(lambda x: str(x[0]), cur.execute(f"""SELECT Subreddit_name FROM Subreddits 
                WHERE id = {self.id_num}""").fetchall())))
        self.sub_list.clear()
        self.sub_list.addItems(self.subreddits)

    def remove_sub(self):
        sub_name = str(self.subreddit_name.text())
        if len(sub_name) > 3 and sub_name[:2] == 'r/':
            sub_name = sub_name[2:]
        sub_name = sub_name.lower().capitalize()  # Format subreddit name to not have duplicates
        cur.execute(f"""DELETE FROM Subreddits WHERE id = ? and Subreddit_name = ?""", (self.id_num, str(sub_name)))
        con.commit()
        self.refresh()

    def import_subs(self):
        # God bless stackoverflow and their QMessageBox tutorials
        confirm_window = QMessageBox
        ret = confirm_window.question(self, '', "Are you sure you want to import from account?",
                                      confirm_window.Yes | confirm_window.No)

        if ret == confirm_window.Yes:
            # Basically a refresh except we use user's subbed subreddits
            self.subreddits = sorted(list(map(lambda x: x.display_name.lower().capitalize(),
                                              list(reddit.user.subreddits(limit=None)))))
            for i in self.subreddits:
                cur.execute("""INSERT INTO Subreddits VALUES (?, ?)""", (self.id_num, str(i)))
                con.commit()
            self.sub_list.clear()
            self.sub_list.addItems(self.subreddits)

    def export_subs(self):
        # Once again, may the sun never set on the StackOverflow empire
        confirm_window = QMessageBox
        ret = confirm_window.question(self, '', "Are you sure you want to export to account?",
                                      confirm_window.Yes | confirm_window.No)

        if ret == confirm_window.Yes:
            old_subreddits = sorted(list(map(lambda x: x.display_name, list(reddit.user.subreddits(limit=None)))))
            new_subreddits = sorted(list(map(lambda x: str(x[0]), cur.execute(f"""SELECT Subreddit_name FROM Subreddits 
                            WHERE id = {self.id_num}""").fetchall())))
            for i in old_subreddits:
                reddit.subreddit(i).unsubscribe()

            for i in new_subreddits:
                reddit.subreddit(i).subscribe()


    def done(self):
        login_window.app_main_window.refresh_posts()
        self.hide()


class LoginWindow(QWidget, app_ui.LoginUi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(470, 350)  # Set size to perfect one.

        # Make links to registration on Reddit work
        self.label_register.setOpenExternalLinks(True)
        self.label_api.setOpenExternalLinks(True)

        self.check_for_accounts()  # Check for accounts

        # Connect editing buttons
        self.edit_1.clicked.connect(lambda: self.edit(1))
        self.edit_2.clicked.connect(lambda: self.edit(2))
        self.edit_3.clicked.connect(lambda: self.edit(3))

        self.login_btn.clicked.connect(self.open_reddit)  # Connect button that opens main window

    def check_for_accounts(self):
        # Clear all username labels
        # Because if we just deleted a profile it would still be there
        self.username_1.setText('EMPTY SLOT')
        self.username_2.setText('EMPTY SLOT')
        self.username_3.setText('EMPTY SLOT')

        # Reset buttons and disable them for same reason.
        # First radiobutton is chosen by default. Not perfect but couldn't figure out how to uncheck them all
        self.radioButton.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton.setChecked(True)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.login_btn.setEnabled(False)

        # Check for and delete invalid accounts.
        # Because accounts tend to get deleted or banned.
        logins = cur.execute("""SELECT * FROM Users""").fetchall()
        for i in logins:
            if 3 < i[0] or i[0] < 1 or not check_for_credentials(i):
                cur.execute(f"""DELETE FROM Users WHERE id = {i[0]}""")
                cur.execute(f"""DELETE FROM Sorting WHERE id = {i[0]}""")
                con.commit()

        # Find accounts
        logins = cur.execute("""SELECT * FROM Users""").fetchall()  # Get all valid accounts
        login_exists = False  # Assume no accounts exist
        for i in logins:
            # If account exists in at least 1 slot then we can choose it and login. Oh and also display account name.
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
        self.app_edit_window = LoginWindowEdit(id_num)  # Create edit window
        self.app_edit_window.show()  # Show it
        # For more details on editing process check LoginWindowEdit class

    def open_reddit(self):
        self.login_btn.setEnabled(False)  # Solves bug of user sometimes managing to click it twice

        # Get account that is currently selected
        if self.radioButton.isChecked():
            id_num = 1
        elif self.radioButton_2.isChecked():
            id_num = 2
        else:
            id_num = 3

        credentials = cur.execute(f"""SELECT * FROM Users WHERE id = {id_num}""").fetchone()  # Get credentials of it
        self.app_main_window = MainWindow(credentials)  # Create main window
        self.app_main_window.show()  # Show it
        self.hide()  # Hide this one because we're not gonna need it for rest of session


class LoginWindowEdit(QWidget, app_ui.LoginEditUi):
    def __init__(self, id_num):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(480, 350)  # Fix the awful design of this window that's been annoying me since day 1

        self.save_btn.clicked.connect(self.save)  # Connect Save Button
        self.delete_btn.clicked.connect(self.delete)  # Connect Delete Button
        self.id_num = id_num  # Save id of which account slot we are editing

        # Check if this slot is already occupied and if it is pre-input current credentials
        data = cur.execute(f"""SELECT * FROM Users WHERE id = {id_num}""").fetchone()
        if data is not None:
            self.username.setText(data[1])
            self.password.setText(data[2])
            self.api_id.setText(data[3])
            self.api_secret.setText(data[4])

    def save(self):
        # Get credentials user put into the slots
        credentials = (self.id_num,
                       str(self.username.text()),
                       str(self.password.text()),
                       str(self.api_id.text()),
                       str(self.api_secret.text()))

        # If they are valid save them otherwise tell user to check and try again
        if check_for_credentials(credentials):
            cur.execute("""INSERT INTO Users VALUES(?, ?, ?, ?, ?)""", credentials)  # Put them into the chosen slot
            cur.execute("""INSERT INTO Sorting VALUES(?, ?, ?)""", (credentials[0], 'hot', 'no time'))  # Set sorting
            con.commit()
            login_window.check_for_accounts()  # Refresh accounts to make this one selectable
            self.hide()  # Exit this window
        else:
            app_login_error = MessageWindow('Invalid credentials', 'Please check them and submit again')
            app_login_error.show()

    def delete(self):
        cur.execute(f"""DELETE FROM Users WHERE id = {self.id_num}""")  # Empty the slot we were connected to
        con.commit()
        login_window.check_for_accounts()  # Refresh accounts to show the change
        self.hide()  # Exit this window


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Connect to the database
    con = sqlite3.connect('Settings.db')
    cur = con.cursor()

    # Open login window
    login_window = LoginWindow()
    login_window.show()

    sys.exit(app.exec_())
