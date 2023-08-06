import argparse
import os
import platform
from aldemsubs.aldemsubs import AlDemSubsMain
from aldemsubs.aldemsubs import AlreadySubscribed
from aldemsubs.feed import EmptyFeed
from urllib.error import URLError


def main(argv=None):

    parser = argparse.ArgumentParser()

    if os.name == 'posix':
        cfgpath = "~/.config/aldemsubs.ini"
    elif platform.system() == 'Windows':
        cfgpath = "%APPDATA%\\aldemsubs\\aldemsubs.ini"

    parser.add_argument(
        '-c', '--config', metavar='CONFIG_FILE',
        default=cfgpath,
        help="Configuration file that should be used."
    )
    parser.add_argument(
        '-s', '--subscribe', metavar='CHANNEL_ID',
        help="Subscribe to a youtube channel via its channel id."
    )
    parser.add_argument(
        '-u', '--update', action='store_true',
        help="Update subscriptions from RSS feed."
    )
    parser.add_argument(
        '-d', '--download', action='store_true',
        help="Download new videos."
    )
    parser.add_argument(
        '-l', '--list', action='store_true',
        help="List all subscriptions."
    )
    parser.add_argument(
        '-r', '--unsubscribe', metavar='CHANNEL_ID',
        help="Unsubscribe from channel."
    )
    parser.add_argument(
        '-x', '--delete', action='store_true',
        help="Delete all videos older than n days (specified in config file)"
    )

    args = parser.parse_args()

    ads = AlDemSubsMain(args.config)

    if args.list:
        ads.list_channels()

    if args.unsubscribe is not None:
        ads.unsubscribe(args.remove)

    if args.subscribe is not None:
        try:
            ads.subscribe(args.subscribe)
        except AlreadySubscribed:
            print(f"You are already subscribed to {args.subscribe}")
            return 1
        except EmptyFeed:
            print(f"{args.subscribe} is not a valid channel-id.")
            return 2
        except URLError:
            print("No internet connection.")
            return 3

    if args.update:
        try:
            ads.update_subscriptions()
        except URLError:
            print("No internet connection.")
            return 3

    if args.download:
        ads.download_new_videos()

    if args.delete:
        ads.delete_old_videos()

    return 0


if __name__ == "__main__":
    exit(main())
