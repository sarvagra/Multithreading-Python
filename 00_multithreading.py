import threading 
import urllib.request

def test(id):
    print("prog start %d"% id)

thread =[threading.Thread(target=test,args=(i,)) for i in range(10)]
for t in thread :
    t.start()

def file_download(url , filename):
    urllib.request.urlretrieve(url,filename)

file_download('https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt',"test.txt")
url_list  = ['https://raw.githubusercontent.com/itsfoss/text-files/master/agatha.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sherlock.txt','https://raw.githubusercontent.com/itsfoss/text-files/master/sample_log_file.txt']

file_name_list = ['data1.txt','data2.txt','data3.txt']
ther = [threading.Thread(target=file_download , args = (url_list[i] , file_name_list[i]) ) for i in range(len(url_list))]

for t in ther :
    t.start()