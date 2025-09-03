#!/usr/bin/env python3
"""
knock_knock.py
A tiny Python script that prints a classic knock-knock joke.
Run with: python knock_knock.py
"""

def main():
    lines = [
        "Knock, knock.",
        "Who's there?",
        "Lettuce.",
        "Lettuce who?",
        "Lettuce in — it's cold out here!"
    ]
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()
