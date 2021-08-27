# Scraping advocate websites using SELENIUM - PYTHON 

Project contains source code for scraping two websites containing information about lawyers. Code uses `Google Chrome` driver and is made to run on `Windows 10 OS`.

`Python version 3.8`

To run the code locally:
- IMP: You would need to install the web driver for your browser for selenium to work
- Clone the repository
- `cd` in the `Advocate` folder 
- Create a virtual environment using `venv` or `conda` 
- Activate your environment and do `pip install -r requirements.txt`
- Change your driver path in the files
- Line 60, 27: `driver = webdriver.Chrome("D:\\your\\path\\to\\driver\\here\\chromedriver.exe")`
- `cd` in the respective directory and `python <script_name>_scrape.py`

### Cyprus Website
https://www.cyprusbar.org/CypriotAdvocateMembersPage.aspx
![ezgif com-gif-maker](https://user-images.githubusercontent.com/28010398/131078306-c7be099d-9278-4ac4-a1b8-bdff0db278b3.gif)

```
cd cyprus
python cyprus_scrape.py
```
##### Output
![2021-08-27-11-31-43](https://user-images.githubusercontent.com/28010398/131079834-ebcaa3b9-7d77-47fe-9985-46934c240b39.png)


### Davac Website
http://vyhledavac.cak.cz
![ezgif com-gif-maker_davac](https://user-images.githubusercontent.com/28010398/131079241-733da2e8-037d-4184-a528-19f3adfd4f13.gif)

```
cd davac
python davac_scrape.py
```
##### Output
![2021-08-27-11-39-44](https://user-images.githubusercontent.com/28010398/131080892-5f7269c3-5187-4965-9ec4-b424d062ec0f.png)

