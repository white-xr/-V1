#!C:\Users\RUI\PyCharmMiscProject\.venv\Scripts\python.exe
import sys
import os
import ultralytics
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtCore import Qt
from src.gui.mainwindow import PDMainWindow
from src.gui.login import LoginDialog

def init_fonts():
    """初始化字体"""
    # 添加 SimHei 字体
    font_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SimHei.ttf")
    if os.path.exists(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id != -1:
            print("✅ 成功加载 SimHei 字体")
            return True
    print("⚠️ 无法加载 SimHei 字体，将使用系统默认字体")
    return False

def create_default_font():
    """创建默认字体"""
    font = QFont()
    font.setPointSize(12)
    
    if init_fonts():
        font.setFamily("SimHei")
    else:
        # 尝试使用系统字体
        for family in ['Microsoft YaHei', 'SimSun', 'Arial']:
            if family in QFontDatabase().families():
                font.setFamily(family)
                break
    return font

def main():
    print("="*40)
    print(f"🔍 YOLO 模型版本: {ultralytics.__version__}")
    print("🚀 正在准备启动 Pedestrian Detection 应用...")
    print("="*40)

    try:
        # 在创建QApplication之前设置属性
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
        
        # 创建应用实例
        app = QApplication(sys.argv)
        app.setStyle('Fusion')
        
        # 设置应用程序范围的默认字体
        default_font = create_default_font()
        app.setFont(default_font)
        
        # 显示登录窗口
        login_dialog = LoginDialog()
        if login_dialog.exec_() == QDialog.Accepted:
            # 登录成功，创建并显示主窗口
            print("✅ 登录成功，正在加载主界面...")
            win = PDMainWindow()
            # 设置用户信息
            username = login_dialog.username_input.text().strip()
            role = 'admin' if username == 'admin' else 'user'
            win.set_user_info(username, role)
            win.show()
            print("✅ 应用界面已显示，进入事件循环中...")
            exit_code = app.exec_()
            print(f"👋 应用已正常退出，退出码: {exit_code}")
            sys.exit(exit_code)
        else:
            print("❌ 登录取消或失败，应用退出")
            sys.exit(0)
            
    except Exception as e:
        print("❌ 启动过程中发生异常:")
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
