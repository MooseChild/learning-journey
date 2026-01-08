import os

# Define the file we want to read
log_file = "data.log"

def parse_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found!")
        return

    error_count = 0
    info_count = 0

    print(f"--- Processing {file_path} ---")
    
    with open(file_path, "r") as file:
        for line in file:
            # Clean up the line (remove extra whitespace)
            line = line.strip()
            
            if "ERROR" in line:
                error_count += 1
                print(f"[!] Found Error: {line}")
            elif "INFO" in line:
                info_count += 1

    print("----------------------------")
    print(f"Summary: {info_count} INFO messages, {error_count} ERROR messages.")
    
    if error_count > 0:
        print("Action Required: Check the database/auth logs!")
    else:
        print("System Status: Healthy")

if __name__ == "__main__":
    parse_logs(log_file)
