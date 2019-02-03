from Interface.MiningInterface import MiningInterface
from Interface.PrintHead import PrintHead

def print_header(header):
    print("\n\n")
    print("_" * 100)
    print(header)


def main():
    interface = MiningInterface("train_tweets.csv")

    print_header("Statistics:")
    for st in interface.get_all_statistics():
        PrintHead(st)

    print_header("Prepare file:")
    PrintHead(interface.prepare_file())

    print_header("Sentimental analysis:")
    PrintHead(interface.get_sentimental())

    interface.restore()

    print_header("Bag of words:")
    print(interface.get_similiarity_array())
    print(interface.get_bow_names())
    print(interface.get_most_similiar_tweets())


if __name__ == "__main__":
    main()
