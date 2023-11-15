import base64
import os, threading
import sqlite3
import pickle
from tketool.JConfig import get_config_instance
import tketool.buffer.bufferbase as bb

# Global variables should be in uppercase according to PEP8
BUFFER_FOLDER = get_config_instance().get_config("buffer_folder", "buffer")
BUFFER_FILE_PATH = os.path.join(os.getcwd(), BUFFER_FOLDER, "buffer.db")


def init_db():
    """
    Initializes the SQLite database and updates the bufferbase module.
    """
    if not os.path.exists(BUFFER_FOLDER):
        os.makedirs(BUFFER_FOLDER)

    connect_pool = {}

    def get_or_create_connect():
        curr_thread_id = threading.get_ident()
        if curr_thread_id not in connect_pool:
            connect_pool[curr_thread_id] = sqlite3.connect(BUFFER_FILE_PATH)
        return connect_pool[curr_thread_id]

    t_conn = get_or_create_connect()
    t_c = t_conn.cursor()

    # create table if not exists
    t_c.execute('''
        CREATE TABLE IF NOT EXISTS buffer (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
    ''')
    t_conn.commit()

    def _load_buffer_file(key):
        conn = get_or_create_connect()
        c = conn.cursor()
        c.execute("SELECT value FROM buffer WHERE key = ?", (key,))
        row = c.fetchone()
        if row is not None:
            byte_str = base64.b64decode(row[0].encode('utf-8'))
            return pickle.loads(byte_str)
        else:
            return None

    def _save_buffer_file(lists):
        conn = get_or_create_connect()
        c = conn.cursor()
        for k, v in lists:
            byte_str = pickle.dumps(v)
            str_obj = base64.b64encode(byte_str).decode('utf-8')
            c.execute("REPLACE INTO buffer (key, value) VALUES (?, ?)", (k, str_obj))
        conn.commit()

    def _delete_buffer_file(key):
        conn = get_or_create_connect()
        c = conn.cursor()
        c.execute("DELETE FROM buffer WHERE key = ?", (key,))
        conn.commit()

    def _has_buffer_file(key):
        conn = get_or_create_connect()
        c = conn.cursor()
        c.execute("SELECT 1 FROM buffer WHERE key = ?", (key,))
        row = c.fetchone()
        return row is not None

    bb.has_buffer_file = _has_buffer_file
    bb.load_buffer_file = _load_buffer_file
    bb.delete_buffer_file = _delete_buffer_file
    bb.save_buffer_file = _save_buffer_file

    return t_conn, t_c


# Initialize the SQLite connection and cursor and store them in global variables
CONN_OBJ, CURSOR_OBJ = init_db()


def close_db():
    """
    Closes the SQLite connection.
    """
    global CONN_OBJ
    if CONN_OBJ:
        CONN_OBJ.close()
        CONN_OBJ = None
