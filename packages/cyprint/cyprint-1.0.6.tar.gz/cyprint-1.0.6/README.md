# CyPrint

CyPrint is a Python package for customized colorful logging.

## Installation

You can install CyPrint using pip:

```bash
pip install cyprint
```

## Usage

```python
from cyprint import cyprint

cyprint('info信息', "INFO")
cyprint('警告信息', "WARNING")
cyprint('成功信息', "SUCCESS")
cyprint('错误信息', "ERROR")
cyprint('debug信息', "DEBUG")
```

### Customizing Log Messages

You can also create custom log messages by specifying the log level:

```python
cyprint('Custom message', 'debug')
```

## Contributing

We welcome contributions! If you'd like to contribute to CyPrint, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE] file for details.
```

将上述内容保存到名为 `README.md` 的文件中，确保其中的信息与你的项目一致，并提供必要的安装和使用示例。然后将它放在你的项目根目录下。