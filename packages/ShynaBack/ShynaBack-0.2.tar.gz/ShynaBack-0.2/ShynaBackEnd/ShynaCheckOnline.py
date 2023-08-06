import urllib.request


class CheckOnline:
    """Open the url and check for the received byte. if bytes are there then it returns Pass otherwise Fail
    make object of CheckOnline and call test_connection method. True and False are self explainatory.
    """
    result = ""

    def open_url(self):
        try:
            x = urllib.request.urlopen(url='https://www.google.com', timeout=2)
            response = x.read()
            if response == b'':
                self.result = "Fail"
            else:
                self.result = "Pass"
        except Exception as e:
            print(e)
            self.result = "Fail"
        finally:
            print("Internet Connection", self.result)
            return self.result
    
    def test_connection(self):
        test_connection =  False
        try:        
            if str(self.open_url()) == "Fail":
                test_connection = False
            else:
                test_connection = True
        except Exception as e:
            test_connection = False
            print(e)
        finally:
            return test_connection

