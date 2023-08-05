from metafinder import __version__


banner = """
   _____               __             ___________ .__               .___                   
  /     \     ____   _/  |_  _____    \_   _____/ |__|   ____     __| _/   ____   _______  
 /  \ /  \  _/ __ \  \   __\ \__  \    |    __)   |  |  /    \   / __ |  _/ __ \  \_  __ \ 
/    Y    \ \  ___/   |  |    / __ \_  |     \    |  | |   |  \ / /_/ |  \  ___/   |  | \/ 
\____|__  /  \___  >  |__|   (____  /  \___  /    |__| |___|  / \____ |   \___  >  |__|    
        \/       \/               \/       \/               \/       \/       \/          
        """

author = "@JosueEncinar"
description = "Search for documents in a domain through Search Engines. The objective is to extract metadata"
usage_example = "metafinder -d domain.com -l 50 -o /tmp -go -bi"


def show_banner():
    print(banner)
    print(f"|_ Author: {author}")
    print(f"|_ Description: {description}")
    print(f"|_ Version: {__version__}")
    print(f"|_ Usage: {usage_example}")
    print("")
