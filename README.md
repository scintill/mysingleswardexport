# mysingleswardexport

Scrape the ward list from mysinglesward.com (now defunct?).  Currently takes HTML saved from the site (I saved from Google Chrome) and outputs in vCard format (with embedded profile pictures!)  This is me pretending to know Python.

## Usage
Download your ward list (https://mysinglesward.com/Home/WardList) using your browser, put the HTML and its accompanying files in a folder, and edit html2vcard.py to point to the HTML file.  Execute it and redirect the output to a file, which should be output in vCard format with contacts for all the people in the ward.

## Known Issues
- Full addresses might not be handled absolutely correctly; but apparently well enough to be imported to Gmail
- The bishopric have their calling titles put in their address fields, since the addresses are in different pages and not in the same column as everyone else's
