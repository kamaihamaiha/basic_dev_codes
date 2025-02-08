在 macOS 上，默认情况下 `python` 命令可能指向的是 Python 2.x 版本，而 `python3` 命令才是 Python 3.x 版本。由于 Python 2.x 已经不再维护，很多开发者都使用 Python 3.x 进行开发。为了让 VSCode 使用 `python3` 来执行 Python 代码，你可以按照以下步骤进行配置：

### 方法一：修改 VSCode 的 Python 解释器

1. **打开 VSCode**。
2. **打开命令面板**：
   - 使用快捷键 `Cmd + Shift + P`（macOS）。
3. **选择 Python 解释器**：
   - 在命令面板中输入 `Python: Select Interpreter`，然后选择它。
4. **选择 Python 3.x 解释器**：
   - 在弹出的列表中，选择你安装的 Python 3.x 解释器（通常路径类似于 `/usr/local/bin/python3` 或者 `/usr/bin/python3`）。

### 方法二：修改 `settings.json` 文件

1. **打开 VSCode**。
2. **打开设置**：
   - 使用快捷键 `Cmd + ,`（macOS）。
3. **搜索 `python.pythonPath`**：
   - 在搜索框中输入 `python.pythonPath`。
4. **修改 `python.pythonPath`**：
   - 将其值修改为 `python3` 或者你 Python 3.x 解释器的具体路径（例如 `/usr/local/bin/python3`）。

### 方法三：使用 `code-runner` 插件

如果你使用的是 `code-runner` 插件来运行代码，可以通过以下步骤配置：

1. **打开 VSCode**。
2. **打开设置**：
   - 使用快捷键 `Cmd + ,`（macOS）。
3. **搜索 `code-runner.executorMap`**：
   - 在搜索框中输入 `code-runner.executorMap`。
4. **修改 Python 的执行命令**：
   - 找到 `python` 的配置项，将其值修改为 `python3`。

### 方法四：在终端中直接运行

如果你希望在终端中直接运行 Python 脚本，可以使用以下命令：

```bash
python3 /Users/zhangkx/dev/myCode/basic_dev_codes/study_for_python_book/c15/mpl_squares.py
```

### 方法五：创建别名

为了方便起见，你可以在你的 shell 配置文件（如 `.bashrc`、`.zshrc` 等）中创建一个别名，将 `python` 指向 `python3`：

1. **打开终端**。
2. **编辑配置文件**：
   - 如果你使用的是 `zsh`，编辑 `~/.zshrc` 文件：
     ```bash
     nano ~/.zshrc
     ```
   - 如果你使用的是 `bash`，编辑 `~/.bashrc` 文件：
     ```bash
     nano ~/.bashrc
     ```
3. **添加别名**：
   - 在文件末尾添加以下行：
     ```bash
     alias python='python3'
     ```
4. **保存并退出**：
   - 按 `Ctrl + X`，然后按 `Y` 确认保存。
5. **使更改生效**：
   - 运行以下命令使更改立即生效：
     ```bash
     source ~/.zshrc  # 或者 source ~/.bashrc
     ```

通过以上方法，你可以让 VSCode 使用 `python3` 来执行 Python 代码。