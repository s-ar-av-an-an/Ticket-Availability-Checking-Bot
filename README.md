# Ticket-Availability-Checking-Bot
It works currently with TicketNew, can be used to check if bookings are open for your favourite movies. 

# Installation Procedure
# 1. Install termux and termux-api from f-droid (links below)
termux: https://f-droid.org/en/packages/com.termux/<br />
termux-api: https://f-droid.org/en/packages/com.termux.api/<br />

# 2. Download the application as zip file and extract using unzip
curl -LO https://github.com/s-ar-av-an-an/Ticket-Availability-Checking-Bot/archive/refs/heads/main.zip<br />
pkg install unzip<br />
unzip main.zip<br />

# 3. Install necessary packages
pkg install update -y
cd Ticket-Availability-Checking-Bot-main/<br />
chmod +x initialize.sh<br />
./initialize.sh<br />
pip install -r requirements.txt<br />

# 4. Run the application
python3 ticketbotm.py
