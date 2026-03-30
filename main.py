from ascii_filter import AsciiFilter
from video_input import VideoInput


def main():
    ascii_filter = AsciiFilter()
    video_input = VideoInput(filter=ascii_filter)

    video_input.run()


if __name__ == "__main__":
    main()
