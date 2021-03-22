from easygui import *
import os
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from pinkbike import Pinkbike
from craigslist import Craigslist
from facebook import Facebook



# class Pinkbike:
#     def __init__(self,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
#         self.biketype = biketype
#         self.year = year
#         self.adtitle = adtitle
#         self.condition = condition
#         self.material = material 
#         self.frameSize = frameSize
#         self.wheelSize = wheelSize
#         self.forkTravel = forkTravel
#         self.rearTravel = rearTravel
#         self.phoneNumber = phoneNumber
#         self.askingPrice = askingPrice 
#         self.priceOffer = priceOffer
#         self.trades = trades
#         self.shipping = shipping
#         self.description = description 

        

#     driver.get('https://pinkbike.com/user/login')
#     #driver.implicitly_wait(10)
#     print(driver.title)
#     def loginUser(name,password):

#         driver.find_element_by_name('username-login-loginlen').send_keys(name)
#         driver.find_element_by_name("password-password-lt200").send_keys(password)
#         driver.find_element_by_name("submitbutton['Login']").send_keys(Keys.RETURN)
        





#     def postadd(self,biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description):
#         driver.find_element_by_xpath("/html/body/div[1]/div[3]/ul/li[6]/a").click()#buysell button
#         driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div/div[1]/ul/li[6]/a/span").click()#postadd btn
#         bikeelems = {'year':year,'itemcondition':condition,'material':material,'framesize':frameSize,'wheelsize':wheelSize,'fronttravel':forkTravel,'reartravel':rearTravel,'currency':'CAD $','offer':priceOffer,'trade':trades,'shipping':shipping}
#         #bikeelems2 = {'fronttravel':forkTravel, 'reartravel':rearTravel}
#         driver.find_element_by_link_text(biketype).click()
#         #selectOption('fronttravel', forkTravel)
#         for y in bikeelems:
#             selectOption(y, bikeelems[y])
        
#         driver.find_element_by_name('title-gt1-textbb-lt55').send_keys(adtitle)
#         driver.find_element_by_name('phone-textbb-lt20').send_keys(phoneNumber)
#         driver.find_element_by_name('price-gt0-lt8-float').send_keys(askingPrice)
#         driver.find_element_by_name('description-gt3-textbb').send_keys(description)
#         driver.find_element_by_name("submitbutton['Upload NewclearPhotos']").click()
        
#         droparea = driver.find_element_by_xpath('//*[@id="uppy-select-files"]/div/div[2]/div/div[1]/ul/li[1]/input')
#         droparea.send_keys(os.getcwd()+"/testbike.jpg")
#         driver.find_element_by_id('idup').click()
#         try:

#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.NAME, "submitbutton['Save']"))
#             ) 
#             element.click()
#             #driver.find_elements_by_name("submitbutton['Save']").click()
#         finally:
#             pass
            

#     def selectOption(trate, wantedTrate):
#         tratename = driver.find_element_by_name(trate + '-locationselect')
#         options = tratename.find_elements_by_tag_name('option')
#         tratename.click()
#         for i in options:
#             if i.text == wantedTrate:
#                 i.click()
            
#     def runPB():
#         loginUser('boogiej', 'testaccount')
#         postadd(biketype,year,adtitle,condition,material,frameSize,wheelSize,forkTravel,rearTravel,phoneNumber,askingPrice,priceOffer,trades,shipping,description)
#         driver.quit()



#     # def craigsMain():
#     #     driver.get('https://accounts.craigslist.org/login')


#     # pinkbikeMain()
#     # craigsMain()
version = "Ontop Auto Add v.1.0"

#bikeorpartChoice = buttonbox(msg="Yo! You posting a bike or a part?", title=version, choices=('Bike','Part'))


def bike():
    basicInfoBike = []
    basicInfoBike= multenterbox("Enter info",title=version, fields=('Add Title', 'Price','Year','Make','Model'))
    
    optConvBike = {
        'typeBike_PB.CR':{'All Mountain/Enduro Bikes':'mountain','DH Bikes':'mountain','XC Bikes':'mountain','Dirt Jump Bikes':'bmx','Kids Bikes':'kids','Vintage Bikes':'other'},
        'materialBike_PB.CR':{'Aluminium':'aluminum','Carbon Fiber':'carbon fiber','Chromoly':'composite','Steel':'steel','Titanium':'titanium','Unknown':'other/unknown'},
        'framesizeBike_CR.PB':{'Extra Small':'XS','Small':'S','Medium':'M','Large':'L','Extra Large':'XL'},
        'wheelSizeBike_CR.PB':{'10 in':'16" or less','12 in':'16" or less','14 in':'16" or less','16 in':'16" or less','18 in':'Unkown','20 in':'20"','24 in':'24"','26 in':'26"','27.5 in':'27.5" / 650B','29 in':'29"','650C':'650C','700C':'700C'},
        'condition_PB.CR':{'New - Dealer/Store':'new','Excellent':'excellent','Good':'good','Poor':'fair','For parts / not working':'salvage'},
    }
    
    # forksusPB_Inp = ''
    # rearsusPB_Inp = ''
    # typeBike_Inp = choicebox('What is the type of the bike?', title=version, choices=('All Mountain/Enduro Bikes','DH Bikes','XC Bikes','Dirt Jump Bikes','Kids Bikes','Vintage Bikes'))
    # materialBike_Inp = choicebox('What is the material of the frame?', title=version, choices=('Aluminium','Carbon Fiber','Chromoly','Steel','Titanium','Unknown')) 
    # frameSizeBike_Inp = choicebox('What is the size of the frame?', title=version, choices=('Extra Small','Small','Medium','Large','Extra Large'))
    # suspensionCR_Inp = choicebox('What type of suspension?', title=version, choices=('none (rigid)','suspension fork (hardtail)','frame and fork (full suspension)'))
    # if (suspensionCR_Inp == 'none (rigid)'):
    #     forksusPB_Inp = '0 mm'
    #     rearsusPB_Inp = '0 mm'
    # elif(suspensionCR_Inp == 'suspension fork (hardtail)'):
    #     forksusPB_Inp = choicebox('How much travel does the fork have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unkown'))
    #     rearsusPB_Inp = '0 mm'
    # elif(suspensionCR_Inp == 'frame and fork (full suspension)'):
    #     forksusPB_Inp = choicebox('How much travel does the fork have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','Unkown'))        
    #     rearsusPB_Inp = choicebox('How much travel does the rear have?', title=version, choices=('60 mm','80 mm','100 mm','110 mm','120 mm','140 mm','160 mm','170 mm','180 mm','190 mm','200 mm','203 mm','208 mm','215 mm','255 mm','Unkown'))

    # wheelSizeBike_Inp = choicebox('What is the size of the wheels?', title=version, choices=('10 in','12 in','14 in','16 in','18 in','20 in','24 in','26 in','27.5 in','29 in','650C','700C'))
    # conditionBike_Inp = choicebox('What is the condition of the bike?', title=version, choices=('New - Dealer/Store','Excellent','Good','Poor','For parts / not working'))
    # bikeDescription_Inp = enterbox("What is the description of the bike?", title=version)
    #textbox("Press ok to select photos of bike", title=version)
    photoBike_Inp = filesavebox()
    print(photoBike_Inp)
    #PATH = '/Users/sven/Desktop/OntopAdds/chromedriver'
    #driver = webdriver.Chrome(PATH) 
    #pbLoad = Pinkbike(driver,'svenyensen','pythonz2',typeBike_Inp,basicInfoBike[2],basicInfoBike[0],conditionBike_Inp,materialBike_Inp,optConvBike.get('framesizeBike_CR.PB')[frameSizeBike_Inp],optConvBike.get('wheelSizeBike_CR.PB')[wheelSizeBike_Inp],forksusPB_Inp,rearsusPB_Inp,'604-990-9550',basicInfoBike[1],'Firm','No Trades','Local pickup only',bikeDescription_Inp)
    #pbLoad.runPB()

    #CR = Craigslist(driver,'part','bit4104@gmail.com','testaccountferda','Test Bike','90','its a sick bike','fork only','Small','santacruz','nomad','mountain','alloy','10 in','frame and fork (full suspension)','drum','drop','none','new')
    #CR.run()

bike()
# if bikeorpartChoice == "Bike":
#     bike()

#pbLoad = Pinkbike(driver,'johnbaconback','testaccountferda',"All Mountain/Enduro Bikes",'2019','MEGATeasdasstaasdsdBike3','Good','Steel','S','26"','180 mm','160 mm','778998877','800','Firm','No Trades','Local pickup only','its a super super megawickeasdasdasd bike eh')
#pbLoad.runPB()

#CR = Craigslist(driver,'part','bit4104@gmail.com','testaccountferda','Test Bike','90','its a sick bike','fork only','Small','santacruz','nomad','mountain','alloy','10 in','frame and fork (full suspension)','drum','drop','none','new')
#CR.run()

# fB = Facebook(driver,'bit4104@gmail.com','testaccountferda!',"All Mountain/Enduro Bikes",'2019','MEGATestaasdsdBike3','Good','Steel','S','26"','180 mm','160 mm','778998877','800','Firm','No Trades','Local pickup only','its a super super megawickeasdasdasd bike eh')
# fB.runFB()