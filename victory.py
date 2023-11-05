from argparse import ArgumentParser
import victory

def parse_args():
    parser = ArgumentParser()

    parser.add_argument("-f", "--file", type=str, help="Путь до файла с вопросами")
    parser.add_argument("-c", "--count", type=int, help="Количество вопросов")

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    app = victory.App(args)
    app.run()
