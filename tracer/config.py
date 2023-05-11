import datetime as dt

from pydantic import BaseSettings


class TracerConfig(BaseSettings):
    subreddit_name: str

    tracer_start_time: str
    tracer_end_time: str

    pushshift_api_url: str = 'https://api.pushshift.io/reddit/comment/search'

    @property
    def start_timestamp(self):
        """
        Convert the user defined start_time string to a int timestamp.
        """
        datetime_obj = dt.datetime.fromisoformat(self.tracer_start_time)
        return int(datetime_obj.timestamp())

    @property
    def end_timestamp(self):
        """
        Convert the user defined end_time string to a int timestamp.
        """
        datetime_obj = dt.datetime.fromisoformat(self.tracer_end_time)
        return int(datetime_obj.timestamp())


cfg = TracerConfig()
