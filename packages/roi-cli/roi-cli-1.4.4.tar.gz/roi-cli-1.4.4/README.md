## 环境依赖
 - ubuntu


## 库依赖
 - click


## 安装步骤
 - pip install roi-cli 


## 目录结构描述

```
├── Readme.md                    // help document
│
├── bin                          // 可执行程序
│   ├── __init__.py
│   ├── ai_check.py              // 算法检查当前环境程序
│   ├── ai_env.py                // 安装算法所需环境程序
│   ├── ai_init.py               // 初始化算法项目工程程序
│   ├── ai_pkg.py                // 安装算法三方库
│   ├── be_init.py               // 初始化server项目工程程序
│   └── be_pkg.py                // 安装server三方库
│
├── core                         // 项目核心文件
│   ├── __init__.py
│   └── main.py                  // 项目入口文件
│
└── setup.py                     // 项目配置文件
```

## V1.1.1 版本内容
 - 1.检查当前系统环境
 - 2.安装当前所需环境
 - 3.安装当前所需三方库
 - 4.搭建项目工程


## 使用命令
```
Usage: roi [OPTIONS] COMMAND [ARGS]...

  This is an automated Scaffolding, see the following for specific usage

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  ai-check  check ai_env info
  ai-env    install ai_env
  ai-init   init an ai project
  ai-pkg    install ai_packages
  be-init   init a drf project
  be-pkg    download drf sitepackages

```