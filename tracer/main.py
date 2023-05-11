from tracer.utils import build_params
from tracer.config import cfg
from tracer.comments import extract_comments


if __name__ == '__main__':
    params = build_params(cfg)
    extract_comments(params)
