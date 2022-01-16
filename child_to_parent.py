"""
Please subscribe
Youtube channel:
	https://www.youtube.com/channel/UCD5qW5OsxJ-ZH7PlxstpdbQ
fauziwei@yahoo.com
"""
import sys

from PySide2.QtWidgets import (QApplication, QWidget,
	QTreeWidget, QTreeWidgetItem, QHBoxLayout)
from PySide2.QtGui import (QIcon, QPixmap)

# ------------------------
# children0 connect to parent0
parent0 = {'parent_id': None, 'id': 6, 'name': 'Test1'}
children0 = [
	{'parent_id': 6, 'id': 46, 'name': 'CG Render Footage with AOV'},
	{'parent_id': 6, 'id': 47, 'name': 'Reference'},
	{'parent_id': 6, 'id': 45, 'name': 'Shoot Footage'},
	{'parent_id': 46, 'id': 141, 'name': 'Fire and Smoke Explode'},
	{'parent_id': 46, 'id': 142, 'name': 'Fragment'},
	{'parent_id': 46, 'id': 140, 'name': 'Smoke Dust'},
	{'parent_id': 47, 'id': 143, 'name': 'Reference for CG Production'},
	{'parent_id': 47, 'id': 144, 'name': 'The Fragment of Effect in Movie'},
	{'parent_id': 45, 'id': 135, 'name': 'Blood'},
	{'parent_id': 45, 'id': 137, 'name': 'Fire and Smoke'},
	{'parent_id': 45, 'id': 139, 'name': 'Lens Flare'},
	{'parent_id': 45, 'id': 136, 'name': 'Rain and Snow'},
	{'parent_id': 45, 'id': 138, 'name': 'TV-Noise'}
]

# ------------------------
# children1 connect to parent1
parent1 = {'parent_id': None, 'id': 5, 'name': 'Test2'}
children1 = [
	{'parent_id': 5, 'id': 40, 'name': 'Billow'},
	{'parent_id': 5, 'id': 35, 'name': 'Burned Smoke'},
	{'parent_id': 5, 'id': 36, 'name': 'Cloud'},
	{'parent_id': 5, 'id': 34, 'name': 'Environment Dust and Smoke'},
	{'parent_id': 5, 'id': 37, 'name': 'Fire'},
	{'parent_id': 5, 'id': 44, 'name': 'Mar/Fragment Crush'},
	{'parent_id': 5, 'id': 41, 'name': 'Sea Surface'},
	{'parent_id': 5, 'id': 43, 'name': 'Thunder and Lighting'},
	{'parent_id': 5, 'id': 39, 'name': 'Vortex'},
	{'parent_id': 5, 'id': 42, 'name': 'Water Surface'},
	{'parent_id': 5, 'id': 38, 'name': 'Waterfall'}
]


# ------------------------
class Window(QWidget):

	def __init__(self):
		super().__init__()

		self.icon_dir = QIcon(QPixmap("folder.png"))
		self.icon_logo = QIcon(QPixmap("logo.ico"))

		# collect the parents
		self.parents = []
		self.parents.append(parent0)
		self.parents.append(parent1)

		# collect the children
		self.children = []
		self.children.append(children0)
		self.children.append(children1)

		self.initUi()
		self.initData()
		self.initLayout()

	def initUi(self):
		self.tree = QTreeWidget(self)
		self.tree.setHeaderHidden(True)

	def initData(self):
		for i, parent in enumerate(self.parents):
			p_obj = QTreeWidgetItem(self.tree) # connect parent to treewidget
			p_obj.setText(0, parent['name'])
			p_obj.setIcon(0, self.icon_dir)
			# p_obj.setExpanded(True) # show expanded trees
			# recursion
			self.get_parent(parent, self.children[i], p_obj)

	def get_parent(self, parent, children, p_obj):
		for child in children:
			if parent['id'] == child['parent_id']:
				""" get parent and connect to parent """
				c_obj = QTreeWidgetItem(p_obj) # child to parent
				c_obj.setText(0, child['name'])
				c_obj.setIcon(0, self.icon_dir)
				# c_obj.setExpanded(True) # show expanded trees
				# recursion
				self.get_parent(child, children, c_obj)

	def initLayout(self):
		layout = QHBoxLayout()
		layout.addWidget(self.tree)
		self.setLayout(layout)
		self.resize(600,400)
		self.setWindowIcon(self.icon_logo)
		self.setWindowTitle('Child to Parent')
		self.show()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	sys.exit(app.exec_())
