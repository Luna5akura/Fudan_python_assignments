import yaml
import json

PATH = 'datasets.yml'

def main():
    with open(PATH, 'r') as file:
        data = yaml.safe_load(file)

    json_data = json.dumps(data, indent=2)
    print(json_data)
    print(data['jobs']['build']['steps'][-1]['run'])


if __name__ == '__main__':
    main()
