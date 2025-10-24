from qgis.PyQt import QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets

'''
heckableComboBox(self.dataProvidersComboBox)
'''

class CheckableComboBox(QtWidgets.QComboBox):
        
    def __init__(self, position, *args, **kwargs): # = (0,0), title = '', parent=None, 
        super().__init__(*args,**kwargs)
        # self.setTitle(title)
        # self.position = position # try this
        self.view().pressed.connect(self.handleItemPressed)
        self.setModel(QtGui.QStandardItemModel(self))

    def handleItemPressed(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == QtCore.Qt.Checked:
            item.setCheckState(QtCore.Qt.Unchecked)
        else:
            item.setCheckState(QtCore.Qt.Checked)

    def title(self):
        return self._title

    def setTitle(self, title):
        self._title = title
        self.repaint()

    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        painter.setPen(self.palette().color(QtGui.QPalette.Text))
        opt = QtWidgets.QStyleOptionComboBox()
        self.initStyleOption(opt)
        opt.currentText = self._title
        painter.drawComplexControl(QtWidgets.QStyle.CC_ComboBox, opt)
        painter.drawControl(QtWidgets.QStyle.CE_ComboBoxLabel, opt)

# class CheckableSearchableComboBox(QtWidgets.QComboBox):

#     # Subclass Delegate to increase item height
#     # do I need this?
#     class Delegate(QtWidgets.QStyledItemDelegate):
#         def sizeHint(self, option, index):
#             size = super().sizeHint(option, index)
#             size.setHeight(20)
#             return size

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Make the combo editable to set a custom text, but readonly
#         # why readonly?
#         self.setEditable(True)
#         self.lineEdit().setReadOnly(True)

#         # Use custom delegate
#         self.setItemDelegate(CheckableSearchableComboBox.Delegate())

#         # Update the text when an item is toggled
#         self.model().dataChanged.connect(self.updateText)

#         # Hide and show popup when clicking the line edit
#         self.lineEdit().installEventFilter(self)
#         self.closeOnLineEditClick = False

#         # Prevent popup from closing when clicking on an item
#         self.view().viewport().installEventFilter(self)

#         #def __init__(self, parent=None):
#         #super(SearchableComboBox, self).__init__(parent)

#         self.setFocusPolicy(Qt.ClickFocus)
#         self.setEditable(True)

#         # prevent insertions into combobox
#         self.setInsertPolicy(QtWidgets.QComboBox.NoInsert)

#         # filter model for matching items
#         self.pFilterModel = QSortFilterProxyModel(self)
#         self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
#         self.pFilterModel.setSourceModel(self.model())

#         # completer that uses filter model
#         self.completer = QtWidgets.QCompleter(self.pFilterModel, self)
#         self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
#         self.setCompleter(self.completer)

#         # connect signals
#         self.lineEdit().textEdited[str].connect(self.pFilterModel.setFilterFixedString)
#         self.completer.activated.connect(self.on_completer_activated)

#     def resizeEvent(self, event):
#         # Recompute text to elide as needed
#         self.updateText()
#         super().resizeEvent(event)

#     def eventFilter(self, object, event):

#         if object == self.lineEdit():
#             if event.type() == QEvent.MouseButtonRelease:
#                 if self.closeOnLineEditClick:
#                     self.hidePopup()
#                 else:
#                     self.showPopup()
#                 return True
#             return False

#         if object == self.view().viewport():
#             if event.type() == QEvent.MouseButtonRelease:
#                 index = self.view().indexAt(event.pos())
#                 item = self.model().item(index.row())

#                 if item.checkState() == Qt.Checked:
#                     item.setCheckState(Qt.Unchecked)
#                 else:
#                     item.setCheckState(Qt.Checked)
#                 return True
#         return False

#     def showPopup(self):
#         super().showPopup()
#         # When the popup is displayed, a click on the lineedit should close it
#         self.closeOnLineEditClick = True

#     def hidePopup(self):
#         super().hidePopup()
#         # Used to prevent immediate reopening when clicking on the lineEdit
#         self.startTimer(100)
#         # Refresh the display text when closing
#         self.updateText()

#     def timerEvent(self, event):
#         # After timeout, kill timer, and reenable click on line edit
#         self.killTimer(event.timerId())
#         self.closeOnLineEditClick = False

#     def updateText(self):
#         texts = []
#         for i in range(self.model().rowCount()):
#             if self.model().item(i).checkState() == Qt.Checked:
#                 texts.append(self.model().item(i).text())
#         text = ", ".join(texts)

#         # Compute elided text (with "...")
#         metrics = QtWidgets.QFontMetrics(self.lineEdit().font())
#         elidedText = metrics.elidedText(text, Qt.ElideRight, self.lineEdit().width())
#         self.lineEdit().setText(elidedText)

#     def addItem(self, text, data=None):
#         item = QStandardItem()
#         item.setText(text)
#         if data is None:
#             item.setData(text)
#         else:
#             item.setData(data)
#         item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
#         item.setData(Qt.Unchecked, Qt.CheckStateRole)
#         self.model().appendRow(item)

#     def addItems(self, texts, datalist=None):
#         for i, text in enumerate(texts):
#             try:
#                 data = datalist[i]
#             except (TypeError, IndexError):
#                 data = None
#             self.addItem(text, data)

#     def currentData(self):
#         # Return the list of selected items data
#         res = []
#         for i in range(self.model().rowCount()):
#             if self.model().item(i).checkState() == Qt.Checked:
#                 res.append(self.model().item(i).data())
#         return res

# #class SearchableComboBox(QComboBox):

#     def on_completer_activated(self, text):
#         if text:
#             index = self.findText(text)
#             self.setCurrentIndex(index)
#             self.activated[str].emit(self.itemText(index))

#     def setModel(self, model):
#         super(CheckableSearchableComboBox, self).setModel(model)
#         self.pFilterModel.setSourceModel(model)
#         self.completer.setModel(self.pFilterModel)

#     def setModelColumn(self, column):
#         self.completer.setCompletionColumn(column)
#         self.pFilterModel.setFilterKeyColumn(column)
#         super(CheckableSearchableComboBox, self).setModelColumn(column)