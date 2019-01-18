input_file = 'mpd_full_list.txt'
output_file = 'mpd_filtered_list.txt'
filter_file = 'mpd_filter_list.txt'

filter_list = [line.lower().strip() for line in open(filter_file)]


with open(input_file, 'r') as inputf, open(output_file, 'w') as outputf:
    for line in inputf:
        #print (line)
        if not any(x in line.lower() for x in filter_list):
            outputf.write(line)


