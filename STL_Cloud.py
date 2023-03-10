import os
import time

# Start timer
start = time.time()

# Test
# Open STL Data
for x in os.listdir():
    if x.endswith(".stl"):
        # Prints only text file present in My Folder
        print("Converting " + x + " to .csv file.")

        with open(x) as face_stl:
            # reads into separate lines
            raw_data = face_stl.readlines()

        # Create CSV File
        csv_ = x.split(".")
        new_csv_name = csv_[0]+'.csv'
        with open(new_csv_name, 'w') as f:
            for line in raw_data:
                # print(line)
                if line.strip().startswith("vertex"):
                    s_line = line.split(" ")
                    s_line = s_line[1:]
                    csv_lines = ",".join(s_line)
                    f.write(csv_lines)

end = time.time()
elapsed = str("{:.2f}".format(end - start))
print("")
print("Process complete. Run time: " + elapsed + " seconds.")
