from argparse import ArgumentParser, SUPPRESS


def create_parser():
    parser = ArgumentParser(
        usage="""
        Example fetch: post_sender -e 'Arseni.Dudko@burberry.com' -f 'Inbox/Noreply/FailureYmkt' -d '30-May-2018'
        Example send:  post_sender -s one/all
        """,
        description="""
        Download and resend yMKT Abandoned Basket messages
        """,
        epilog = """
        If you find any bug just let me know by email - arseni_dudko@epam.com.
        """)

    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')

    required.add_argument("-e", dest="email",    help="Email address (example: 'Arseni.Dudko@burberry.com')")
    required.add_argument("-f", dest="folder",   help="Mail folder (example: 'Inbox/Noreply/FailureYmkt')")
    required.add_argument("-d", dest="date",     help="Messages date (example: '30-May-2018')")
    parser.add_argument("-p",   dest="password", help=SUPPRESS)
    optional.add_argument('-s', choices=['all', 'one'], dest="send", help="Send post request from each file in 'attachments' folder")
    parser._action_groups.append(optional)
    return parser


def main():
    import os
    import sys
    import getpass
    import imaplib

    from fetcher import FetchEmail
    from poster  import content_collector, post_data

    try:
        args = create_parser().parse_args()

        curr_dir = '.'
        if 'attachments' not in os.listdir(curr_dir):
            os.mkdir('attachments')

        download_folder = curr_dir + "/attachments/"

        if args.email and args.folder and args.date and not args.password:
            args.password = getpass.getpass('Enter a password: ')

            connection = FetchEmail(username=args.email, password=args.password, mail_folder=args.folder)
            message_list = connection.fetch_messages(error_date=args.date)

            new_message_list = list()
            for msg in message_list:
                new_message_list.append(('{}: {}: {}'.format(msg.get('from'), msg.get('subject'), msg.get('date'))))
                connection.save_attachment(msg=msg, download_folder=download_folder)

            print "\nList of messages:\n-----------------"
            for elem in new_message_list:
                print elem
            sys.exit(1)
        if args.send == 'all':
            print "\nSending all requests:\n-----------------\n"
            for file_name, content in content_collector(download_folder).iteritems():
                post_data(file_name, content)
            sys.exit(1)
        if args.send == 'one':
            print "\nSending first one request:\n-----------------\n"
            for file_name,content in content_collector(download_folder).iteritems():
                post_data(file_name, content)
                sys.exit(1)
        else:
            print "Please input all arguments: -e 'email' -f 'inbox_folder' -d 'date'"

    except KeyboardInterrupt, err:
        print err
    except imaplib.IMAP4.error, err:
        print err