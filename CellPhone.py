from concurrent.futures.process import _python_exit
from pyexpat import model
from tracemalloc import start
import CellPhoneClass as cp


def main():

    manufact = input("Enter your cell phone manufact: ")

    model = input("Enter your cell phone model: ")

    retail_price = input("Enter your cell phone retail price: ")

    cellphone = cp.CellPhone(manufact, model, retail_price)

    print("The manufact is ", cellphone.get_manufact())

    print("The mmodel is ", cellphone.get_model())

    print("The retail price is ", cellphone.get_retail_price())

    print(cellphone)


main()
