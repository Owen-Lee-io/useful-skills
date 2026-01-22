---
name: skill-editor-sop
description: 当用户需要创建、编辑、管理 Agent Skills 时使用此技能。提供标准化的操作流程和最佳实践指导。
user-invocable: true
---

# Agent Skills 编辑标准操作流程 (Meta-Skill)

## 核心指令

### 1. 技能创建流程
当用户要创建新技能时，严格按照以下步骤执行：

1. **确定技能类型和存放位置**
   - 项目专用：`.claude/skills/`
   - 个人全局：`~/.claude/skills/`
   - VS Code：`.github/skills/`
   - Cursor：`.cursor/skills/`

2. **创建目录结构**
   ```bash
   mkdir -p [位置]/[技能名称]
   cd [位置]/[技能名称]

