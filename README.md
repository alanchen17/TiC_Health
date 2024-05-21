# TiC_Health
First, let me just say it is very interesting to see what other people have come up with. Ironically, but simply search up Serif Health - you can see others' approach. Kudos to the creative repo names 😌. (https://github.com/search?q=serif%20health&type=repositories). However, this is in fact my work and no ideas/code were copied or taken from others.

## The script or code used to parse the file and produce output.
https://github.com/alanchen17/TiC_Health/blob/main/main.py

## The setup or packaging file(s) required to bootstrap and execute your solution code
```
pip3 install ijson
```
Download the ToC file and unzip the contents within this directory. Currently have it named as `2024-05-01_anthem_index.json`

## The output URL list.
https://serifhealth123.s3.us-east-2.amazonaws.com/output_file.csv

## A README file, explaining your solution, how long it took you to write, how long it took to run, and the tradeoffs you made along the way.
Took me about 30mins to write the code and 43.7sec for the code to run. Most of my time was spent on understanding the problem and the data format as well as tradeoffs.

There is really two parts to the problem/solution:

#### 1. Parsing through the table of contents(ToC) for machine readable file URLS
> Solution - Since the ToC is huge (>20GB), it is not likely to load the entire dataset onto RAM. I utilize a streaming approach(ijson) that reads the file by line and parsing it on the fly. For my purposes this was sufficient, however there are other ways that are arguable better, but with much more code/infrastructure overhead. Some other ways include distributed computing (spark), batch/parallel processing, and database storage (MongoDB json-doc upload). Also it is important to note, ToC came in a compressed file - so uncompressing it on the fly is important as well.

#### 2. Determining if it is part of Anthem Preferred provider organization(PPO) network in NY, and if it is then add it to the output file.
> Solution - Another word for PPO is in-network provider and since all file urls within ToC are in-network file, we just have determine if it is in NY state (Assumption). I used the description for parsing key word like "NY" and "New York". This could also be applied to the actual URL as well. However there are other generic discription such as "In-Network Negotiated Rates Files" and "CareFirst BCBS : Select Preferred Provider", which I am unable to determine if it is in NY - hence I did not add it to the output. Another method that could be helpful is the Anthem API for search up Plan via EIN and then cross-verifying the output with the URL from ToC. To note, with all these methods it is uncertain the output file encompassess all Anthem PPO network in NY.
