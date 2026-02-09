"""Pytest 共享 fixtures 用于 Meta-Skills 项目测试。"""

import pytest
from datetime import datetime
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MockSkill:
    """模拟 Skill 数据模型"""
    name: str
    version: str
    hash: str
    metadata: dict[str, str]


@dataclass(frozen=True)
class MockEvolutionRecord:
    """模拟 EvolutionRecord 数据模型"""
    id: str
    skill_name: str
    timestamp: datetime
    changes: list[str]
    metrics: dict[str, float]


@dataclass(frozen=True)
class MockAnalysisResult:
    """模拟 AnalysisResult 数据模型"""
    score: float
    analysis_details: dict[str, str]
    issues: list[str]
    recommendations: list[str]


@pytest.fixture
def sample_skill():
    """提供示例 Skill 实例"""
    return MockSkill(
        name="test-skill",
        version="1.0.0",
        hash="abc123",
        metadata={"description": "Test skill", "author": "Claude"}
    )


@pytest.fixture
def sample_evolution_record():
    """提供示例 EvolutionRecord 实例"""
    return MockEvolutionRecord(
        id="ev-001",
        skill_name="test-skill",
        timestamp=datetime.now(),
        changes=["Updated description", "Added documentation"],
        metrics={"success_rate": 0.95, "performance": 0.85}
    )


@pytest.fixture
def sample_analysis_result():
    """提供示例 AnalysisResult 实例"""
    return MockAnalysisResult(
        score=0.85,
        analysis_details={"complexity": "medium", "lines_of_code": 150},
        issues=["Missing error handling", "No type hints"],
        recommendations=["Add error handling", "Add type hints"]
    )


@pytest.fixture
def temp_data_dir(tmp_path):
    """提供临时目录路径用于文件操作测试"""
    import os
    data_dir = os.path.join(tmp_path, "data")
    os.makedirs(data_dir, exist_ok=True)
    return data_dir
