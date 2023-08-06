from downloadutil.downloader import Downloader
from downloadutil.download_config import DownloadConfig

import argparse
import logging
import os


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(filename)s:%(lineno)d] %(asctime)s %(levelname)s: %(message)s")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        '--url', help='URL to download.', required=True)
    parser.add_argument(
        '--dest-dir-parent', help='Parent directory in which to extract the archive',
        required=True)
    parser.add_argument(
        '--cache-dir',
        default=os.path.expanduser('~/.cache/downloads'),
        help='Download cache directory on the local disk. Must have enough space.')
    parser.add_argument(
        '--verify-checksum',
        help='In addition to downloading the given URL, also download the SHA256 checksum file '
             'from an URL with an appended .sha256 suffix, and verify the checksum.',
        action='store_true')

    parser.add_argument('--verbose', action='store_true', help='Verbose logging')
    args = parser.parse_args()
    config = DownloadConfig(
        verbose=args.verbose,
        cache_dir_path=args.cache_dir)
    downloader = Downloader(config=config)
    downloader.download_url(
        args.url,
        verify_checksum=args.verify_checksum,
        download_parent_dir_path=args.dest_dir_parent)


if __name__ == '__main__':
    main()
