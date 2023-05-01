from collections import Counter, defaultdict, OrderedDict

def main() -> None:
    
    li = [1,2,3,4,5,6,7,7]
    
    # Example of Counter class
    # Counts repetitions in an iterable
    cnt_list = Counter(li)
    
    print(cnt_list)
    
    # They also work for strings
    sentence = "This is some random sentence"
    
    cnt_str = Counter(sentence)
    
    print(cnt_str)
    
    # Default Dict provides us of a default function that returns value for nonexisting keys
    dictionary = defaultdict(lambda: "value does not exist",{"a": 1, "b": 2})
    print(dictionary['c']) 
    
    # Ordered Dict Example
    d = OrderedDict()
    d['a'] = 1
    d['b'] = 2
    
    d2 = OrderedDict()
    d2['b'] = 2
    d2['a'] = 1
    
    print(d)
    print(d2)
    print(d == d2)
    

if __name__ == "__main__":
    main()