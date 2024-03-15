"""_summary_
"""

import segno

ids = [0, 1, 2, 3]
# products = ["Apples", "Pears", "Chocolate", "Melon"]
# weights = [12, 56, 23, 76]
# volumes = [5, 15, 2, 20]


def qr_generate():
    """_summary_
    """
    qrcode = segno.make_qr(ids[0])
    qrcode.save("basic_qr.png", scale=10)
    print("Hello World!")


def main():
    """_summary_
    hola
    """
    qr_generate()


if __name__ == "__main__":
    main()
