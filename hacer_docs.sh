#!/bin/bash

rm -rf docs
mkdir docs
touch docs/.nojekyll
cp -r _build/html/* docs

git add docs


