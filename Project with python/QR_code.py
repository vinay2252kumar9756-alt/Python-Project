import qrcode
import os


class QRGenerator:

    def text_to_qr(self):
        data = input("Enter text: ")

        if data == "":
            print("Text cannot be empty!\n")
            return

        img = qrcode.make(data)
        img.save("text_qr.png")

        print("QR Code saved as text_qr.png\n")

    def website_qr(self):
        url = input("Enter website URL: ")

        if url == "":
            print("Website URL cannot be empty!\n")
            return

        img = qrcode.make(url)
        img.save("website_qr.png")

        print("Website QR saved as website_qr.png\n")

    def payment_qr(self):
        upi_id = input("Enter UPI ID: ")
        name = input("Enter Name: ")
        amount = input("Enter Amount: ")

        if upi_id == "" or name == "" or amount == "":
            print("All fields are required!\n")
            return

        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than 0!\n")
                return

        except ValueError:
            print("Invalid amount!\n")
            return

        upi_link = (
            f"upi://pay?pa={upi_id}"
            f"&pn={name}"
            f"&am={amount:.2f}"
            f"&cu=INR"
        )

        img = qrcode.make(upi_link)
        img.save("payment_qr.png")

        print("Payment QR saved as payment_qr.png\n")

    # QR History
    def qr_history(self):
        files = [
            "text_qr.png",
            "website_qr.png",
            "payment_qr.png"
        ]

        print("\n----- QR History -----")

        found = False

        for file in files:
            if os.path.exists(file):
                print(file)
                found = True

        if not found:
            print("No QR codes found.")

        print("----------------------\n")

    # Delete QR
    def delete_qr(self):
        print("\n----- Delete QR -----")
        print("1. text_qr.png")
        print("2. website_qr.png")
        print("3. payment_qr.png")

        choice = input("Enter choice: ")

        if choice == "1":
            filename = "text_qr.png"

        elif choice == "2":
            filename = "website_qr.png"

        elif choice == "3":
            filename = "payment_qr.png"

        else:
            print("Invalid choice!\n")
            return

        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} deleted successfully!\n")
        else:
            print("QR file not found!\n")


# ===== MAIN PROGRAM =====

qr = QRGenerator()

while True:

    print("\n================================")
    print("          QR GENERATOR")
    print("================================")
    print("1. Text to QR")
    print("2. Website QR")
    print("3. Payment QR")
    print("4. QR History")
    print("5. Delete QR")
    print("6. Exit")
    print("================================")

    choice = input("Enter choice: ")

    if choice == "1":
        qr.text_to_qr()

    elif choice == "2":
        qr.website_qr()

    elif choice == "3":
        qr.payment_qr()

    elif choice == "4":
        qr.qr_history()

    elif choice == "5":
        qr.delete_qr()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice!\n")