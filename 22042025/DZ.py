
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

# --- KONSTANTE ---
COLLAGE_SIZE = 800
QUADRANT_SIZE = COLLAGE_SIZE // 2
BORDER_SIZE = 5
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (255, 255, 255, 180)
TEXT_CONTENT = "Uspomene 2025"
FONT_PATH = "arial.ttf"  # prilagodi putanju ako treba

def load_images(image_paths: list[str]) -> list[Image.Image]:
    """
    Učitava slike iz zadanih putanja.

    :param image_paths: lista putanja do slika koje se žele učitati.
    :return: lista PIL.Image objekata.
    """
    pass

def resize_image(image: Image.Image, max_size: int) -> Image.Image:
    """
    Proporcionalno smanjuje sliku da stane u kvadrat danih dimenzija.

    :param image: Slika koju treba smanjiti.
    :param max_size: Maksimalna širina/visina kvadranta.
    :return: Smanjena slika.
    """
    pass

def add_border(image: Image.Image, border_size: int = BORDER_SIZE, color: tuple[int, int, int] = (0, 0, 0)) -> Image.Image:
    """
    Dodaje okvir oko slike.

    :param image: Slika kojoj se dodaje okvir.
    :param border_size: Debljina okvira u pikselima.
    :param color: Boja okvira (RGB).
    :return: Nova slika s okvirom.
    """
    pass

def apply_effects(image: Image.Image, effects: list[str]) -> Image.Image:
    """
    Primjenjuje vizualne efekte na sliku.

    :param image: Ulazna slika.
    :param effects: lista efekata, npr. ["blur"].
    :return: Slika s primijenjenim efektima.
    """
    pass

def create_collage(images: list[Image.Image]) -> Image.Image:
    """
    Kreira kolaž iz 4 slike.

    :param images: lista 4 slike (PIL.Image) koje se postavljaju u kolaž.
    :return: Generirani kolaž dimenzija 800x800.
    """
    pass

def add_signature(image: Image.Image, text: str = TEXT_CONTENT, font_path: str = FONT_PATH) -> Image.Image:
    """
    Dodaje tekstualni potpis u donji desni kut slike.

    :param image: Slika na koju se dodaje tekst.
    :param text: Tekst koji se ispisuje.
    :param font_path: Putanja do fonta (.ttf).
    :return: Slika s dodanim tekstom.
    """
    pass

def save_image(image: Image.Image, path: str) -> None:
    """
    Sprema sliku u datoteku.

    :param image: PIL slika koja se sprema.
    :param path: Putanja gdje će se spremiti slika.
    """
    pass

# --- GLAVNI DIO PROGRAMA ---
if __name__ == "__main__":
    # TODO: Zamijeni putanje sa stvarnim lokacijama svojih slika
    image_paths = ["slika1.jpg", "slika2.jpg", "slika3.jpg", "slika4.jpg"]

    for path in image_paths:
        if not os.path.exists(path):
            raise FileNotFoundError(f"❌ Datoteka nije pronađena: {path}")

    images = load_images(image_paths)
    collage = create_collage(images)
    collage = add_signature(collage)
    save_image(collage, "kolaz_uspomene_funkcije.jpg")
