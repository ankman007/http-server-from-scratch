## Project Intro

A minimal HTTP web server built from scratch using Python sockets that serves static HTML, CSS & image files without using any web framework. It handles raw HTTP requests directly over sockets and implements basic routing serving all static assets from a static/ directory. Logs and client connections are displayed in the terminal using the Loguru library.

## Local Setup Guide

1. Create virtual enviroment 
2. Install required dependencies using command `pip install -r requirements.txt`
2. Run server `python main.py`

## How it works
1. Creates a TCP socket server
2. Listens on port 8000
3. Accepts incoming HTTP requests
4. Parses:
    - Method (GET)
    - Path (/)
5. Serves matching static file
6. Sends raw HTTP response back to browser

## Example Logs
```text
2026-06-07 14:24:49.533 | INFO     | run:start_server:11 - Listening on 0.0.0.0:8000
2026-06-07 14:24:53.299 | INFO     | run:start_server:17 - New connection from 127.0.0.1:62227
2026-06-07 14:24:53.300 | INFO     | run:start_server:29 - 127.0.0.1 - - "GET / HTTP/1.1"
2026-06-07 14:24:53.565 | INFO     | run:start_server:17 - New connection from 127.0.0.1:65475
2026-06-07 14:24:53.566 | INFO     | run:start_server:29 - 127.0.0.1 - - "GET /style.css HTTP/1.1"
2026-06-07 14:24:53.645 | INFO     | run:start_server:17 - New connection from 127.0.0.1:55072
```
