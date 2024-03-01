# #!/bin/bash
# #Takes in a URL, sends a request to that URL, and displays
# #the size of the body of the response

# curl -s "$1" | wc -c

#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Assign URL argument to a variable
url="$1"

# Send request to the URL and store the response body in a temporary file
response_body=$(curl -s -o /tmp/response_body.txt -w "%{size_download}" "$url")

# Check if curl command was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to retrieve response from $url"
    exit 1
fi

# Display the size of the response body in bytes
echo "Size of the response body: $response_body bytes"

# Remove temporary file
rm -f /tmp/response_body.txt
