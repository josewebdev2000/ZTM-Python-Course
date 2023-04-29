from SuperList import SuperList

def main() -> None:
    super_list1 = SuperList()
    print(super_list1)
    
    super_list1.append(5)
    print(super_list1)
    
    print(len(super_list1))
    
    # print(issubclass(super_list1, list))

if __name__ == "__main__":
    main()