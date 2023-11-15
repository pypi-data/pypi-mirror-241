from PyQt6.QtCore import pyqtSignal, QObject

class AppSignals(QObject):
    from ..widgets.file_note import fileNote

    get_db_name = pyqtSignal(str, name="get_db_name")

    filter_setup_closed = pyqtSignal(name="filter_setup_closed")

    collapseSignal = pyqtSignal(QObject, bool)

    start_file_search = pyqtSignal(str, list, name="start_file_search")

    user_signal = pyqtSignal(str, name="user_signal")

    app_mode_changed = pyqtSignal(int)

    delete_note = pyqtSignal(fileNote)

    start_edit_note = pyqtSignal(fileNote)

    toggle_column = pyqtSignal()