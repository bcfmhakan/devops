import yaml
import argparse

parser = argparse.ArgumentParser()
path = parser.add_argument("-p", "--path", help="YAML Path - String", type=str)
tag = parser.add_argument("-t", "--tag", help="Tag Value - Integer", type=int)
args = parser.parse_args()

with open(f"{args.path}", "r") as file:
    try:
        f = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(exc)

f["deploy"]["tag"] = args.tag

with open(f"{args.path}", "w") as output:
    yaml.dump(f, output)