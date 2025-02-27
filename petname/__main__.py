#!/usr/bin/env python
#
# petname
#
# Copyright 2014 Dustin Kirkland <dustin.kirkland@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import petname
import sys

def main():
	parser = argparse.ArgumentParser(description='Generate human readable random names')
	parser.add_argument('-w', '--words', help='Number of words in name, default=2', default=2)
	parser.add_argument('-l', '--letters', help='Maximum number of letters per word, default=6', default=6)
	parser.add_argument('-s', '--separator', help='Separator between words, default="-"', default="-")
	parser.add_argument('-S', '--seed', help='Seed for random generator.', default=None)
	parser.options = parser.parse_args()

	if parser.options.seed:
		generated = petname.Generate(
			int(parser.options.words),
			parser.options.separator,
			int(parser.options.letters),
			random.Random(parser.options.seed))
	else:
		generated = petname.Generate(
			int(parser.options.words),
			parser.options.separator,
			int(parser.options.letters))

	sys.stdout.write(generated + "\n")

if __name__ == "__main__":
	main()
