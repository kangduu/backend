# macOS 上安装 Python

在 macOS 上安装 Python 并执行 `.py` 代码，推荐使用 Homebrew + Python 3 + VS Code。

## 检查 Mac 是否已安装 Python

打开 macOS 的终端（Terminal），依次执行：

```
python3 --version
```

再执行：

```
which python3
```

如果输出类似：

```
Python 3.13.x
/opt/homebrew/bin/python3
```

说明已经安装了 Python 3，可以直接跳到第三步。

注意：macOS 中的 `python`、`python3` 和 `pip3` 并不完全相同。建议开发时明确使用 `python3`，不要修改 macOS 系统自带的 Python。

## 使用 Homebrew 安装 Python

### 1. 更新 Homebrew

```
brew update
```

### 2. 安装 Python

```
brew install python
```

### 3. 验证安装结果

```
python3 --version
pip3 --version
which python3
```

Apple Silicon 芯片（M 系列）Mac 通常会使用 `/opt/homebrew` 下的 Homebrew 安装路径。

## 推荐的开发方式：使用虚拟环境

如果你后续会运行数据处理脚本、自动化程序或第三方 Python 库，建议每个项目都创建独立的虚拟环境，避免不同项目的依赖相互冲突。

在项目目录下执行：

```
# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境
source .venv/bin/activate

# 安装第三方库
python -m pip install requests

# 执行 Python 文件
python main.py
```

激活成功后，终端提示符通常会出现 `(.venv)`。

退出虚拟环境：

```
deactivate
```

## 五、常用命令速查

| 需求             | 命令                              |
| ---------------- | --------------------------------- |
| 查看 Python 版本 | `python3 --version`               |
| 执行 Python 文件 | `python3 main.py`                 |
| 进入交互式解释器 | `python3`                         |
| 退出交互式解释器 | `exit()`                          |
| 查看 pip 版本    | `python3 -m pip --version`        |
| 安装第三方库     | `python3 -m pip install requests` |
| 查看已安装的库   | `python3 -m pip list`             |
| 创建虚拟环境     | `python3 -m venv .venv`           |
| 激活虚拟环境     | `source .venv/bin/activate`       |
| 退出虚拟环境     | `deactivate`                      |

# Windows 安装 Python 3

## 使用官方安装包（推荐）

1. 打开 Python 官方下载页面：[Python for Windows](https://www.python.org/downloads/windows/?utm_source=chatgpt.com)
2. 下载 Windows 64-bit 安装程序。
3. 双击运行安装程序。

**非常重要** 安装时一定勾选： `Add python.exe to PATH`

然后点击 `Install Now`。

## 验证 Python 是否安装成功

打开 Windows Terminal 或 PowerShell。

执行：

```
python --version
```

查看安装路径：

```
where.exe python
```

查看 pip：

```
python -m pip --version
```

也可以使用 Windows Python Launcher：

```
py --version
```

## 测试执行 Python 代码

创建项目目录：

```
mkdir D:\python-projects
cd D:\python-projects
```

创建 `main.py`：

```
name = "Windows Python"print(f"Hello, {name}!")print("Python is working!")
```

执行：

```
python main.py
```

## 四、Windows 与 macOS 命令对比

| 操作         | macOS                             | Windows                          |
| ------------ | --------------------------------- | -------------------------------- |
| 查看版本     | `python3 --version`               | `python --version`               |
| 执行代码     | `python3 main.py`                 | `python main.py`                 |
| pip 安装库   | `python3 -m pip install requests` | `python -m pip install requests` |
| 进入交互模式 | `python3`                         | `python`                         |
| 创建虚拟环境 | `python3 -m venv .venv`           | `python -m venv .venv`           |
| 激活虚拟环境 | `source .venv/bin/activate`       | `.venv\Scripts\Activate.ps1`     |
| 退出虚拟环境 | `deactivate`                      | `deactivate`                     |

# 推荐的开发环境

让 Mac 和 Windows 使用相同的 Python 项目结构、依赖管理方式（`.venv` + `requirements.txt`），这样两个系统之间切换开发会更加方便。
