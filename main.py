import argparse
import codecs
import onymize

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()
    with codecs.open(args.source, 'r', encoding='utf8') as f:
        text = f.read()
    onymize.choose_onymize(text, False)
