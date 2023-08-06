import httpx
import logging
import mugmoment.converters

__version__ = "0.1.0"
__all__ = ["converters"]

# Default client ID from twitch web UI
default_headers = {"Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko"}


def fetch_raw(vod_id: int) -> dict:
    """Fetch raw chat log array from twitch API"""
    page_counter = 1
    base_url = f"https://api.twitch.tv/v5/videos/{vod_id}/comments"

    req = httpx.get(base_url, headers=default_headers)
    reqj = req.json()

    comments = reqj["comments"]

    while reqj.get("_next"):
        page_counter += 1
        url = f"{base_url}?cursor={reqj['_next']}"
        logging.debug(f"Fetching {url}, page {page_counter}.")

        req = httpx.get(url, headers=default_headers)
        reqj = req.json()

        comments += reqj["comments"]
        logging.debug(f"{comments[-1]['content_offset_seconds']} seconds of offset")
    return comments


def fetch_simple(vod_id: int) -> dict:
    """Fetch a simple chat log array"""
    raw_log = fetch_raw(vod_id)
    return mugmoment.converters.ttv_raw_to_simple_format(raw_log)


def fetch_txt(vod_id: int) -> str:
    """Fetch a simple text-only chat log"""
    raw_log = fetch_raw(vod_id)
    return mugmoment.converters.ttv_raw_to_txt(raw_log)


def fetch_html(vod_id: int) -> str:
    """Fetch a simple HTML chat log"""
    raw_log = fetch_raw(vod_id)
    return mugmoment.converters.ttv_raw_to_html(raw_log)
