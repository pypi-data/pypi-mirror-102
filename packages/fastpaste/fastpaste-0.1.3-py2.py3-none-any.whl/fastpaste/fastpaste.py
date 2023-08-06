import os, pyaes, binascii, pbkdf2, string, random, requests, re, time

from typing_extensions import runtime

class exeptions:
    class Error(Exception):
        """Base class for other exceptions"""
        pass
    class NoFile(Error):
        """Exception for when the passed file does not exists"""
        pass
    class NoUser(Error):
        """Exception for When There Is No User Set in PasteApi"""
        def __str__(self):
            return f'There Is No User Set in PasteApi Class'
    class UnknownError(Error):
        """Exception for When There Is No Keys Set For AesObj"""
        def __str__(self):
            return f'There Are No Keys Set in AesObj Class'         
    class NoKeys(Error):
        """Exception for When There Is No Keys Set For AesObj"""
        def __str__(self):
            return f'There Are No Keys Set in AesObj Class'        

class Data:
    def __init__(self):
        pass
    def time_convert(sec):
        try:
            return f'{str("0"+str(int(int(int(sec)//60)//60)) if(int(int(int(sec)//60)//60) < 10) else int(int(int(sec)//60)//60))}:{str("0"+str(int(int(sec)//60)%60) if(int(int(sec)//60)%60 < 10) else int(int(sec)//60)%60)}:{str("0"+str(int(sec)%60) if(int(sec)%60 < 10) else int(sec)%60)}.{str(str(round(float(str("0."+str(sec).split(".")[1])), 7)).split(".")[1])}'
        except IndexError:
            pass
            return f'{str("0"+str(int(int(int(sec)//60)//60)) if(int(int(int(sec)//60)//60) < 10) else int(int(int(sec)//60)//60))}:{str("0"+str(int(int(sec)//60)%60) if(int(int(sec)//60)%60 < 10) else int(int(sec)//60)%60)}:{str("0"+str(int(sec)%60) if(int(sec)%60 < 10) else int(sec)%60)}.{str(str(round(float(str("0."+str(sec).split(".")[1])), 7)))}'
    time=time
    UserName=""
    KeyData=[]
    ExpireInt=1
    ExpireOptionsList=["burn", "5", "60", "1440", "10080", "40320", "483840"]
    DefScrapeNum=1
    DefSilent=False

class AesObj:
    """Class For AES Encryption And Dencryption"""
    def __init__(self):
        pass
    def gen():
        """A Function For Generating A Keys.txt File in The Current Dir\n
        :return: List of [AesKey, AesIV]"""
        d=[pbkdf2.PBKDF2(str("".join([random.choice(str(string.digits)+string.ascii_letters) for _ in range(40)])), os.urandom(16)).read(32), random.randint(27, 999999)]
        open(os.path.abspath(f'{os.getcwd()}{os.sep}keys.txt'),'w').write(f"{str(binascii.hexlify(d[0]))[2:-1]};{d[1]}")
        print(f"New KeyData:\n\tKey: {d[0]}\n\tIV: {d[1]}\n\nCreated Key Backup File {os.path.abspath(f'{os.getcwd()}{os.sep}keys.txt')}") if(Data.DefSilent==False) else None
        Data.KeyData=[binascii.hexlify(d[0]),int(d[1])]
        return list([binascii.hexlify(d[0]),int(d[1])])
    def keyfile2Tup(path: str):
        """A Function Used For Getting The Keys From A File\n
        :param path: String of The Path From The Current Dir to The keys.txt File\n
        :return: List of [AesKey, AesIV]"""
        if(os.path.exists(os.path.abspath(path))):
            return list(open(os.path.abspath(path), 'r').read().split(";"))
        else:
            raise exeptions.NoFile
    def Enc(data: str):
        """Encrypts The Data Passed Using The Default Aes Key Data\n
        :param data: String of The Data You Want to Encrypt\n
        :return: Bytes String of The Encrypted Data"""
        return bytes(binascii.hexlify(pyaes.AESModeOfOperationCTR(binascii.unhexlify(Data.KeyData[0]),pyaes.Counter(int(Data.KeyData[1]))).encrypt(data)))
    def Denc(data: bytes):
        """Dencrypts The Data Passed Using The Default Aes Key Data\n
        :param data: Bytes String of The Data You Want to Decrypt\n
        :return: String of The Decrypted Data"""    
        return str(str(pyaes.AESModeOfOperationCTR(binascii.unhexlify(Data.KeyData[0]),pyaes.Counter(int(Data.KeyData[1]))).decrypt(binascii.unhexlify(data)))[2:-1])
class api:
    """Lower Level Api Functions For pastesite.org API"""
    def __init__(self):
        pass
    def scrapePastes(NumOfPages: int):
        """Gets all Pastes Up to the Specified Page Number\n
        :param NumOfPages: Int of the Number of Pages You Want to Scrape\n
        :return: List of all Pastes On Every Page Up to NumOfPages in PasteObj Format"""
        NumOfPages=int(10 if(type(NumOfPages) != int) else NumOfPages)
        pasteList=[]
        [[pasteList.append(dict({"url": lst[0],"code": str(lst[0].split("/")[-1]),"title": lst[1],"user": lst[2],"lang": lst[3],"time": lst[4]})) for lst in re.findall(re.compile(r"\<tr\>\n.+\<td\ class=\"first\"\>\<a href=\"(https:\/\/pastesite\.org\/view\/.{8})\"\>(.+)\<\/a.+\n.+\<td\>(.+)\<.+\n.+\<td\>(.+)\<.+\n.+\n.+\<td\>(.+)\<.+\n.+\/tr\>"), requests.get(f"https://pastesite.org/lists/{str(_*15)}").text)] for _ in range(NumOfPages)]
        return list(pasteList)
    def paste(title: str, data: str, user: str, expire: str, lang: str, keys: list):
        """Creates A New Paste\n
        :param title: String of The Title of The Paste\n
        :param data: String of Data to Be Encrypted Then Pasted\n
        :param user: String of UserName to Post Under\n
        :param expire: String of the Time At Which The Paste Should Expire(Full List of Times in Data.ExpireOptionsList)\n
        :param lang: String of The Paste Text Format\n
        :param keys: List of [AesKey, AesIV]\n
        :return: Bool (True If The Paste Was Successful Or False If It Was Not)"""
        bk=Data.KeyData
        Data.KeyData=keys 
        pd=f"name={user}&title={title}&lang={lang}&code={AesObj.Enc(data)}&expire={expire}&submit=submit"
        Data.KeyData=bk
        headers=dict({"Host": "pastesite.org","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate, br","Content-Type": "application/x-www-form-urlencoded","Content-Length": f"{len(pd)}","Origin": "https://pastesite.org","Connection": "keep-alive","Referer": "https://pastesite.org/",})
        ck=dict({"stikked": str(requests.get("https://pastesite.org/").cookies.get("stikked"))})
        req=requests.post("https://pastesite.org/", data=pd, headers=headers, cookies=ck, allow_redirects=False)
        if(req.status_code == 303):
            return True
        else:
            return False
    def scrapeUser(NumOfPages: int):
        """Gets all of the Pastes Found From The Default User\n
        :param NumOfPages: Int of the Number of Pages You Want to Scrape\n
        :return: List of all Pastes Created By The Default User in PasteObj Format"""
        NumOfPages=int(10 if(type(NumOfPages) != int) else NumOfPages)
        pasteList=[]
        [[pasteList.append(dict({"url": lst[0],"code": str(lst[0].split("/")[-1]),"title": lst[1],"user": lst[2],"lang": lst[3],"time": lst[4]})) if(lst[2] == Data.UserName) else "" for lst in re.findall(re.compile(r"\<tr\>\n.+\<td\ class=\"first\"\>\<a href=\"(https:\/\/pastesite\.org\/view\/.{8})\"\>(.+)\<\/a.+\n.+\<td\>(.+)\<.+\n.+\<td\>(.+)\<.+\n.+\n.+\<td\>(.+)\<.+\n.+\/tr\>"), requests.get(f"https://pastesite.org/lists/{str(_*15)}").text)] for _ in range(NumOfPages)]
        return list(pasteList)
    def searchPastes(PasteList: list, **kwargs):
        """Filters Pastes In PasteList With The Specified Paramater\n
        :param PasteList: List of PasteObj\n
        :param kwargs: Specify one or More args For Filtering\n
        :return: List of PasteObj With the Specified Paramaters\n
        **kwargs={user=None, title=None, lang=None}"""
        u=kwargs.get("user") if(kwargs.get("user") != None) else False
        t=kwargs.get("title") if(kwargs.get("title") != None) else False
        l=kwargs.get("lang") if(kwargs.get("lang") != None) else False
        a=kwargs.get("after") if(kwargs.get("after") != None) else False
        b=kwargs.get("before") if(kwargs.get("before") != None) else False
        OutList=[]
        for p in PasteList:
            if(u!=False and p['user']==u):
                OutList.append(p)
            if(t!=False and p['title']==t):
                OutList.append(p)
            if(l!=False and p['lang']==l):
                OutList.append(p)
            if(a!=False and p['time']==a):
                OutList.append(p)
            if(b!=False and p['time']==b):
                OutList.append(p)
            if(u==False and t==False and l==False and a==False and b==False):
                    OutList.append(p)
        return list(OutList)
    def scrapePaste(paste: dict, keys: list):
        """Scrapes the Data From a Paste Using the Keys Passed\n
        :param paste: PasteObj\n
        :param keys: List of [AesKey, AesIV]\n
        :return: String of Dencrypted Data from Paste"""
        bk=Data.KeyData
        Data.KeyData=keys        
        req=AesObj.Denc(requests.get(f"https://pastesite.org/view/raw/{paste['code']}").text[2:-1])
        Data.KeyData=bk
        return str(req)
class PasteApi:
    """Easy To Use PasteSite.org API Wrapper"""
    def __init__(self):
        pass
    def Paste(title: str, data: str):
        """Creates A New Paste Using the Deafult UserName and Keys\n
        :param title: String of the Title of the Paste\n
        :param data: String of Data to Be Encrypted Then Pasted\n
        :return: True If the Paste Was Successful Or False if it was Not\n"""
        if(Data.UserName==""):
            raise exeptions.NoUser
        var=True if(api.paste(title, data, Data.UserName, Data.ExpireOptionsList[Data.ExpireInt], 'text', Data.KeyData)) else False      
        if(var==True):
            print("Successfully Pasted") if(Data.DefSilent==False) else None
            return True
        else:
            print("Failed") if(Data.DefSilent==False) else None
            return False
    def GetLastPaste():
        """Retrieves The Most Recent Paste From The Default User\n
        :return: PasteObj if a Paste Was Found and False if else"""
        v=api.scrapeUser(Data.DefScrapeNum)
        return dict(v[0]) if(v!=[]) else False
    def Scrape(paste: dict):
        """Scrapes the Data From a PasteObj Using the Default Keys\n
        :param paste: PasteObj\n
        :return: String of Dencrypted Data from Paste"""
        return str(api.scrapePaste(paste, Data.KeyData))
    def SearchByTitle(title: str, NumOfPages: int):
        """Filters Through All Pastes up to NumOfPages and only returns a list of valid matches\n
        :param : String of the Title You Want To Search\n
        :param NumOfPages: Int of the Number of Pages You Want to Scrape\n
        :return: List Of PasteObj With The Specified Title"""
        pl=api.scrapePastes(NumOfPages)
        return list(api.searchPastes(pl, title=title))
    def SearchByUser(user: str, NumOfPages: int):
        """Filters Through All Pastes up to NumOfPages and only returns a list of valid matches\n
        :param User: String of the User You Want To Search\n
        :param NumOfPages: Int of the Number of Pages You Want to Scrape\n
        :return: List Of PasteObj With The Specified User"""
        pl=api.scrapePastes(NumOfPages)
        return list(api.searchPastes(pl, user=user))
    def SearchByLang(lang: str, NumOfPages: int):
        """Filters Through All Pastes up to NumOfPages and only returns a list of valid matches\n
        :param : String of the Text Format You Want To Search\n
        :param NumOfPages: Int of the Number of Pages You Want to Scrape\n
        :return: List Of PasteObj With The Specified Format"""
        pl=api.scrapePastes(NumOfPages)
        return list(api.searchPastes(pl, lang=lang))
    def WaitForPaste(RefreshTime: int):
        """Check For Pastes from the Default User if none are found the function will wait RefreshTime then check again until it has found a paste\n
        :param RefreshTime: Int of the Ammount Of Time to Wait before Checking again\n
        :return: list(paste,pastetxt)"""
        paste=dict()
        s=time.time()
        while(paste == dict()):
            os.system("cls") if(Data.DefSilent==False) else None
            print(f"Runtime: {Data.time_convert(time.time()-s)}") if(Data.DefSilent==False) else None
            print("Scraping...") if(Data.DefSilent==False) else None
            data=api.scrapeUser(1)
            print(f"Scraped {len(data)} pastes") if(Data.DefSilent==False) else None
            if(len(data) >= 1):
                paste=dict(data[0])
                pastetxt=api.scrapePaste(paste, Data.KeyData)
                print("Decyptred Text: "+pastetxt) if(Data.DefSilent==False) else None
            else:
                time.sleep(RefreshTime)
            runtime=float(time.time()-s)  
        return (paste, pastetxt, runtime)
         