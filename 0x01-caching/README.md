# Caching System Project

This project covers different caching algorithms and their implementations.

---

## Table of Contents

- [Background Context](#background-context)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Caching Classes](#caching-classes)
  - [Basic Dictionary](#0-basic-dictionary)
  - [FIFO Caching](#1-fifo-caching)
  - [LIFO Caching](#2-lifo-caching)
  - [LRU Caching](#3-lru-caching)
  - [MRU Caching](#4-mru-caching)

---

## Background Context

In this project, you learn different caching algorithms such as FIFO, LIFO, LRU, MRU, and LFU.

### Resources

- Cache replacement policies - FIFO
- Cache replacement policies - LIFO
- Cache replacement policies - LRU
- Cache replacement policies - MRU
- Cache replacement policies - LFU

---

## Learning Objectives

By the end of this project, you should be able to explain the following without the help of Google:

- What is a caching system?
- What do FIFO, LIFO, LRU, MRU, and LFU mean?
- What is the purpose of a caching system?
- What limits a caching system?

---

## Requirements

- Python 3.7, tested on Ubuntu 18.04 LTS.
- Code follows the `pycodestyle` style guide (version 2.5).
- All files are executable and end with a new line.
- Modules, classes, and functions are documented.

---

## Caching Classes

### 0. Basic Dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and implements a basic caching system.

```python
#!/usr/bin/env python3
""" Basic dictionary caching """

class BaseCaching:
    """ BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data.get(key)}")

    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your cache class")

class BasicCache(BaseCaching):
    """ BasicCache defines a caching system without limit """

    def put(self, key, item):
        """ Assign to the dictionary cache_data the item value for the key key """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key """
        return self.cache_data.get(key) if key else None
