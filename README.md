# 🦓 ZebraWatch - 斑马线行人检测系统

## 📝 项目简介

ZebraWatch 是一个基于 YOLOv8 和 PyQt5 开发的实时行人检测系统，专门用于监测斑马线区域的行人情况。该系统支持实时视频流分析、离线视频处理和图片检测功能。

## ✨ 主要特性

- 🎯 实时行人检测
- 🎥 支持摄像头实时监测
- 📹 支持视频文件分析
- 🖼️ 支持图片检测
- 📊 实时显示检测结果
- 💾 视频录制功能
- 🔐 用户认证系统
- 📋 检测日志记录

## 🛠️ 技术栈

- Python 3.8+
- YOLOv8
- PyQt5
- OpenCV
- SQLite3

## 📦 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/ZebraWatch.git
cd ZebraWatch
```

2. 创建虚拟环境（推荐）：
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 🚀 使用说明

1. 启动程序：
```bash
python run.py
```

2. 登录系统：
   - 默认管理员账号：admin
   - 默认密码：admin123
   - 或注册新用户

3. 主要功能：
   - 📹 离线识别
     - 支持视频文件分析
     - 支持图片文件分析
   - 🎥 在线识别
     - 支持摄像头实时监测
   - 💾 录制功能（仅管理员）
     - 支持检测结果录制
   - ℹ️ 帮助
     - 关于
     - 使用说明

## 👥 用户权限

- 👑 管理员用户
  - 所有功能的完整访问权限
  - 视频录制功能
  - 系统管理功能

- 👤 普通用户
  - 基本检测功能
  - 查看检测结果
  - 实时监测功能

## 📊 检测效果

系统可以实时检测：
- 🚶 行人位置
- 🦓 斑马线区域
- 📊 统计人数
- ⚠️ 违规行为

## 💡 特别说明

- 支持多种视频格式（mp4, avi 等）
- 支持多种图片格式（jpg, png, bmp）
- 检测结果实时显示
- 自动记录检测日志
- 界面简洁直观

## 🔧 系统要求

- 操作系统：Windows/Linux/MacOS
- Python 3.8 或更高版本
- 内存：至少 4GB
- 显卡：支持 CUDA 可获得更好性能（可选）

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 📧 Email: xiangrui0070@gmail.com
- 💬 微信: Liang-Zai_666

## 🙏 致谢

- YOLOv8 团队提供的优秀目标检测模型
- PyQt5 提供的 GUI 开发框架
- OpenCV 团队的计算机视觉库

---
⭐ 如果这个项目对你有帮助，欢迎点个 star！ 
