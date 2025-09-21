import re


def main():
    # Output youtube URL.
    print(parse(input("HTML: ")))


# Convert html to youtube URL.
def parse(s):
    pattern = r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(?P<video_id>\w*)".*</iframe>'
    if match := re.search(pattern, s):
        return "https://youtu.be/" + match.group("video_id")
    else:
        return None


if __name__ == "__main__":
    main()
