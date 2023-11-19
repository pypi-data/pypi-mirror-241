import pywaybackup.archive as archive 
import argparse
import os
__version__ = "0.2.6"

def main():
    parser = argparse.ArgumentParser(description='Download from wayback machine (archive.org)')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__, help='Show version')
    required = parser.add_argument_group('required')
    required.add_argument('-u', '--url', type=str, help='URL to use')
    exclusive_required = required.add_mutually_exclusive_group(required=True)
    exclusive_required.add_argument('-c', '--current', action='store_true', help='Download the latest version of each file snapshot (opt range in y)')
    exclusive_required.add_argument('-f', '--full', action='store_true', help='Download snapshots of all timestamps (opt range in y)')
    optional = parser.add_argument_group('optional')
    optional.add_argument('-l', '--list', action='store_true', help='Only print snapshots (opt range in y)')
    optional.add_argument('-r', '--range', type=int, help='Range in years to search')
    optional.add_argument('-o', '--output', type=str, help='Output folder')
    special = parser.add_argument_group('special')
    #special.add_argument('--detect-filetype', action='store_true', help='If a file has no extension, try to detect the filetype')
    special.add_argument('--retry-failed', nargs='?', const=True, type=int, help='Retry failed downloads (opt tries as int, else infinite)')

    args = parser.parse_args()
    if args.current:
        mode = "current"
    if args.full:
        mode = "full"

    if args.output is None:
        args.output = os.path.join(os.getcwd(), "waybackup_snapshots")
    cdxResult_list = archive.query_list(args.url, args.range, mode)
    if args.list:
        archive.print_result(cdxResult_list)
    if not args.list:
        archive.download_url_list(cdxResult_list, args.output, args.retry_failed, mode)
        archive.remove_empty_folders(args.output)

if __name__ == "__main__":
    main()