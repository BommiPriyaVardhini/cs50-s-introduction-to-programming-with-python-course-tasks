import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match YouTube embed URLs in iframe src attributes
    match = re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None

if __name__ == "__main__":
    main()
