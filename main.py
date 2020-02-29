import argparse
import hashlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('hashfile')
    parser.add_argument('potfile')
    args = parser.parse_args()
    with open(args.hashfile) as file:
        hashes = set(file.read().splitlines())
    
    with open(args.potfile) as file:
        potfile = file.read().splitlines()
    
    correct = set()
    for line in potfile:
        hash_, _, pass_ = line.partition(':')
        if hash_ in hashes:
            if hashlib.md5(pass_.encode()).hexdigest() == hash_:
                correct.add(line)
                hashes.remove(hash_)
            else:
                print('Error: %s hashes to %s, but file says it hashes to %s'
                      % (pass_, hashlib.md5(pass_.encode()).hexdigest(), hash_))
    with open('%s_found.txt' % len(correct), 'w') as file:
        file.write('\n'.join(sorted(correct)) + '\n')
    with open('%s_left.txt' % len(hashes), 'w') as file:
        file.write('\n'.join(sorted(hashes)) + '\n')


if __name__ == '__main__':
    main()
