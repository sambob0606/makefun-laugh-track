from pathlib import Path

JOKE = (
    "I used 20x leverage for a quick win, "
    "and my liquidation price showed up before my take-profit ever did."
)


def main() -> None:
    print(JOKE)
    output_path = Path("/output/entry.txt")
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(JOKE, encoding="utf-8")
    except OSError:
        fallback = Path("output/entry.txt")
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
