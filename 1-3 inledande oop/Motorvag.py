from Bil import Bil             # kör koden i filen Bil.py
class Motorväg:
    def main():
        minBil = Bil(60, "Saab")
        minBil.drive()
    if __name__ == "__main__":  # True ifall det är den aktuella filen som "körs"
        main()