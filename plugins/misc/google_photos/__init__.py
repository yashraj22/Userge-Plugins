# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

""" Google Photos """

import os

from userge.utils import secure_env


G_PHOTOS_CLIENT_ID = os.environ.get(
    secure_env("G_PHOTOS_CLIENT_ID"), os.environ.get(secure_env("G_DRIVE_CLIENT_ID")))

G_PHOTOS_CLIENT_SECRET = os.environ.get(
    secure_env("G_PHOTOS_CLIENT_SECRET"), os.environ.get(secure_env("G_DRIVE_CLIENT_SECRET")))

G_PHOTOS_AUTH_TOKEN_ID = int(os.environ.get("G_PHOTOS_AUTH_TOKEN_ID") or 0)
