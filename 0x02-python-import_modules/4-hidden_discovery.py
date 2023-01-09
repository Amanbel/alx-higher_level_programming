#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    func_list = dir(hidden_4)
    for i in func_list:
        if i[0] != '_':
            print(i)
