# Meta-Skills 实施计划

> 基于 project-spec.md 和 tech-stack.md 的基础架构搭建计划
> 重点：初始化项目结构、核心系统骨架、基础测试
> Python 版本：3.10+

---

## 第一阶段：项目初始化与基础结构

### 步骤 1.1：创建项目根目录结构

**【具体操作】**
**时间估算：5分钟**

1. 在项目根目录下创建以下目录结构：
   - `meta_skills/` - 核心代码库
   - `meta_skills/core/` - 核心框架
   - `meta_skills/core/models/` - 数据模型
   - `meta_skills/evolution/` - 进化引擎
   - `meta_skills/loop/` - 递归循环
   - `meta_skills/scripts/` - 可执行脚本
   - `tests/` - 测试目录
   - `tests/test_models/` - 模型测试
   - `tests/test_core/` - 核心测试
   - `tests/test_evolution/` - 进化测试
   - `tests/test_loop/` - 循环测试

2. 创建所有 `__init__.py` 文件以形成有效的 Python 包

**【验证测试方法】**
- 验证所有目录已创建
- 验证所有 `__init__.py` 文件存在且为空
- 运行 `python -c "import meta_skills"` 验证包导入成功

---

### 步骤 1.2：创建配置文件

**【具体操作】**
**时间估算：10分钟**

1. 创建 `meta_skills/requirements.txt`：
   - 添加 pydantic>=2.0.0
   - 添加 networkx>=3.0
   - 添加 rich>=13.0.0
   - 添加 typer>=0.9.0
   - 添加 PyYAML>=6.0
   - 添加 aiofiles>=0.8.0
   - 添加 aiohttp>=3.0.0

2. 创建 `meta_skills/dev-requirements.txt`：
   - 添加 pytest>=7.0.0
   - 添加 pytest-cov>=4.0.0
   - 添加 pytest-asyncio>=0.21
   - 添加 ruff>=0.1.0

3. 创建 `meta_skills/.ruff.toml`：
   - 设置 line-length = 88
   - 设置 target-version = "py310"
   - 配置 lint 规则（E, W, F, I, B, C4, UP, ARG, SIM）
   - 配置格式化选项

4. 创建 `tests/pytest.ini`：
   - 配置测试文件发现模式
   - 配置覆盖率报告路径

5. 创建 `tests/conftest.py`：
   - 定义共享的 pytest fixtures（模拟数据）

**【验证测试方法】**
- 运行 `ruff check meta_skills/` 验证配置文件语法正确
- 运行 `pytest --version` 验证 pytest 可用
- 运行 `pytest tests/` 验证测试框架初始化成功（应无测试通过）

---

### 步骤 1.3：安装依赖并验证并验证环境

**【具体操作】**
**时间估算：5分钟**

1. 在项目根目录运行：
   - 安装生产依赖：`pip install -r meta_skills/requirements.txt`
   - 安装开发依赖：`pip install -r meta_skills/dev-requirements.txt`

2. 验证 Python 版本 >= 3.10

3. 验证所有依赖包正确安装

**【验证测试方法】**
- 运行 `python --version` 验证 Python 版本
- 运行 `pip list` 验证所有依赖已安装
- 运行 `ruff --version` 验证 ruff 可用
- 运行 `pytest --version` 验证 pytest 可用

---

## 第二阶段：核心数据模型

### 步骤 2.1：定义 Skill 数据模型

**【具体操作】**
**时间估算：10分钟**

1. 创建 `meta_skills/core/models/skill.py`：
   - 定义 Skill dataclass（使用 frozen=True）
   - 字段：name (str), version (str), hash (str), metadata (dict)
   - 添加完整的类型注解
   - 添加类方法用于从字典创建实例
   - 添加 to_dict 方法用于序列化

2. 遵循不可变性和类型安全原则

**【验证测试方法】**
- 创建 `tests/test_models/test_skill.py`
- 编写测试用例验证 Skill 实例创建
- 编写测试用例验证 to_dict 方法
- 运行 `pytest tests/test_models/test_skill.py -v`

---

### 步骤 2.2：定义 EvolutionRecord 数据模型

**【具体操作】**
**时间估算：10分钟**

1. 创建 `meta_skills/core/models/evolution_record.py`：
   - 定义 EvolutionRecord dataclass（frozen=True）
   - 字段：id (str), skill_name (str), timestamp (datetime), changes (list[str]), metrics (dict)
   - 添加完整的类型注解
   - 添加序列化和反序列化方法

2. 确保 datetime 字段使用 ISO 格式序列化

**【验证测试方法】**
- 创建 `tests/test_models/test_evolution_record.py`
- 编写测试用例验证实例创建
- 编写测试用例验证序列化/反序列化
- 运行 `pytest tests/test_models/test_evolution_record.py -v`

---

### 步骤 2.3：定义 DependencyGraph 数据模型

**【具体操作】**
**时间估算：15分钟**

1. 创建 `meta_skills/core/models/dependency_graph.py`：
   - 定义 DependencyGraph 类封装 networkx.DiGraph
   - 方法：add_skill, add_dependency, get_dependencies, get_dependents
   - 方法：detect_cycles, to_dict, from_dict
   - 所有方法添加类型注解

2. 使用 networkx 处理图算法

**【验证测试方法】**
- 创建 `tests/test_models/test_dependency_graph.py`
- 编写测试用例验证添加技能和依赖
- 编写测试用例验证循环检测
- 编写测试用例验证序列化/反序列化
- 运行 `pytest tests/test_models/test_dependency_graph.py -v`

---

## 第三阶段：生成器与优化器基类

### 步骤 3.1：定义 Generator 抽象基类

**【具体操作】**
**时间估算：15分钟**

1. 创建 `meta_skills/core/generator.py`：
   - 定义 Generator 抽象基类
   - 抽象方法：generate(user_request: str) -> Skill
   - 抽象方法：validate_template(template: dict) -> bool
   - 添加类型注解和文档字符串
   - 定义基础属性和构造函数

2. 使用 abc.ABC 和 @abstractmethod

**【验证测试方法】**
- 创建 `tests/test_core/test_generator.py`
- 编写测试验证抽象方法不能直接实例化
- 编写测试验证子类必须实现所有抽象方法
- 运行 `pytest tests/test_core/test_generator.py -v`

---

### 步骤 3.2：定义 Optimizer 抽象基类

**【具体操作】**
**时间估算：15分钟**

1. 创建 `meta_skills/core/optimizer.py`：
   - 定义 Optimizer 抽象基类
   - 抽象方法：analyze(skill: Skill) -> AnalysisResult
   - 抽象方法：optimize(skill: Skill, analysis: AnalysisResult) -> Skill
   - 抽象方法：suggest_improvements(skill: Skill) -> list[str]
   - 添加完整的类型注解

2. 定义 AnalysisResult dataclass：
   - 字段：score (float), analysis_details (dict), issues (list[str]), recommendations (list[str])
   - 使用 frozen=True

**【验证测试方法】**
- 创建 `tests/test_core/test_optimizer.py`
- 编写测试验证抽象类行为
- 编写测试验证 AnalysisResult 模型
- 运行 `pytest tests/test_core/test_optimizer.py -v`

---

### 步骤 3.3：定义 EvolutionCycle 管理类

**【具体操作】**
**时间估算：15分钟**

1. 创建 `meta_skills/core/evolution_cycle.py`：
   - 定义 EvolutionCycle 类
   - 方法：start_cycle(generator: Generator, optimizer: Optimizer) -> EvolutionRecord
   - 方法：record_evolution(record: EvolutionRecord) -> None
   - 方法：get_history(skill_name: str) -> list[EvolutionRecord]
   - 添加类型注解和错误处理

2. 实现基本的周期追踪逻辑

**【验证测试方法】**
- 创建 `tests/test_core/test_evolution_cycle.py`
- 编写测试验证周期启动和记录
- 编写测试验证历史查询
- 运行 `pytest tests/test_core/test_evolution_cycle.py -v`

---

## 验收标准

### 结构验证
- 所有目录结构符合 project-spec.md 定义
- 所有配置文件格式正确
- 所有 `__init__.py` 文件存在

### 功能验证
- 所有数据模型可通过测试
- 抽象基类设计正确
- 类型注解完整

### 代码质量验证
- 运行 `ruff check meta_skills/` 无错误
- 运行 `pytest tests/ --cov=meta_skills --cov-report=term-missing`
- 测试覆盖率 >= 80%

---

## 后续阶段（本计划不包含）

- 第四阶段：进化引擎（experience_store, session_analyzer, feedback_processor, pattern_miner）
- 第五阶段：递归自自优化循环（bootstrap, self_reflection, generation, recursive_loop）
- 第六阶段：命令行界面（CLI）
- 第七阶段：现有技能迁移
