# Meta-Skills 架构文档

> 记录项目架构设计和文件职责

---

## 架构概览

```
meta_skills/
├── core/                     # 核心框架
│   ├── models/               # 数据模型
│   │   ├── skill.py         # Skill 数据模型
│   │   ├── evolution_record.py  # EvolutionRecord 数据模型
│   │   └── dependency_graph.py # DependencyGraph 类
│   ├── generator.py          # Generator 抽象基类
│   ├── optimizer.py          # Optimizer 抽象基类
│   └── evolution_cycle.py    # EvolutionCycle 管理类
├── evolution/               # 进化引擎（待实现）
├── loop/                   # 递归循环（待实现）
└── scripts/                 # 可执行脚本（待实现）
```

---

## 环境配置

### Conda 虚拟环境
- **环境名称**: meta-skills
- **Python 版本**: 3.10.19
- **环境位置**: C:\Users\ljh\.conda\envs\meta-skills

### 激活环境

每次开发前需要激活虚拟环境：

**Windows:**
```bash
conda activate meta-skills
```

**或使用 conda run:**
```bash
conda run -n meta-skills <command>
```

### 依赖版本

**生产依赖：**
- pydantic 2.12.5
- pydantic-core 2.41.5
- networkx 3.4.2
- rich 14.3.2
- typer 0.21.1
- PyYAML 6.0.3
- aiofiles 25.1.0
- aiohttp 3.13.3

**开发依赖：**
- pytest 9.0.2
- pytest-cov 7.0.0
- pytest-asyncio 1.3.0
- ruff 0.15.0

### 环境变量（可选）

可以通过环境变量配置存储路径：
- `META_SKILLS_DATA_DIR`: 数据存储目录（默认：./data）

---

## 核心模块职责

### core/models/skill.py
- **职责**: 定义技能核心数据结构
- **字段**: name, version, hash, metadata
- **方法**: from_dict, to_dict

### core/models/evolution_record.py
- **职责**: 记录技能进化历史
- **字段**: id, skill_name, timestamp, changes (list[str]), metrics
- **方法**: 序列化/反序列化

### core/models/dependency_graph.py
- **职责**: 管理技能间的依赖关系
- **方法**: add_skill, add_dependency, detect_cycles

### core/generator.py
- **职责**: 定义 α-生成器抽象接口
- **抽象方法**: generate, validate_template

### core/optimizer.py
- **职责**: 定义 Ω-优化器抽象接口
- **抽象方法**: analyze, optimize, suggest_improvements
- **数据模型**: AnalysisResult (score, analysis_details, issues, recommendations)

### core/evolution_cycle.py
- **职责**: 管理进化周期和记录
- **方法**: start_cycle, record_evolution, get_history

---

## 数据流

```
用户请求 → Generator.generate() → Skill
Skill → Optimizer.analyze() → AnalysisResult
AnalysisResult → Optimizer.optimize() → Evolved Skill
Evolved Skill → EvolutionCycle.record_evolution() → EvolutionRecord
```

---

## 依赖关系

- Generator 和 Optimizer 独立运作
- EvolutionCycle 依赖 Generator 和 Optimizer
- 所有组件依赖数据模型

---

## 设计原则

1. **不可变性**: 所有数据模型使用 frozen dataclass
2. **类型安全**: 所有函数有完整类型注解
3. **高内聚低耦合**: 每个模块职责单一
4. **模块化**: 小文件，每个文件 <800 行

---

## 数据存储

- 使用 JSON 文件存储经验数据
- 存储位置: `evolution/experience_store.py` (待实现)

---

## 配置文件（已创建）

### meta_skills/requirements.txt
- 核心依赖：pydantic, networkx, rich, typer, PyYAML
- 异步支持：aiofiles, aiohttp

### meta_skills/dev-requirements.txt
- 开发依赖：pytest, pytest-cov, pytest-asyncio, ruff

### meta_skills/.ruff.toml
- 配置：line-length=88, target-version=py310
- Lint 规则：E, W, F, I, B, C4, UP, ARG, SIM
- 格式化：double quotes, space indent

### tests/pytest.ini
- 测试部：source=meta_skills, branch=true
- 覆盖率：exclude tests/*

### tests/conftest.py
- 共享 fixtures：MockSkill, MockEvolutionRecord, MockAnalysisResult
- 临时目录 fixture：temp_data_dir
