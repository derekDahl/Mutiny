#Snippet for opening a text file and reading into memory
from sys import argv
import csv

file = open("working.txt", "r")
file_text = file.read()
print(file_text)
