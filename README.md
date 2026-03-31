# Weibo MCP Server 🚀

基于 Model Context Protocol 的微博数据接口服务器 - 实时获取微博用户信息、动态内容、热搜榜单、粉丝关注数据。支持用户搜索、内容搜索、话题分析，为 AI 应用提供完整的微博数据接入方案。

<a href="https://glama.ai/mcp/servers/@qinyuanpei/mcp-server-weibo">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/@qinyuanpei/mcp-server-weibo/badge" alt="Weibo Server MCP server" />
</a>

[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/qinyuanpei-mcp-server-weibo-badge.png)](https://mseep.ai/app/qinyuanpei-mcp-server-weibo)

## 安装

**Cookie 自动获取：** 无需手动配置 Cookie，程序会自动通过微博访客通行证生成有效的访问凭证。

从源代码安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": [
                "--from",
                "git+https://github.com/qinyuanpei/mcp-server-weibo.git",
                "mcp-server-weibo"
            ]
        }
    }
}
```
从包管理器安装：

```json
{
    "mcpServers": {
        "weibo": {
            "command": "uvx",
            "args": ["mcp-server-weibo"],
        }
    }
}
```

## 命令行工具 (CLI)

除了 MCP 服务器，还提供了独立的命令行工具可直接访问：

```bash
# 安装
pip install -e .

# 查看帮助
weibo-cli --help

# 获取用户资料
weibo-cli profile 1749127163

# 获取用户动态
weibo-cli feeds 1749127163 -n 10

# 搜索内容
weibo-cli search "关键词"

# 搜索用户
weibo-cli users "关键词"

# 搜索话题
weibo-cli topics "关键词"

# 获取热搜榜单
weibo-cli trending -n 10

# 获取评论
weibo-cli comments 5173507416919189

# 获取粉丝
weibo-cli followers 1749127163 -n 10

# 获取关注
weibo-cli fans 1749127163 -n 10
```

### CLI 命令列表

| 命令 | 说明 |
|------|------|
| `weibo-cli profile <uid>` | 根据 UID 获取用户资料 |
| `weibo-cli feeds <uid> [-n N]` | 获取用户动态 |
| `weibo-cli search <关键词> [-n N] [-p P]` | 按关键词搜索帖子 |
| `weibo-cli users <关键词> [-n N] [-p P]` | 按关键词搜索用户 |
| `weibo-cli topics <关键词> [-n N] [-p P]` | 按关键词搜索话题 |
| `weibo-cli trending [-n N]` | 获取热搜榜单 |
| `weibo-cli comments <feed_id> [-p P]` | 获取帖子评论 |
| `weibo-cli followers <uid> [-n N] [-p P]` | 获取用户粉丝 |
| `weibo-cli fans <uid> [-n N] [-p P]` | 获取用户关注 |

## 组件

### 工具

- `search_weibo_users`: 用于搜索微博用户
    - **输入:** `keyword`: 搜索关键词
    - **输出:** `WeiboUsers`: 包含用户基本信息的 Pydantic 模型列表

- `extract_weibo_profile`: 获取用户详细信息
    - **输入:** `user_id`: 用户ID
    - **输出:** `WeiboProfile`: 包含用户详细信息的 Pydantic 模型

- `extract_weibo_feeds`: 获取用户动态
    - **输入:** `user_id`: 用户ID, `limit`: 获取数量限制
    - **输出:** `WeiboFeeds`: 包含用户动态信息的 Pydantic 模型列表

### 资源   

无

### 提示

无

## 依赖要求

- Python >= 3.8
- httpx >= 0.24.0
- pydantic >= 2.0.0
- fastmcp >= 0.1.0

## 许可证

MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 免责声明

本项目与微博官方无关，仅用于学习和研究目的。
