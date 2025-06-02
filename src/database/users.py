import sqlite3
import hashlib
import os

class UserDatabase:
    def __init__(self, db_file='users.db'):
        self.db_file = db_file
        self._init_database()

    def _init_database(self):
        """初始化数据库，创建用户表"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()

    def _hash_password(self, password, salt=None):
        """使用SHA-256和随机salt对密码进行哈希"""
        if salt is None:
            salt = os.urandom(32).hex()
        password_hash = hashlib.sha256((password + salt).encode()).hexdigest()
        return password_hash, salt

    def add_user(self, username, password, role='user'):
        """添加新用户"""
        try:
            password_hash, salt = self._hash_password(password)
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO users (username, password_hash, salt, role) VALUES (?, ?, ?, ?)',
                (username, password_hash, salt, role)
            )
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False  # 用户名已存在

    def verify_user(self, username, password):
        """验证用户登录"""
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute('SELECT password_hash, salt, role FROM users WHERE username = ?', (username,))
        result = cursor.fetchone()
        conn.close()

        if result:
            stored_hash, salt, role = result
            password_hash, _ = self._hash_password(password, salt)
            if password_hash == stored_hash:
                return True, role
        return False, None

    def change_password(self, username, new_password):
        """修改用户密码"""
        password_hash, salt = self._hash_password(new_password)
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE users SET password_hash = ?, salt = ? WHERE username = ?',
            (password_hash, salt, username)
        )
        success = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return success 