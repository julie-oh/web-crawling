from get_low_price import get_low_price

def main():
    with open('./list.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            low_price = get_low_price(line)
            

if __name__ == '__main__':
    main()

