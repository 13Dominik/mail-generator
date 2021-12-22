#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
proxy_http = os.environ.get("proxy_http", "default")


def is_proxy() -> bool:
    if proxy_http == "default":
        return False
    return True
