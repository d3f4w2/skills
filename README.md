# Skills

## 概述

Meta-Skills 是一个递归自我优化的 AI 技能管理系统。

## 快速开始

### 1. 克隆仓库（如果需要）

```bash
git clone https://github.com/d3f4w2/skills.git
cd skills
```

### 2. 创建并激活虚拟环境（可选）

```bash
python -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r meta_skills/requirements.txt
pip install -r meta_skills/dev-requirements.txt
```

### 4. 查看文档

```bash
cat memory-bank/project-spec.md
cat CLAUDE.md
```

## 项目结构

```
meta_skills/
├── core/                     # 核心框架
│   ├── models/               # 数据模型
│   ├── generator.py          # Generator 抽象基类
│   ├── optimizer.py          # Optimizer 抽象基类
│   └── evolution_cycle.py    # EvolutionCycle 管理类
├── evolution/               # 进化引擎（待实现）
├── loop/                   # 递归循环（待实现
└── scripts/                 # 可执行脚本（待实现）

tests/
├── conftest.py              # 测试 fixtures
├── pytest.ini                # Pytest 配置
├── test_models/              # 模型测试
├── test_core/                # 核心测试
├── test_evolution/           # 进化测试
└── test_loop/                # 循环测试
```

## 下一步

1. 安装依赖并验证环境
2. 开始实现核心数据模型
