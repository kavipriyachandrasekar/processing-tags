# remove duplicates in the comma separated string tags-processed.txt
# and write the result to tags-processed-unique.txt

from tqdm import tqdm

def main():
    # read the file
    f = open("tags-processed.txt", "r")
    lines = f.readlines()
    f.close()

    # remove duplicates
    tags = []
    # print(len(lines))
   
    for tag in tqdm(lines[0].split(",")):
        if tag not in tags:
            tags.append(tag)


    # write the result
    f = open("tags-processed-unique.txt", "w")
    for tag in tags:
        f.write(tag + ",")
    f.close()

# if __name__ == "__main__":
    # main()