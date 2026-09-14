#!/usr/bin/env bash
set -e

echo "=== ruff format check ==="
ruff format --check

echo "=== ruff lint check ==="
ruff check

echo "=== pytest run ==="
pytest
