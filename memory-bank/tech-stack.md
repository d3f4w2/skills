# Meta-Skills 技术栈

> 项目技术栈配置，基于 Vibe Coding 开发流程

---

## 核心技术

| 技术 | 版本 | 用途 |
|------|--------|------|
| **Python** | 3.10+ | 主要编程语言 |
| **pytest** | 7.0.0+ | 测试框架 |
| **ruff** | 0.1.0+ | 代码格式化和 linting |
| **pydantic** | 2.0.0+ | 数据验证和模型定义 |
| **typer** | 0.9.0+ | 命令行界面框架 |
| **rich** | 13.0.0+ | 美化 CLI 输出 |
| **PyYAML** | 6.0+ | YAML 文件解析 |
| **networkx** | 3.0+ | 技能依赖图分析 |

---

## 数据存储

| 技术 | 用途 | 配置 |
|------|------|------|
| **JSON 文件** | 轻量级数据存储 | 无额外依赖，适合中小规模 |

---

## 开发工具

| 左具 | 用途 |
|------|------|
| **ruff** | 代码格式化、linting、import 排序 |
| **pytest** | 单元测试、集成测试、覆盖率 |
| **pytest-cov** | 测试覆盖率报告 |

---

## 可选依赖

| 依赖 | 版本 | 用途 |
|------|--------|------|
| **pytest-asyncio** | 0.21+ | 异步测试支持 |
| **aiofiles** | 0.8.0+ | 异步文件操作 |
| **aiohttp** | 3.0+ | 异步 HTTP 请求（如需） |

---

## 依赖文件

### requirements.txt
```
# 核心依赖
pydantic>=2.0.0
networkx>=3.0
rich>=13.0.0
typer>=0.9.0
PyYAML>=6.0

# 异步支持
aiofiles>=0.8.0
aiohttp>=3.0.0
```

### dev-requirements.txt
```
# 开发依赖
pytest>=7.0.0
pytest-cov>=4.0.0
pytest-asyncio>=0.21
ruff>=0.1.0
```

---

## 代码风格配置

### ruff.toml
```toml
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "B",           # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # flake8-unused-arguments
    "SIM",    # flake8-simplify
]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

---

## 开发原则

1. **不可变性**: 使用 `@dataclass(frozen=True)` 或 `NamedTuple`
2. **类型安全**: 所有函数必须有类型注解（Python 3.10+ 原生语法）
3. **错误处理**: 显式错误处理，绝不静默吞噬
4. **模块化**: 小文件 (<800 行），高内聚低耦合
5. **测试驱动**: TDD 方法论，80%+ 覆盖率

---

## Python 3.10+ 特性使用

本项目将利用 Python 3.10+ 的现代特性：

```python
# 类型提示联合语法 - 使用 | 代替 Optional
def process(value: int | None) -> str:
    ...

# 使用 dict 和 list 代替 Dict, List
def get_items() -> list[dict[str, Any]]:
    ...

# match 语句
match status:
    case "success":
        ...
    case "error" | "failed":
        ...
    case _:
        ...

# Pydantic v2+ 使用 field_validator
from pydantic import BaseModel, Field, field_validator

class MyModel(BaseModel):
    @field_validator('name')
    @classmethod
    def validate_name(cls, v: str) -> str:
        return v.strip()
```
