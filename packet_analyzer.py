from compute_metrics import compute

files = ['Node1.txt', 'Node2.txt', 'Node3.txt', 'Node4.txt']

def main():
    for f in files:
        compute(f)

if __name__ == '__main__':
    main()