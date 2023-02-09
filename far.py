def main():
    far=50
    while far<=150:
        celcius=5/9*(far-32)
        print(f"{celcius:10.2f} {far:10.2f}")
        far=far+1
main()
