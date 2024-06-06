from DS.linkedList.UnorderedList import UnorderedList

if __name__ == "__main__":
    unordered_list = UnorderedList()
    unordered_list.add(4)
    unordered_list.add(8)
    unordered_list.add(15)
    unordered_list.add(16)
    unordered_list.add(23)
    unordered_list.add(42)
    print(unordered_list.size())
    print(unordered_list.find(4))
    unordered_list.show()
    print(unordered_list.remove(4))
    unordered_list.show()
    print(unordered_list.remove(42))
    unordered_list.show()







