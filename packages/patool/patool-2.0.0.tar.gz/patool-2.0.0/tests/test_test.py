# -*- coding: utf-8 -*-
# Copyright (C) 2013-2015 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest
import os
from patoolib import cli
from . import datadir, needs_program

class ArchiveTestTest(unittest.TestCase):

    @needs_program('7z')
    def test_test(self):
        archive = os.path.join(datadir, "t .7z")
        args = ["--non-interactive", "test", archive]
        cli.main(args=args)
