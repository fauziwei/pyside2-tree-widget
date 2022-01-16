"""
Please subscribe
Youtube channel:
	https://www.youtube.com/channel/UCD5qW5OsxJ-ZH7PlxstpdbQ
fauziwei@yahoo.com
"""
import os.path as op
import sys
import os

from PySide2.QtWidgets import (QApplication, QWidget,
	QTreeWidget, QTreeWidgetItem, QHBoxLayout)
from PySide2.QtGui import (QIcon, QPixmap, QBrush, QColor)

"""
	What i want to do:
		Search subdirectories from current directory
"""
base_dir = op.abspath(op.dirname(__file__))


# ------------------------
class Window(QWidget):

	def __init__(self):
		super().__init__()

		self.icon_dir = QIcon(QPixmap("folder.png"))
		self.icon_logo = QIcon(QPixmap("logo.ico"))

		self.initUi()
		self.initData()
		self.initLayout()

	def initUi(self):
		self.tree = QTreeWidget(self)
		self.tree.setHeaderHidden(True)

	def initData(self):

		self.lists = [] # all the dictionaries

		files = os.listdir(base_dir)
		for file in files:
			fullpath = op.join(base_dir, file)
			filetype = 'dir' if op.isdir(fullpath) else 'file'

			obj = QTreeWidgetItem(self.tree)
			obj.setText(0, file)
			if filetype == 'dir':
				obj.setIcon(0, self.icon_dir)
			# obj.setExpanded(True)
			if filetype == 'file': # gray
				obj.setBackground(0, QBrush(QColor(230,230,230)))

			p = {'name': file,
				 'path': fullpath,
				 'type': filetype,
				 'obj': obj,
			}

			self.lists.append(p)

		for p in self.lists:
			# recursion to children
			self.get_children(p)


	def get_children(self, p):
		# no recursion for filetype == 'file'
		if p['type'] == 'file':
			return

		files = os.listdir(p['path'])
		for file in files:
			fullpath = op.join(p['path'], file)
			filetype = 'dir' if op.isdir(fullpath) else 'file'

			obj = QTreeWidgetItem(p['obj'])
			obj.setText(0, file)
			if filetype == 'dir':
				obj.setIcon(0, self.icon_dir)
			# obj.setExpanded(True)
			if filetype == 'file':
				obj.setBackground(0, QBrush(QColor(230,230,230)))

			c = {'name': file,
				 'path': fullpath,
				 'type': filetype,
				 'obj': obj,
			}

			self.lists.append(c)

	def initLayout(self):
		layout = QHBoxLayout()
		layout.addWidget(self.tree)
		self.setLayout(layout)
		self.resize(600,400)
		self.setWindowIcon(self.icon_logo)
		self.setWindowTitle('Parent to Child')
		self.show()		




if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	sys.exit(app.exec_())
