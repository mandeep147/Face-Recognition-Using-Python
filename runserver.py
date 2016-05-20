#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import argparse

from FaceDetection.app import app

parser = argparse.ArgumentParser(description="FaceDetection")
parser.add_argument(
    "--port", "-p",
    type=int,
    help="Port to listen on",
    default=3000,
)
args = parser.parse_args()

if __name__ == '__main__':
    flask_options = dict(
        host='127.0.0.1',
        debug=True,
        port=args.port,
        threaded=True,
    )

    app.run(**flask_options)
