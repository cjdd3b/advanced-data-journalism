if __name__ == '__main__':
    try:
        import requests, mechanize, jupyter
        from bs4 import BeautifulSoup
        print('Yay! All looks good.')
    except:
        print("Something has gone horribly wrong!")
        raise