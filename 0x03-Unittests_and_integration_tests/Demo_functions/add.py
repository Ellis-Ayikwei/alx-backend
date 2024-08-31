#!/usr/bin/env pyhton3


def add(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int) :
        raise TypeError("an put is not supported")
    else:
        return x + y 



if __name__ == "__main__":
    print(add(56, "78"))