#!/usr/bin/python3
# coding: utf-8
#
# Copyright (C) 2023 hidenorly
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import MeCab
import re

m = MeCab.Tagger("-Owakati")

text = sys.stdin.read()
node = m.parseToNode(text)

# Extract noun unique word
result = set()
while node:
    feature = node.feature
    if feature.startswith("名詞") and ( "固有名詞" in feature or "一般" in feature ):
        jpWord = re.sub("[a-zA-Z0-9]+", "", node.surface)
        if jpWord:
            result.add( jpWord )
    node = node.next

# Sub extraction
result2 = set()
for aLine in result:
    aSet = set(aLine.split("・"))
    if aSet:
        result2 = result2 | aSet
    else:
        aSet = set(aLine.split("、"))
        if aSet:
            result2 = result2 | aSet
        else:
            result2.add(aLine)

# Output
for aLine in result2:
    print(aLine)
