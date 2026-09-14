import argparse


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args()
    name_stripped = a.name.strip()
    if not name_stripped:
        raise SystemExit(2)
    print(f"Hello, {a.name}!")
