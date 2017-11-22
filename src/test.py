import sys
from PyQt4 import QtGui


def blankPane():
	app = QtGui.QApplication(sys.argv); 

	w = QtGui.QWidget(); 
	w.resize(250,150); 
	w.move(300,300); 
	w.setWindowTitle('Simple'); 
	w.show(); 
	sys.exit(app.exec_()); 

def buttonPane():
	app = QtGui.QApplication(sys.argv); 

	w = QtGui.QWidget(); 
	w.setToolTip("This is a <b>QWidget</b> widget");

	btn = QtGui.QPushButton('Button',w); 
	btn.setToolTip('This is a <b>QPushButton</b> widget'); 
	btn.resize(btn.sizeHint()); 
	btn.move(50,50); 

	w.setGeometry(300,300,250,150); 
	w.setWindowTitle("ToolTips"); 
	w.show(); 
	sys.exit(app.exec_()); 

if __name__ == '__main__':
	buttonPane(); 