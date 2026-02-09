# Meta-Skills 项目规格说明书

> 基于 Vibe Coding 开发流程和元方法论 (Meta-Methodology) 的递归自我优化思想

---

## 上下文

本项目旨在根据**元方法论** (Meta-Methodology) 的递归自我优化思想，重构当前的 Khazix-Skills 项目，构建一个能够自我优化的 AI 技能管理系统。通过创建 α-提示词（生成器）和 Ω-提示词（优化器）的核心框架，实现技能的持续进化和自我超越。

**项目背景：**
- 现有项目包含三个核心技能：github-to-skills、skill-manager、skill-evolution-manager
- 元方法论定义了递归优化循环：创生 → 自省与进化 → 创造 → 循环与飞跃
- 项目遵循 Vibe Coding 开发流程，强调规划至上和渐进式实施

**用户选择：**
- 重构范围：完整框架（含递归循环）
- 数据存储：JSON 文件（轻量级，无额外依赖）
- 兼容性：重新开始（不保证向后兼容）

---

## 产品需求 (Product Requirements)

### 核心功能

1. **α-提示词生成器 (Generator)**
   - 从用户需求生成新技能的初始结构
   - 分析 GitHub 仓库并生成技能包装器
   - 生成标准化的 SKILL.md 和相关脚本
   - 支持从模板创建技能

2. **Ω-提示词优化器 (Optimizer)**
   - 分析现有技能的性能和使用情况
   - 基于用户反馈和演化数据优化技能
   - 识别技能间的重复和可合并模式
   - 提出优化建议并自动应用

3. **递归自优化循环 (Recursive Evolution Loop)**
   - 创生阶段：生成初始的 α 和 Ω
   - 自省阶段：Ω 优化 α
   - 创造阶段：α 生成所有技能
   - 循环阶段：闭环反馈，持续进化

4. **经验存储与反馈处理**
   - 基于 JSON 文件的轻量级存储
   - 用户反馈的解析和处理
   - 跨技能的模式挖掘
   - 自动化的技能合并和拆分建议

5. **命令行界面 (CLI)**
   - 初始化、生成、分析、优化、进化等命令
   - 进度显示和状态跟踪
   - 交互式配置选项

---

## 技术栈

### 语言与框架版本
- **语言**: Python 3.10+
- **编码风格**: PEP 8 + ruff
- **测试框架**: pytest
- **格式化**: ruff (替代 black/isort)
- **类型检查**: 可选 (mypy/pyright)
- **数据验证**: pydantic
- **数据存储**: JSON 文件
- **CLI 框架**: typer
- **美化输出**: rich
- **依赖图分析**: networkx
- **YAML 解析**: PyYAML

### Python 依赖
```
pydantic>=2.0.0      # 数据验证
networkx>=3.0         # 依赖图分析
rich>=13.0.0          # 美化 CLI 输出
typer>=0.9.0          # CLI 框架
PyYAML>=6.0           # YAML 解析
```

### 开发依赖
```
pytest>=7.0.0          # 测试框架
pytest-cov>=4.0.0      # 覆盖率
pytest-asyncio>=0.21   # 异步测试支持
ruff>=0.1.0           # 格式化和 linting
mypy>=1.0.0           # 可选类型检查
```

---

## 项目结构

```
project-root/
├── .claude/
│   └── rules/                  # Claude Code 规则配置
├── memory-bank/                 # 项目记忆库（状态跟踪）
│   ├── product-requirements.md   # 产品需求文档
│   ├── tech-stack.md           # 技术栈说明
│   ├── implementation-plan.md  # 实施计划
│   ├── progress.md            # 进度跟踪
│   └── architecture.md        # 架构文档
├── meta_skills/               # 核心代码库
│   ├── SKILL.md              # 元方法论技能定义
│   ├── __init__.py
│   ├── requirements.txt       # Python 依赖
│   ├── .ruff.toml           # 代码风格配置
│   ├── core/                 # 核心框架
│   │   ├── __init__.py
│   │   ├── generator.py       # 抽象生成器基类
│   │   ├── optimizer.py       # 抽象优化器基类
│   │   ├── evolution_cycle.py  # 进化周期管理
│   │   └── models/           # 数据模型
│   │       ├── __init__.py
│   │       ├── skill.py       # 技能核心模型
│   │       ├── evolution_record.py  # 进化记录模型
│   │       └── dependency_graph.py  # 技能依赖图
│   ├── evolution/             # 进化引擎
│   │   ├── __init__.py
│   │   ├── session_analyzer.py    # 会话分析器
│   │   ├── feedback_processor.py   # 反馈处理器
│   │   ├── pattern_miner.py      # 模式挖掘器
│   │   └── experience_store.py   # 经验存储 (JSON)
│   ├── loop/                 # 递归循环
│   │   ├── __init__.py
│   │   ├── bootstrap.py       # 创生阶段
│   │   ├── self_reflection.py # 自省阶段
│   │   ├── generation.py      # 创造阶段
│   │   └── recursive_loop.py # 循环阶段
│   ├── scripts/              # 可执行脚本
│   │   ├── alpha_generator.py # α-生成器入口
│   │   ├── omega_optimizer.py # Ω-优化器入口
│   │   └── recursive_evolver.py  # 递归进化控制器
│   └── cli.py               # 命令行界面
└── tests/                    # 测试目录
    ├── conftest.py
    ├── pytest.ini
    ├── test_models/
    ├── test_core/
    ├── test_evolution/
    └── test_loop/
```

---

## 开发原则

1. **不可变性**: 使用 frozen dataclasses 或 NamedTuple
2. **类型安全**: 所有函数必须有类型注解
3. **错误处理**: 显式错误处理，绝不静默吞噬
4. **模块化**: 小文件 (<800 行），高内聚低耦合
5. **测试驱动**: TDD 方法论，80%+ 覆盖率

---

## 实施阶段

### 第一阶段：项目初始化与基础结构

创建项目目录结构和核心模块框架，包括 memory-bank 文件。

**任务清单：**
1. 创建 `meta_skills/` 目录结构
2. 创建 `memory-bank/` 目录和初始文件
3. 创建 `__init__.py` 文件
4. 创建 `requirements.txt`
5. 初始化测试目录结构
6. 设置基本配置（`.ruff.toml`）

### 第二阶段：核心数据模型

定义技能、进化记录、依赖关系等核心数据模型。

**核心模型：**
- `Skill`: 技能核心模型（name, version, hash, metadata）
- `EvolutionRecord`: 进化记录模型
- `DependencyGraph`: 技能依赖图

### 第三阶段：生成器与优化器基类

定义 α-生成器（Generator）和 Ω-优化器（Optimizer）的抽象基类。

### 第四阶段：进化引擎

构建能够从对话历史、用户反馈和错误日志中学习的进化引擎。

### 第五阶段：递归自优化循环

实现元方法论的核心递归循环。

### 第六阶段：命令行界面

提供用户友好的 CLI 工具。

### 第七阶段：现有技能迁移

将现有三个技能重构到新框架。

---

## 风险评估

| 风险 | 等级 | 缓解措施 |
|------|------|----------|
| 递归循环可能无限执行或不收敛 | HIGH | 设置最大迭代次数、收敛阈值检测、人工确认机制 |
| 进化可能破坏现有技能 | MEDIUM | 完整的备份机制、版本回滚、集成测试 |
| 抽象层次过高，难以理解 | MEDIUM | 详细文档、示例代码、渐进式重构 |
| 性能开销较大 | LOW | 异步执行、增量更新、缓存优化 |

---

## 验证标准

### 功能验证
1. 初始化测试：运行 `meta-skills-skills init` 验证系统初始化
2. 生成测试：使用 α-生成器创建一个测试技能
3. 优化测试：使用 Ω-优化器分析技能库
4. 循环测试：触发一轮完整的进化循环
5. CLI 测试：验证所有 CLI 命令正常工作

### 测试覆盖率
- **总体覆盖率**: > 80%
- **核心模型覆盖率**: > 90%
- **关键路径覆盖率**: > 95%

---

## 预估复杂度：中高

- **项目初始化**: 1-2 小时
- **核心数据模型**: 3-4 小时
- **生成器与优化器**: 4-6 小时
- **进化引擎**: 5-7 小时
- **递归循环**: 4-5 小时
- **CLI 开发**: 3-4 小时
- **现有技能迁移**: 2-3 小时
- **测试与验证**: 4-6 小时
- **总计**: 26-37 小时
