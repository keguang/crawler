#!/usr/bin/env bash
sqlacodegen --noviews --noconstraints --noindexes  --schema ttsrc --table yingyongbao  --outfile /Users/guokeguang/Python/crawler/crawler/model/ttsrc.py mysql://user:pwd@ip:3306/db?charset=utf8
