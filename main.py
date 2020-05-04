import pynput
from pynput.mouse import Button, Controller, Listener
import cv2
from bs4 import BeautifulSoup as bs
import requests as rs
# import webbrowser
import numpy as np
import urllib.request as urllib
import io

class main():

    def process(self, img):
        
        return cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)[1]
    
    def url_to_img(self, url):
        resp = urllib.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)
        image = self.process(image)
        # cv2.imwrite('image.jpg',image)
        return image

    def draw_in_a_file(self):
        self.get_color_pixels()
        text = ''
        for i in self.img:
            text+='\n'

            for  j in i:
                if j<200:
                    text+='0'
                else:
                    text+=' '
        with open("drawn here.txt", "a") as f:
            f.write(text)

    def get_google_img(self):
        search = 'https://www.google.com/search?q='+self.keyword+'&tbm=isch&tbs=itp%3Aclipart&rlz=1C1CHBD_enIN845IN845&hl=en&ved=0CAEQpwVqFwoTCICOstOFmukCFQAAAAAdAAAAABAC&biw=1384&bih=665'
        res = rs.get(search)
        soup = bs(res.text, "html.parser")
        # print(soup)
        images = soup.find_all('img')
        url = ''
        for i in images:
            print('heeee')
            if i.has_attr('src'):
                if 'http' in i['src']:
                    print('HEE')
                    if i.has_attr('height'):
                        if int(i['height'])>100:
                            print('HEEHEE')
                            url = i['src']
                            break
        
        return self.url_to_img(url)
        


    def get_color_pixels(self):
        img = cv2.resize(self.img, (int(self.width/self.pwidth),int(self.height/self.pheight)))
        # cv2.imshow("img",img)
        # cv2.waitKey(0)
        # b,g,r = cv2.split(img)
        # pwidth =self.pwidth
        # pheight = self.pheight
        # bAvg = np.empty((int(self.width/self.pwidth), int(self.height/self.pheight)))
        # gAvg = np.empty((int(self.width/self.pwidth), int(self.height/self.pheight)))
        # rAvg = np.empty((int(self.width/self.pwidth), int(self.height/self.pheight)))
        # for i in range(int(self.width/self.pwidth-1)):
        #     for j in range(int(self.height/self.pheight-1)):
        #         bAvg[i][j] = np.mean(b[i*pwidth:(i+1)*pwidth][j*pheight:(j+1)*pheight])
        #         gAvg[i][j] = np.mean(g[i*pwidth:(i+1)*pwidth][j*pheight:(j+1)*pheight])
        #         rAvg[i][j] = np.mean(r[i*pwidth:(i+1)*pwidth][j*pheight:(j+1)*pheight])
#         self.newImg = cv2.merge((bAvg,gAvg,rAvg))
        self.img = img
    
    def on_click(x, y, button, pressed):
        print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x,y)))
    
    def draw(self):
        self.get_color_pixels
        

    # with Listener(on_click = on_click) as listener:
    #     listener.join()
# 419, 295
# 1329, 980
    def __init__( self ):
        print('hh')
        # self.img = cv2.imread('C:\\Users\\keshh\\OneDrive\\Pictures\\Pictures\\45642421_10157254930088676_919688390838845440_n.jpg')
        self.startX = 1329
        self.startY = 980
        self.width = 200
        self.height = 200
        self.pwidth = 3
        self.pheight = 3
        self.keyword = input('Enter what to draw')
        self.img = self.get_google_img()

        self.draw_in_a_file()
        

        # self.get_color_pixels()
        # cv2.imwrite('image.jpg',self.newImg)
        # cv2.waitKey(0)
        

if __name__ == "__main__":
    main = main()

    