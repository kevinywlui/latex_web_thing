import requests
import sys


def parse_string(s):
    pieces = s.split(':')
    payload = dict(zip(pieces, ['au', 'ti', 'year']))
    payload['format'] = 'bibtex'
    return payload


def get_bibtex(s):
    payload = parse_string(s)
    r = requests.get('https://mathscinet.ams.org/mrlookup', params=payload)
    output = r.text
    return output.split('<pre>')[1].split('</pre>')[0].strip('\n')


def parse_bib(filename):
    all_entries = set()
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith("@"):
                all_entries.add(line.split('{', 1)[1].split(',', 1)[0])
    return all_entries


def parse_aux(filename):
    with open(filename, "r") as f:
        citations = set()
        for line in f:
            if line.startswith("\\citation{"):
                citations.add(line[10:-2])
    return citations


def append_missing(missing_cits, bib_file):
    with open(bib_file, "a") as f:
        for m in missing_cits:
            new_entry = get_bibtex(m)
            f.write(new_entry)


def main():
    name = sys.argv[1]
    aux_file = name + ".aux"
    bib_file = name + ".bib"
    citations = parse_aux(aux_file)
    existing_bibs = parse_bib(bib_file)

    missing_cits = citations.difference(existing_bibs)
    if missing_cits:
        append_missing(missing_cits, bib_file)


if __name__ == "__main__":
    main()
