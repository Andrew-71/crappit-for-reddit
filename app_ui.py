# IF YOU ARE READING THIS IMMEDIATELY LEAVE
# THIS FILE IS A FUCKING HELLHOLE
# AUTO GENERATED AND NOT MEANT TO BE OPENED


from PyQt5 import QtCore, QtGui, QtWidgets

class CommentsUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 470)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comments_text_window = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.comments_text_window.setObjectName("comments_text_window")
        self.verticalLayout.addWidget(self.comments_text_window)
        self.new_comment_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.new_comment_btn.setObjectName("new_comment_btn")
        self.verticalLayout.addWidget(self.new_comment_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Comments"))
        self.new_comment_btn.setText(_translate("Form", "+"))


class LoginEditUi(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(640, 480)
        Widget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayoutWidget = QtWidgets.QWidget(Widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(80, 10, 361, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName("password")
        self.horizontalLayout_4.addWidget(self.password)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.api_id = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.api_id.sizePolicy().hasHeightForWidth())
        self.api_id.setSizePolicy(sizePolicy)
        self.api_id.setObjectName("api_id")
        self.horizontalLayout_2.addWidget(self.api_id)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.api_secret = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.api_secret.setObjectName("api_secret")
        self.horizontalLayout_3.addWidget(self.api_secret)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_5.addWidget(self.save_btn)
        self.delete_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout_5.addWidget(self.delete_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Login edit"))
        self.label.setText(_translate("Widget", "<html><head/><body><p><span style=\" font-family:\'Courier New\';\">Username:</span></p></body></html>"))
        self.label_4.setText(_translate("Widget", "<html><head/><body><p><span style=\" font-family:\'Courier New\';\">Password:</span></p></body></html>"))
        self.label_2.setText(_translate("Widget", "<html><head/><body><p><span style=\" font-family:\'Courier New\';\">API ID:</span></p></body></html>"))
        self.label_3.setText(_translate("Widget", "<html><head/><body><p><span style=\" font-family:\'Courier New\';\">API Secret:</span></p></body></html>"))
        self.save_btn.setText(_translate("Widget", "Save"))
        self.delete_btn.setText(_translate("Widget", "Delete account"))


class LoginUi(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(470, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QtWidgets.QWidget(Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 20, 371, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.username_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_1.setObjectName("username_1")
        self.horizontalLayout.addWidget(self.username_1)
        self.edit_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_1.sizePolicy().hasHeightForWidth())
        self.edit_1.setSizePolicy(sizePolicy)
        self.edit_1.setObjectName("edit_1")
        self.horizontalLayout.addWidget(self.edit_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.username_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_2.setObjectName("username_2")
        self.horizontalLayout_2.addWidget(self.username_2)
        self.edit_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_2.sizePolicy().hasHeightForWidth())
        self.edit_2.setSizePolicy(sizePolicy)
        self.edit_2.setObjectName("edit_2")
        self.horizontalLayout_2.addWidget(self.edit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_3.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.username_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.username_3.setObjectName("username_3")
        self.horizontalLayout_3.addWidget(self.username_3)
        self.edit_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_3.sizePolicy().hasHeightForWidth())
        self.edit_3.setSizePolicy(sizePolicy)
        self.edit_3.setObjectName("edit_3")
        self.horizontalLayout_3.addWidget(self.edit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.login_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.login_btn.setEnabled(False)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.label_register = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_register.sizePolicy().hasHeightForWidth())
        self.label_register.setSizePolicy(sizePolicy)
        self.label_register.setAlignment(QtCore.Qt.AlignCenter)
        self.label_register.setObjectName("label_register")
        self.verticalLayout.addWidget(self.label_register)
        self.label_api = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_api.sizePolicy().hasHeightForWidth())
        self.label_api.setSizePolicy(sizePolicy)
        self.label_api.setAlignment(QtCore.Qt.AlignCenter)
        self.label_api.setObjectName("label_api")
        self.verticalLayout.addWidget(self.label_api)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.radioButton.setText(_translate("Login", "1"))
        self.username_1.setText(_translate("Login", "EMPTY SLOT"))
        self.edit_1.setText(_translate("Login", "Edit"))
        self.radioButton_2.setText(_translate("Login", "2"))
        self.username_2.setText(_translate("Login", "EMPTY SLOT"))
        self.edit_2.setText(_translate("Login", "Edit"))
        self.radioButton_3.setText(_translate("Login", "3"))
        self.username_3.setText(_translate("Login", "EMPTY SLOT"))
        self.edit_3.setText(_translate("Login", "Edit"))
        self.login_btn.setText(_translate("Login", "Login"))
        self.label_register.setText(_translate("Login", "<html><head/><body><p><a href=\"https://www.reddit.com/register/\"><span style=\" text-decoration: underline; color:#0000ff;\">New? Register here!</span></a></p></body></html>"))
        self.label_api.setText(_translate("Login", "<html><head/><body><p><a href=\"https://www.reddit.com/prefs/apps\"><span style=\" text-decoration: underline; color:#0000ff;\">Get API key and secret here</span></a></p></body></html>"))


class MainUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 497, 303))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.refresh_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout.addWidget(self.refresh_btn)
        self.subreddit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.subreddit_btn.setObjectName("subreddit_btn")
        self.horizontalLayout.addWidget(self.subreddit_btn)
        self.sorting_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.sorting_btn.setObjectName("sorting_btn")
        self.horizontalLayout.addWidget(self.sorting_btn)
        self.submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.submit_btn.setObjectName("submit_btn")
        self.horizontalLayout.addWidget(self.submit_btn)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.subreddit_and_time_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subreddit_and_time_text.sizePolicy().hasHeightForWidth())
        self.subreddit_and_time_text.setSizePolicy(sizePolicy)
        self.subreddit_and_time_text.setObjectName("subreddit_and_time_text")
        self.verticalLayout_2.addWidget(self.subreddit_and_time_text)
        self.username_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_text.sizePolicy().hasHeightForWidth())
        self.username_text.setSizePolicy(sizePolicy)
        self.username_text.setTextFormat(QtCore.Qt.AutoText)
        self.username_text.setObjectName("username_text")
        self.verticalLayout_2.addWidget(self.username_text)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.title_text = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_text.sizePolicy().hasHeightForWidth())
        self.title_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.title_text.setFont(font)
        self.title_text.setObjectName("title_text")
        self.horizontalLayout_4.addWidget(self.title_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.body_text = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.body_text.setObjectName("body_text")
        self.verticalLayout_2.addWidget(self.body_text)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.share_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.share_btn.setEnabled(False)
        self.share_btn.setObjectName("share_btn")
        self.horizontalLayout_3.addWidget(self.share_btn)
        self.comment_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.comment_btn.setEnabled(False)
        self.comment_btn.setObjectName("comment_btn")
        self.horizontalLayout_3.addWidget(self.comment_btn)
        self.upvote_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.upvote_btn.setEnabled(False)
        self.upvote_btn.setObjectName("upvote_btn")
        self.horizontalLayout_3.addWidget(self.upvote_btn)
        self.score_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.score_label.setObjectName("score_label")
        self.horizontalLayout_3.addWidget(self.score_label)
        self.downvote_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.downvote_btn.setEnabled(False)
        self.downvote_btn.setObjectName("downvote_btn")
        self.horizontalLayout_3.addWidget(self.downvote_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previous_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.previous_btn.setEnabled(False)
        self.previous_btn.setObjectName("previous_btn")
        self.horizontalLayout_2.addWidget(self.previous_btn)
        self.next_btn = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.next_btn.setEnabled(False)
        self.next_btn.setObjectName("next_btn")
        self.horizontalLayout_2.addWidget(self.next_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crappit"))
        self.refresh_btn.setText(_translate("Form", "↺"))
        self.subreddit_btn.setText(_translate("Form", "Subreddits"))
        self.sorting_btn.setText(_translate("Form", "Sorting"))
        self.submit_btn.setText(_translate("Form", "+"))
        self.subreddit_and_time_text.setText(_translate("Form", " subreddit"))
        self.username_text.setText(_translate("Form", " username"))
        self.title_text.setText(_translate("Form", " An interesting title"))
        self.body_text.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Fira Sans Semi-Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt;\">Click refresh button to view posts</span></p></body></html>"))
        self.share_btn.setText(_translate("Form", "Share"))
        self.comment_btn.setText(_translate("Form", "Comments"))
        self.upvote_btn.setText(_translate("Form", "⇑"))
        self.score_label.setText(_translate("Form", "vote"))
        self.downvote_btn.setText(_translate("Form", "⇓"))
        self.previous_btn.setText(_translate("Form", "<--"))
        self.next_btn.setText(_translate("Form", "-->"))


class MessageUi(object):
    def setupUi(self, Error_message):
        Error_message.setObjectName("Error_message")
        Error_message.resize(400, 177)
        self.layoutWidget = QtWidgets.QWidget(Error_message)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 10, 381, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.ok_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.ok_btn.setObjectName("ok_btn")
        self.verticalLayout.addWidget(self.ok_btn)

        self.retranslateUi(Error_message)
        QtCore.QMetaObject.connectSlotsByName(Error_message)

    def retranslateUi(self, Error_message):
        _translate = QtCore.QCoreApplication.translate
        Error_message.setWindowTitle(_translate("Error_message", "Dialog"))
        self.label.setText(_translate("Error_message", "text_1"))
        self.label_2.setText(_translate("Error_message", "text_2"))
        self.ok_btn.setText(_translate("Error_message", "Ok"))


class SortingSelectUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(404, 537)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 341, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hot = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.hot.setObjectName("hot")
        self.verticalLayout.addWidget(self.hot)
        self.new_sort = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.new_sort.setObjectName("new_sort")
        self.verticalLayout.addWidget(self.new_sort)
        self.rising = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rising.setObjectName("rising")
        self.verticalLayout.addWidget(self.rising)
        self.t_week = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.t_week.setObjectName("t_week")
        self.verticalLayout.addWidget(self.t_week)
        self.t_year = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.t_year.setObjectName("t_year")
        self.verticalLayout.addWidget(self.t_year)
        self.t_all = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.t_all.setObjectName("t_all")
        self.verticalLayout.addWidget(self.t_all)
        self.c_week = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.c_week.setObjectName("c_week")
        self.verticalLayout.addWidget(self.c_week)
        self.c_all = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.c_all.setObjectName("c_all")
        self.verticalLayout.addWidget(self.c_all)
        self.save_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout.addWidget(self.save_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sorting selection"))
        self.hot.setText(_translate("Form", "Hot"))
        self.new_sort.setText(_translate("Form", "New"))
        self.rising.setText(_translate("Form", "Rising"))
        self.t_week.setText(_translate("Form", "Top (Week)"))
        self.t_year.setText(_translate("Form", "Top (Year)"))
        self.t_all.setText(_translate("Form", "Top (All time)"))
        self.c_week.setText(_translate("Form", "Controversial (Week)"))
        self.c_all.setText(_translate("Form", "Controversial (All time)"))
        self.save_btn.setText(_translate("Form", "Save"))


class SubmitCommentUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 530)
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comment_text = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comment_text.setFont(font)
        self.comment_text.setPlainText("")
        self.comment_text.setObjectName("comment_text")
        self.verticalLayout.addWidget(self.comment_text)
        self.submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout.addWidget(self.submit_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Submit comment"))
        self.label.setText(_translate("Form", "Comment submission"))
        self.label_2.setText(_translate("Form", "formatting:\n"
"*text*: italics\n"
"**text**: bold\n"
"#text: big text\n"
"[text](link): link with text as button"))
        self.submit_btn.setText(_translate("Form", "Post"))


class SubmitPostUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(530, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 501, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.sub_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sub_name.setObjectName("sub_name")
        self.verticalLayout.addWidget(self.sub_name)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.post_title = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.post_title.setObjectName("post_title")
        self.verticalLayout.addWidget(self.post_title)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.post_text = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.post_text.setObjectName("post_text")
        self.verticalLayout.addWidget(self.post_text)
        self.submit_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.submit_btn.setObjectName("submit_btn")
        self.verticalLayout.addWidget(self.submit_btn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Subreddit"))
        self.label_2.setText(_translate("Form", "Title"))
        self.label_3.setText(_translate("Form", "Text (optional)"))
        self.submit_btn.setText(_translate("Form", "Submit"))


class SubredditSelectUi(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 630)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 611))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subreddit_name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.subreddit_name.setObjectName("subreddit_name")
        self.horizontalLayout.addWidget(self.subreddit_name)
        self.add_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.remove_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.remove_btn.setObjectName("remove_btn")
        self.horizontalLayout.addWidget(self.remove_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sub_list = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.sub_list.setObjectName("sub_list")
        self.verticalLayout.addWidget(self.sub_list)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.done_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.done_btn.setObjectName("done_btn")
        self.verticalLayout.addWidget(self.done_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.import_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_2.addWidget(self.import_btn)
        self.export_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.export_btn.setObjectName("export_btn")
        self.horizontalLayout_2.addWidget(self.export_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_btn.setText(_translate("Form", "Add"))
        self.remove_btn.setText(_translate("Form", "Remove"))
        self.label.setText(_translate("Form", "Note: leave empty for r/all"))
        self.done_btn.setText(_translate("Form", "Done"))
        self.import_btn.setText(_translate("Form", "Import from account"))
        self.export_btn.setText(_translate("Form", "Export to account"))