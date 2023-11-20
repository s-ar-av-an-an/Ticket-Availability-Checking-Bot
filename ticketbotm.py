import getInfoTermux
import user_handler
import cron_handler


# create a csv file for bot
row = getInfoTermux.getnvalidateData()
user_handler.add_entry(row)

# add cron job
cron_handler.add_cron(row)


