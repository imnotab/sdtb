#!/usr/bin/env bash
set -e

curl -fsS http://127.0.0.1:8000/packages.json > raw.json

jq -r '
  map(select(.status=="active" and .downloads >= 100))
  | sort_by(-.downloads, .name)
  | "name|version|downloads",
    "---|---|---",
    (.[] | "\(.name)|\(.version)|\(.downloads)")
' raw.json > table.tmp

cat > summary.md <<MD
# Active Packages Report

$(cat table.tmp)
MD

rm -f raw.json table.tmp
