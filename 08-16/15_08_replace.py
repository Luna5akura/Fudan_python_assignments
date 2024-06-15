import re

pattern = r"\w+@"


def main():
    with open("email_text.txt", encoding="gbk") as f:
        content = f.read()

    matches = re.findall(pattern, content)

    with open("extracted_emails.txt", "w", encoding="gbk") as f:
        for match in matches:
            f.write(match + "[protected]\n")


if __name__ == "__main__":
    main()
