import requests
import json
import sys
from PIL import Image
from io import BytesIO


def lekerdez_kep_meret(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        width, height = img.size
        return width, height
    except Exception:
        return None, None


def main():
    if len(sys.argv) != 3:
        print("Hiba! Nem adott meg megfelelő felbontás paramétereket!")
        return

    try:
        min_width = int(sys.argv[1])
        min_height = int(sys.argv[2])
    except ValueError:
        print("Hiba! Érvénytelen felbontás értékek!")
        return

    print("=== Reddit Háttérkép Vadász ===")
    print()
    print("Csatlakozás r/EarthPorn subreddithez...")

    try:
        url = "https://www.reddit.com/r/EarthPorn/.json"

        response = requests.get(url)

        data = json.loads(response.text)

        posts = data["data"]["children"]

        print(f"Sikeres letöltés! ({len(posts)} poszt)")
        print()
        print(f"Keresés: minimum {min_width}x{min_height} felbontású képek")
        print()

        kepek = []

        for post in posts:
            post_data = post["data"]
            title = post_data.get("title", "")
            url_str = post_data.get("url", "")

            if not (
                url_str.endswith(".jpg")
                or url_str.endswith(".png")
                or "i.redd.it" in url_str
                or "i.imgur.com" in url_str
            ):
                continue

            width, height = lekerdez_kep_meret(url_str)

            if width and height:
                kepek.append(
                    {"title": title, "url": url_str, "width": width, "height": height}
                )

        megfelelo_kepek = [
            kep
            for kep in kepek
            if kep["width"] >= min_width and kep["height"] >= min_height
        ]

        megfelelo_kepek_rendezve = sorted(
            megfelelo_kepek, key=lambda k: k["width"] * k["height"], reverse=True
        )

        print("MEGFELELŐ HÁTTÉRKÉPEK:")
        print()

        if megfelelo_kepek_rendezve:
            for i, kep in enumerate(megfelelo_kepek_rendezve, 1):
                print(f"{i}. \"{kep['title']}\"")
                print(f"   Felbontás: {kep['width']} x {kep['height']}")
                print(f"   URL: {kep['url']}")
                print()

            with open("wallpapers.txt", "w", encoding="utf-8") as f:
                f.write(f"Reddit Háttérképek - Minimum {min_width}x{min_height}\n")
                f.write("\n\n")
                for i, kep in enumerate(megfelelo_kepek_rendezve, 1):
                    f.write(f"{i}. {kep['title']}\n")
                    f.write(f"   Felbontás: {kep['width']} x {kep['height']}\n")
                    f.write(f"   URL: {kep['url']}\n\n")

            print()
            print("Eredmények mentve: wallpapers.txt")
            print(f"{len(megfelelo_kepek_rendezve)} db új háttérkép lementve!")
        else:
            print("Sajnos nincs ilyen nagy felbontású kép!")
            print(f"Próbáld alacsonyabb értékkel (pl. 1920 1080).")
    except Exception as e:
        print(f"Hiba! {e}")


if __name__ == "__main__":
    main()
