#!/bin/bash

cd ~

echo "time:" | tee info.txt 

date | tee -a  info.txt

echo "username:" $USER | tee -a info.txt

echo "os:" $OSTYPE | tee -a info.txt

echo "home directory:" | tee -a  info.txt

pwd | tee -a  info.txt

echo "files (recursive):" | tee -a  info.txt

ls -R | wc -l | tee -a info.txt

echo "folders (non recursive):" | tee -a info.txt

ls -la | grep "^d" | wc -l | tee -a  info.txt
