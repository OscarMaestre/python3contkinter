#!/bin/bash

rm -rf docs
mkdir docs

cp -r _build/html/* docs

git add docs


