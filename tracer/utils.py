from tracer.config import TracerConfig


def build_params(cfg: TracerConfig):
    return {
        'subreddit': cfg.subreddit_name,
        'after': cfg.start_timestamp,
        'before': cfg.end_timestamp,
        'size': 1000,
        'fields': ['id', 'body', 'author', 'created_utc', 'permalink'], # TODO: verify if more fields are needed
        'sort_type': 'created_utc'
    }
