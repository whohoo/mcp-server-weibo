# Weibo CLI Skills

## Overview

The `weibo-cli` is a command-line interface tool for interacting with Weibo data without using the MCP protocol. It provides direct access to all Weibo functionality through simple terminal commands.

## How It Works

### Architecture

```
User Terminal
     |
     v
weibo-cli (Click-based CLI)
     |
     v
WeiboCrawler (weibo.py)
     |
     v
Weibo API (m.weibo.cn)
     |
     v
Auto-generated Cookies (Visitor Passport)
```

### Cookie Auto-Generation

Unlike traditional approaches that require manual cookie configuration, `weibo-cli` uses Weibo's visitor passport system to automatically generate valid access credentials:

1. On first request, `_ensure_cookies()` is called
2. It makes a request to `https://visitor.passport.weibo.cn/visitor/genvisitor2`
3. The response contains `SUB` and `SUBP` tokens
4. These tokens are validated before use
5. Cookies are stored in the `WeiboCrawler` instance for subsequent requests

### Installation

```bash
# Run directly with uvx (recommended)
uvx weibo-cli --help

# Or install from PyPI
pip install mcp-server-weibo
```

## CLI Commands

### profile

Get user profile information by UID.

```bash
weibo-cli profile <UID>
```

**Example:**
```bash
weibo-cli profile 1749127163
```

**Output:** JSON object with user details (id, screen_name, description, followers_count, etc.)

### feeds

Get user posts (weibo feeds).

```bash
weibo-cli feeds <UID> [-n LIMIT]
```

**Example:**
```bash
weibo-cli feeds 1749127163 -n 10
```

**Output:** JSON array of feed items with text, source, created_at, comments_count, attitudes_count, reposts_count, etc.

### search

Search for posts containing specific keywords.

```bash
weibo-cli search <KEYWORD> [-n LIMIT] [-p PAGE]
```

**Example:**
```bash
weibo-cli search "人工智能" -n 20 -p 1
```

**Output:** JSON array of matching posts with user info, timestamps, and engagement metrics.

### users

Search for Weibo users by keyword.

```bash
weibo-cli users <KEYWORD> [-n LIMIT] [-p PAGE]
```

**Example:**
```bash
weibo-cli users "科技" -n 10
```

**Output:** JSON array of user profiles matching the search term.

### topics

Search for Weibo topics (hashtags).

```bash
weibo-cli topics <KEYWORD> [-n LIMIT] [-p PAGE]
```

**Example:**
```bash
weibo-cli topics "演唱会" -n 10
```

**Output:** JSON array of topic items with title, description, and URL.

### trending

Get current trending/hot search items.

```bash
weibo-cli trending [-n LIMIT]
```

**Example:**
```bash
weibo-cli trending -n 15
```

**Output:** JSON array of trending items with rank, description, and热度值.

### comments

Get comments for a specific post.

```bash
weibo-cli comments <FEED_ID> [-p PAGE]
```

**Example:**
```bash
weibo-cli comments 5173507416919189 -p 1
```

**Output:** JSON array of comments with user info, text, and timestamps.

### followers

Get a user's followers.

```bash
weibo-cli followers <UID> [-n LIMIT] [-p PAGE]
```

**Example:**
```bash
weibo-cli followers 1749127163 -n 20
```

**Output:** JSON array of user profiles who follow this user.

### fans

Get a user's fans (people who follow this user).

```bash
weibo-cli fans <UID> [-n LIMIT] [-p PAGE]
```

**Example:**
```bash
weibo-cli fans 1749127163 -n 20
```

**Output:** JSON array of user profiles who are fans of this user.

## Common Options

| Option | Description | Default |
|--------|-------------|---------|
| `-n, --limit` | Maximum number of results | varies by command |
| `-p, --page` | Page number for pagination | 1 |

## Exit Codes

- `0`: Success
- `1`: Error (network failure, invalid arguments, etc.)

## Error Handling

All errors are logged to stderr and displayed as error messages. The CLI will exit with code 1 if any operation fails.

## Tips

1. **Pagination**: Use `-p` option to navigate through multiple pages of results
2. **Result Limits**: Use `-n` option to control how many results to fetch
3. **JSON Output**: All results are output as formatted JSON for easy parsing
4. **Async Operations**: Each command runs asynchronously, so multiple commands can be executed in sequence

## See Also

- [MCP Server README](../src/mcp_server_weibo/README.md) - MCP protocol usage
- [Weibo API Documentation](https://m.weibo.cn/)