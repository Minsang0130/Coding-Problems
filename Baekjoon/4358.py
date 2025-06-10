from collections import defaultdict
import sys

def main():
    data = sys.stdin.read().splitlines()
    tree_dict = defaultdict(int)
    count = 0

    for name in data:
        tree_dict[name] += 1
        count += 1
    
    for key, value in sorted(tree_dict.items()):
        print(f"{key} {value/count * 100:.4f}") 

if __name__ == "__main__":
    main()