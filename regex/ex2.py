import re

def main() -> None:
    
    pattern = re.compile(r"([a-zA-Z]).(a)")
    sentence = "Search inside of this text please!"
    
    a = pattern.search(sentence)
    b = pattern.findall(sentence)
    c = pattern.fullmatch(sentence)
    d = pattern.match(sentence)
    
    print(a.group())
    print(b)
    print(c)
    print(d)


if __name__ == "__main__":
    main()