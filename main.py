from src import parser
import argparse

p = argparse.ArgumentParser()
p.add_argument("inputFile", help="file to be processed")
args = p.parse_args()

f = open(args.inputFile)
try:
    lines = f.readlines()
    # find a nicer way to read the entire file
    content = "".join(lines)

    content = parser.parse(content)

    sqls = map(lambda s: s.toSQL(), content)
    for sql in sqls:
        print(sql + '\n')

finally:
    f.close()