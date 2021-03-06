from .. import QtWidgets
from .. import base


class LayoutMixin(object):
    def __init__(self, *args, **kwargs):
        self.prevParent = None
        self.secPrevParent = None

    def __enter__(self):
        if base.glob_current_active_parent:
            self.prevParent = base.glob_current_active_parent
        else:
            self.prevParent = self
        base.glob_current_active_parent = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        base.glob_current_active_parent = self.prevParent

    def setRatio(self, *ratios):
        for idx, ratio in enumerate(ratios):
            self.setStretch(idx, ratio)

    def setLastStretch(self, val):
        lastChild = self.count() - 1
        self.setStretch(lastChild, val)

    def add(self, child):
        from ..widgets.base import LabelMixin
        if isinstance(child,LabelMixin) and child.parentWidget is not None:
            self.add(child.parentWidget)
            return
        else:
            if isinstance(child, QtWidgets.QSpacerItem):
                self.addSpacerItem(child)
            elif isinstance(child, QtWidgets.QWidget):
                self.addWidget(child)
            elif isinstance(child, QtWidgets.QLayout):
                self.addLayout(child)


class VBoxLayout(QtWidgets.QVBoxLayout, LayoutMixin):
    pass


class HBoxLayout(QtWidgets.QHBoxLayout, LayoutMixin):
    pass


class GridLayout(QtWidgets.QGridLayout, LayoutMixin):
    pass


class StackedLayout(QtWidgets.QStackedLayout, LayoutMixin):
    pass


class FormLayout(QtWidgets.QFormLayout, LayoutMixin):
    pass
