#!/bin/bash
. venv/bin/activate
cd src
uvicorn api:app --reload