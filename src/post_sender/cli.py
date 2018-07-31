from argparse import ArgumentParser, SUPPRESS

JOB_LINK_CART = "http://esbaraciap02d.burberry.corp:8500/jms-prod/write_new_mq?queue=BUR.CIRRUS.YMKT.ABANDONED.CART"
JOB_LINK_SIGNUP = "http://esbaraciap02d.burberry.corp:8500/jms-prod/write_new_mq?queue=BUR.CIRRUS.YMKT.EMAIL.SIGNUP"


def create_parser():
    parser = ArgumentParser(
        usage="""
        Example fetch: post_sender -e "Arseni.Dudko@burberry.com" -f "Inbox/Noreply/FailureYmkt" -d "30-May-2018"
        Example send:  post_sender -s one_cart/one_sign/all_cart/all_sign
        """,
        description="""
        Download and resend yMKT Abandoned Basket and ATG SignUp messages 
        """,
        epilog = """
        If you find any bug just let me know by email - arseni_dudko@epam.com.
        """)

    optional = parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')

    required.add_argument('-e', dest='email',    help='Email address (example: "Arseni.Dudko@burberry.com")')
    required.add_argument('-f', dest='folder',   help='Mail folder (example: "Inbox/Noreply/FailureYmkt")')
    required.add_argument('-d', dest='date',     help='Messages date (example: "30-May-2018")')
    parser.add_argument('-p',   dest='password', help=SUPPRESS)
    optional.add_argument('-s', choices=['one_signup',
                                         'one_cart',
                                         'all_signup',
                                         'all_cart'], dest='send', help="Send post request from each file in folder")
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
        subfolder_names = ['abandoned_card', 'signup']
        download_folder = os.getcwd() + "/attachments/"

        if 'attachments' not in os.listdir(curr_dir):
            os.mkdir('attachments')

            for subfolder_name in subfolder_names:
                os.makedirs(os.path.join(download_folder, subfolder_name))

        abandoned_card_folder = download_folder + subfolder_names[0] + '/'
        signup_folder = download_folder + subfolder_names[1] + '/'

        subjects = ['PROD: Abandoned Cart ATG to yMkt - yMKT ERROR','PROD: Email SignUp ATG to yMkt - yMKT ERROR']

        if args.email and args.folder and args.date and not args.password:
            args.password = getpass.getpass('Enter a password: ')

            connection = FetchEmail(username=args.email, password=args.password, mail_folder=args.folder)

            for num,subject in enumerate(subjects):
                message_list = connection.fetch_messages(subject=subject,error_date=args.date)

                new_message_list = list()
                for msg in message_list:
                    new_message_list.append(('{}: {}: {}'.format(msg.get('from'), msg.get('subject'), msg.get('date'))))
                    connection.save_attachment(msg=msg, download_folder=download_folder + subfolder_names[num] + '/')

                print "\nList of messages:\n-----------------"
                for elem in new_message_list:
                    print elem
            sys.exit(1)

        if args.send == 'one_cart':
            print "\nSending the first ABANDONED CART request:\n-----------------\n"
            for file_name,content in content_collector(abandoned_card_folder).iteritems():
                post_data(file_name=file_name, content=content, job_link=JOB_LINK_CART)
                sys.exit(1)

        if args.send == 'one_signup':
            print "\nSending the first SIGNUP request:\n-----------------\n"
            for file_name,content in content_collector(signup_folder).iteritems():
                post_data(file_name=file_name, content=content, job_link=JOB_LINK_SIGNUP)
                sys.exit(1)

        if args.send == 'all_cart':
            print "\nSending all ABANDONED CART requests:\n-----------------\n"
            for file_name, content in content_collector(abandoned_card_folder).iteritems():
                post_data(file_name=file_name, content=content, job_link=JOB_LINK_CART)
            sys.exit(1)

        if args.send == 'all_signup':
            print "\nSending all SIGNUP requests:\n-----------------\n"
            for file_name, content in content_collector(signup_folder).iteritems():
                post_data(file_name=file_name, content=content, job_link=JOB_LINK_SIGNUP)
            sys.exit(1)

        else:
            print 'Please input all arguments: -e "email" -f "inbox_folder" -d "date"'

    except KeyboardInterrupt, err:
        print err
    except imaplib.IMAP4.error, err:
        print err
