import os
from pick import pick

title = 'Please choose your browsers to use with Playwright (press SPACE to mark, ENTER to continue): '
options = ['chromium', 'firefox', 'webkit']
selected = pick(options, title, multiselect=True, min_selection_count=1)
results = []
for option in range(len(selected)):
    results.append(selected[option][0])

browsers = ' '.join(results)
if len(results) > 0:
    print("Installing Browsers..")
    os.system(f'playwright install {browsers}')
    print("Complete Install.")
else:
    print("Nothing to do")
