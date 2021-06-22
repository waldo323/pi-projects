#!/usr/bin/env bash
IFS="\n"
for file in *.ogg;
do
    mv "$file" "${file//[[:space:]]}"
done
IFS="\n"
for file in *.mp3;
do
	    mv "$file" "${file//[[:space:]]}"
done
