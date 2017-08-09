#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import optparse

from send2kindle import _version
from send2kindle.send_kindle import SendKindle


def main():
    '''Run the main program'''
    try:
        usage = ('Usage: %prog [options] FILE...\n'
                 '  FILE is a file to be sent as an email attachment.')
        description = ('send2kindle will send any number of files via email '
                       'to your Kindle device.')
        parser = optparse.OptionParser(usage=usage, version=_version,
                                       description=description)
        parser.add_option('--password', help=('Use provided password instead '
                                              'of smtp_password value from your config file. If you provide '
                                              "neither of these, you'll be asked interactively."))
        parser.add_option('-c', '--convert', action='store_true',
                          default=False, help=('Ask Kindle service to convert the documents '
                                               'to Kindle format (mainly for PDFs) [default: %default]'))
        (options, args) = parser.parse_args()
        if not args:
            parser.error('No files provided as arguments! See --help.')
        kindle = SendKindle(options, args)
        kindle.send_mail()
    except KeyboardInterrupt:
        print >> sys.stderr, 'Program interrupted, exiting...'
        sys.exit(10)


if __name__ == '__main__':
    main()
