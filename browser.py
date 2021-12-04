#Created By Ulto4
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
#os.system('pip install -r requirements.txt')
class MainWindow(QMainWindow):
  def __init__(self,*args,**kwargs):
    super(MainWindow,self).__init__(*args,**kwargs)
    self.browser = QWebEngineView()
    self.browser.setUrl(QUrl("https://Among.robowolf.repl.co"))
    self.browser.urlChanged.connect(self.update_urlbar)
    self.browser.loadFinished.connect(self.update_title)
    self.setCentralWidget(self.browser)
    self.urlbar=QLineEdit()
    self.urlbar.returnPressed.connect(self.navigate_to_url)
    self.status= QStatusBar()
    self.setStatusBar(self.status)
    navtb = QToolBar("Navigation")
    self.addToolBar(navtb)
    homebtn = QAction("Home",self)
    homebtn.setStatusTip('Return to the Skeld')

    homebtn.triggered.connect(self.go_home)
    navtb.addAction(homebtn)
    
    rel = QAction("⟳",self)
    rel.setStatusTip('Reload')
    rel.triggered.connect(self.browser.reload)
    back = QAction("⤶",self)
    back.setStatusTip("Go Back")
    back.triggered.connect(self.browser.back)
    forw = QAction("⤷",self)
    forw.setStatusTip("Go Forward")
    forw.triggered.connect(self.browser.forward)
    navtb.addAction(back)
    navtb.addAction(forw)
    navtb.addAction(rel)
    navtb.addWidget(self.urlbar)
    disc = QAction("Discord",self)
    disc.setStatusTip('Socialize')
    disc.triggered.connect(self.discord)
    trap = QAction("♫",self)
    trap.setStatusTip('Vibe Check')
    trap.triggered.connect(self.trap)
    store = QAction("ඞ",self)
    store.setStatusTip('Don\'t Sue Me InnerSloth')
    store.triggered.connect(self.get_amongus)
    sub = QAction("👍",self)
    sub.setStatusTip('Sub to me plz')
    sub.triggered.connect(self.subscribe)
    navtb.addAction(disc)
    navtb.addAction(trap)
    navtb.addAction(store)
    navtb.addAction(sub)
    #Ulto4 WaterMark
    #self.showMaximized()
    self.show()

  def update_title(self):
    #Ulto4 Water Mark
    title=self.browser.page().title()
    self.setWindowTitle(f'Among - {title}')
  def update_urlbar(self,q):
    self.urlbar.setText(q.toString())
  def navigate_to_url(self):
    q = QUrl(self.urlbar.text())
    if q.scheme()=="":
      q.setScheme("http")
    self.browser.setUrl(q)
  def go_home(self):
    self.browser.setUrl(QUrl('https://Among.robowolf.repl.co'))
  def discord(self):
    self.browser.setUrl(QUrl('https://www.discord.com'))
  def trap(self):
    self.browser.setUrl(QUrl('https://www.youtube.com/watch?v=8-NcrRzH0vA'))
  def get_amongus(self):
    self.browser.setUrl(QUrl('https://store.steampowered.com/app/945360/Among_Us/'))
  def subscribe(self):
    
    self.browser.setUrl(QUrl
('https://www.youtube.com/channel/UClDPJcyKnwUiAX1UQgZgoAw'))

app=QApplication(sys.argv)
app.setApplicationName("Among")
window=MainWindow()
app.exec_()
