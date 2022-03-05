import re

def main():
    reg = re.compile("^\[[A-Z]{2,5}\-\d+\]\s.*$")

    print(reg.match("[JIRA-1223]Hello world"))
    print(reg.match("[JIRA-1223] Hello world"))


if __name__ == "__main__":
    main()
