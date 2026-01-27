# Default HTTP headers for Weibo API requests
DEFAULT_HEADERS = { 
    'Content-Type': 'application/json', 
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15',
    'Referer': 'https://m.weibo.cn/',
}

# URL template for fetching user profile information
# {userId} will be replaced with the actual user ID
PROFILE_URL = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={userId}'

# URL template for fetching user's Weibo feeds
# {userId}: User's unique identifier
# {containerId}: Container ID for the user's feed
# {sinceId}: ID of the last feed for pagination
FEEDS_URL = 'https://m.weibo.cn/api/container/getIndex?type=uid&value={userId}&containerid={containerId}&since_id={sinceId}'

# URL for searching users, posts, topics and trending
SEARCH_URL = 'https://m.weibo.cn/api/container/getIndex'

# URL template for fetching comments of a specific Weibo post
# {feed_id}: The ID of the Weibo post
# {page}: The page number for pagination
COMMENTS_URL = 'https://m.weibo.cn/api/comments/show?id={feed_id}&page={page}'
