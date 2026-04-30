# whohoo/mcp_server_weibo

An MCP (Model Context Protocol) server for interacting with Weibo (Sina Weibo), the Chinese microblogging platform. Provides tools for searching users, fetching feeds, getting trending topics, and more.

**Source Code:** https://github.com/whohoo/mcp-server-weibo

## Supported Platforms

- `linux/amd64`
- `linux/arm64`

## Quick Start

```bash
docker run -d \
  --name weibo-mcp \
  -p 4200:4200 \
  whohoo/mcp_server_weibo
```

The container runs in **HTTP mode** by default and listens on port `4200`.

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | `4200` | HTTP server listening port. Override to change the port inside the container. |

## Docker Compose

```yaml
services:
  weibo_mcp:
    image: whohoo/mcp_server_weibo
    container_name: mcp-server-weibo
    restart: unless-stopped
    ports:
      - "4200:4200"
    environment:
      - PORT=4200
```

## MCP Client Configuration

Configure your MCP client (e.g., Claude Desktop, Cursor, Windsurf) to connect to the HTTP endpoint:

```json
{
  "mcpServers": {
    "weibo": {
      "url": "http://localhost:4200/mcp"
    }
  }
}
```

## Available MCP Tools

| Tool | Description |
|------|-------------|
| `search_users` | Search for Weibo users by keyword |
| `get_profile` | Get a user's profile by UID |
| `get_feeds` | Get a user's recent posts |
| `get_hot_feeds` | Get a user's hot posts |
| `get_trendings` | Get current trending / hot search topics |
| `search_content` | Search Weibo posts by keyword |
| `search_topics` | Search topics by keyword |
| `get_followers` | Get a user's followers |
| `get_fans` | Get a user's fans |
| `get_comments` | Get comments on a post |
