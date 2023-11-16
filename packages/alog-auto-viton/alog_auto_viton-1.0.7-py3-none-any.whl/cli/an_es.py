import argparse
import json
import sys

from es_util.ESTOOL import ES


def main():
    parser = argparse.ArgumentParser(description='an es data cmd')
    parser.add_argument(
        "-id", "--kol_id", dest="kol_id", help="entry kol_id"
    )
    parser.add_argument(
        "-env", "--env", dest="env", help="entry env"
    )
    parser.add_argument(
        "-region", "--region", dest="region", help="entry region"
    )
    args = parser.parse_args()
    env, region, kol_id = 'live', 'id', 0
    if args.env:
        env = args.env
    if args.region:
        region = args.region
    if args.kol_id:
        kol_id = args.kol_id

    if kol_id == 0:
        print(json.dumps({"msg": "param error,kol_id must input", "code": -1}, indent=4))
        sys.exit(-1)

    data = ES(env, region).callES(kol_id)
    if data:
        print(json.dumps(data, indent=4))
    sys.exit(0)


if __name__ == '__main__':
    main()
