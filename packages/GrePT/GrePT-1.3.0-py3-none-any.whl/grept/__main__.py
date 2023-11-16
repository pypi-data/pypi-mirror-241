import argparse
import sys
from grept.util import _crawl, error
from grept.interactive import EmbeddingChat, CompletionChat, ImageChat
from grept.__init__ import __version__
import os


def main():
    parser = argparse.ArgumentParser(description="Ask questions about your code")

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("-c", "--chat", action="store_true", help="chat mode")
    mode.add_argument("-e", "--embed", action="store_true", help="embed mode")
    mode.add_argument("-i", "--image", action="store_true", help="chat with an image")
    mode.add_argument("-v", "--version", action="store_true", help="print version")

    parser.add_argument("files", nargs="*", default=["./"], help="files to query for chat mode")
    parser.add_argument("-l", "--level", type=int, default=1, help="level of directory recursion")
    parser.add_argument("-x", "--suffix", nargs="+", help="filter files by suffix")
    parser.add_argument("-t", "--tokens", type=int, default=512, help="maximum tokens to generate")
    parser.add_argument("-p", "--path", default=".chromadb/", help="path to load embedding from")

    args = parser.parse_args()
    if args.version:
        print(__version__)
        sys.exit(0)

    ignore = []
    try:
        with open(".greptignore", "r") as f:
            ignore = f.read().splitlines()
    except FileNotFoundError:
        pass

    if args.embed:
        chat = EmbeddingChat([], args.tokens, "", args.path)
        chat.interact()
    elif args.chat:
        if args.level < 1: 
            error("level must be greater than 0")
            sys.exit(1)

        file_set = _crawl(args.files, args.level, args.suffix, ignore)
        chat = CompletionChat([], args.tokens, "", file_set)
        chat.interact()
    elif args.image:
        if os.path.isdir(args.files[0]):
            error("must provide an image path")
            sys.exit(1)
        chat = ImageChat([], args.tokens, "", args.files[0]) 
        chat.interact()
    else:
        sys.exit(1)
    
if __name__ == "__main__":
    main()

