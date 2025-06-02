from PyQt5.QtWidgets import (QDialog, QLabel, QLineEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QFont, QIcon
from src.database.users import UserDatabase

class LoginDialog(QDialog):
    loginSuccess = pyqtSignal(str, str)  # 发送用户名和角色信号

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.user_db = UserDatabase()
        self.setup_ui()
        
        # 只在第一次运行时创建默认管理员账户
        try:
            success, _ = self.user_db.verify_user('admin', 'admin123')
            if not success:
                self.user_db.add_user('admin', 'admin123', 'admin')
        except Exception as e:
            print(f"初始化管理员账户时出错: {e}")

    def setup_ui(self):
        self.setWindowTitle('斑马线行人检测系统 - 用户登录')
        self.setFixedSize(400, 250)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)
        
        # 设置窗口样式
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #333333;
                font-size: 12pt;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #cccccc;
                border-radius: 4px;
                background-color: white;
                font-size: 11pt;
            }
            QLineEdit:focus {
                border-color: #66afe9;
                outline: 0;
            }
            QPushButton {
                padding: 8px 20px;
                border: none;
                border-radius: 4px;
                color: white;
                font-size: 11pt;
                min-width: 100px;
            }
            QPushButton#login_button {
                background-color: #337ab7;
            }
            QPushButton#login_button:hover {
                background-color: #286090;
            }
            QPushButton#register_button {
                background-color: #5cb85c;
            }
            QPushButton#register_button:hover {
                background-color: #449d44;
            }
        """)

        # 创建布局
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # 标题
        title_label = QLabel('欢迎登录')
        title_label.setStyleSheet("""
            font-size: 18pt;
            color: #337ab7;
            font-weight: bold;
            margin-bottom: 20px;
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # 用户名输入
        username_layout = QHBoxLayout()
        username_label = QLabel('用户名:')
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('请输入用户名')
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        layout.addLayout(username_layout)
        
        # 密码输入
        password_layout = QHBoxLayout()
        password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('请输入密码')
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)
        
        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)
        self.login_button = QPushButton('登录')
        self.login_button.setObjectName('login_button')
        self.register_button = QPushButton('注册')
        self.register_button.setObjectName('register_button')
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.register_button)
        layout.addLayout(button_layout)
        
        # 提示信息
        hint_label = QLabel('默认管理员账号: admin / admin123')
        hint_label.setStyleSheet('color: #666666; font-size: 10pt;')
        hint_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(hint_label)
        
        self.setLayout(layout)
        
        # 连接信号
        self.login_button.clicked.connect(self.login)
        self.register_button.clicked.connect(self.register)
        self.password_input.returnPressed.connect(self.login)
        
    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, '警告', '用户名和密码不能为空！')
            return
            
        success, role = self.user_db.verify_user(username, password)
        if success:
            self.loginSuccess.emit(username, role)
            self.accept()
        else:
            QMessageBox.warning(self, '错误', '用户名或密码错误！')
            self.password_input.clear()
            self.password_input.setFocus()

    def register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        
        if not username or not password:
            QMessageBox.warning(self, '警告', '用户名和密码不能为空！')
            return
            
        if len(password) < 6:
            QMessageBox.warning(self, '警告', '密码长度必须大于6位！')
            return
            
        if self.user_db.add_user(username, password):
            QMessageBox.information(self, '成功', '注册成功！')
            self.login()
        else:
            QMessageBox.warning(self, '错误', '用户名已存在！') 