print("                            PROJECT AGRICULTURE ASSIST")
print("Press 1 if you know about the pH,Humidity,Type of Soil,Rainfall and Temperature of your field")
print("Press 2 to get information about some crops")
#print('if you only know about your soil type then press 3')
uc=int(input('Enter Your Choice:-'))
if(uc==1):
       ph=float(input("Enter The ph Value Of Your Crop Land: "))
       h=float(input("Enter The Humidity of Your Crop Land: "))
       rf=int(input("Enter The Rainfall per Season in Your Area(Where you are planning to grow the crop): "))
       t=float(input("Enter The Temperature Of Your Area(Where you are planning to grow the crop): "))    
       print("Type 1 for clay ")
       print("Type 2 for loamy ")
       print("Type 3 for loam texture ")
       print("Type 4 for black soil ")
       print("Type 5 for clay loam  ")
       print("Type 6 for laterite ")
       print("Type 7 for sandy ")
       print("Type 8 for alluvial ")
       print("Type 9 for loamy sandy ")
       print("Type 10 for red soil ")
       print("Type 11 for loamy sandy clay ")
       print("Type 12 for lava ")
       print("Type 13 for Red loam ")
       print("Type 14 for snady clay ")
       ''''print('Type 15 for alluvial ")
       print("Type 16 for alluvial ")
       print("Type 17 for alluvial ")'''
       st=int(input("Enter the appropriate number for your Soil type in your Crop Land from above data: "))
       if((ph>5.9 and ph<7.1)and(st==1 or st==2 or st==3 or st==4)and(t>19.9 and t<25.1)and(h>49.9 and h <60.1) and (rf>49.9 and rf<100.1)):
              print("Your field is apporpriate for crop of WHEAT")
       if((ph>6.9 and ph<7.1)and(st==1 or st==9)and(t>9.9 or t<25.1)and(h>9.4 and h <14.9) and (rf>24.9 and rf<40.1)):
              print("Your field is apporpriate for crop of MUSTARD")
       if((ph>5.7 and ph<8.1)and(st==2 or st==4 or st==6)and(t>19.9 and t<32.1)and(h>42.9 and h <46.1) and (rf>49.9 and rf<75.1)):
              print("Your field is apporpriate for crop of COTTON")
       if((ph>5.4 and ph<7.1)and(st==1 or st==2 or st==4 or st==10)and(t>20.9 and t<37.1)and(h>59.9 and h <80.1) and (rf>174.9 and rf<300.1)):
              print("Your field is apporpriate for crop of RICE(PADDY)")
       if((ph>7.4 and ph<8.1)and(st==8 or st==10 or st==2 or st==4 or st==6 or st==7)and(t>19.9 and t<29.1)and(h>54.9 and h <65.1) and (rf>39.9 and rf<60.1)):
              print("Your field is apporpriate for crop of PEARL MILLET(BAJRA)")
       if((ph>5.4 and ph<7.6)and(st==8 or st==2 or st==7)and(t>25.9 and t<29.1)and(h>39.9 or h <60.1) and (rf>49.9 or rf<60.1)):
              print("Your field is apporpriate for crop of KODO MILLET(JAWAR)")
       if((ph>5.9 and ph<7.6)and(st==8 or st==9 or st==7)and(t>25.9 and  t<29.1)and(h>11.9 or h <15.1) and (rf>84.9 or rf<100.1)):
              print("Your field is apporpriate for crop of GREEN GRAM (MOONG)")
       if((ph>6.4 and ph<7.6)and(st==8 or st==2 or st==12 or st==1)and(t>24.9 and  t<35.1)and(h>44.9 or h <65.1) and (rf>59.9 or rf<300.1)):
              print("Your field is apporpriate for crop of SUGARCANE")
       if((ph>6.4 and ph<7.6)and(st==8 or st==9 or st==1 or st==11)and(t>12.9 and  t<44.1)and(h>49.9 or h <55.1) and (rf>79.9 or rf<250.1)):
              print("Your field is apporpriate for crop of TEAK")
       if((ph>5.9 and ph<6.9)and(st==8 or st==9 or st==7 or st==1)and(t>24.9 and  t<29.1)and(h>84.9 or h <90.1) and (rf>39.9 or rf<60.1)):
              print("Your field is apporpriate for crop of WATERMELON")
       if((ph>5.9 and ph<6.9)and(st==8 or st==9 or st==7 or st==1)and(t>19.9 and  t<29.1)and(h>84.9 or h <90.1) and (rf>39.9 or rf<60.1)):
              print("Your field is apporpriate for crop of MUSKMELON")       
       if((ph>6.4 and ph<7.6)and(st==2 or st==7)and(t>17.9 and  t<25.1)and(h>79.9 or h <90.1)):
              print("Your field is apporpriate for crop of MARIGOLD")
       if((ph>6.1 or ph<6.9)and(st==10 or st==1 or st==7 or st==11 or st==14)and(t>21.9 and  t<32.1)and(h>11.9 or h <15.1) and (rf>84.9 or rf<100.1)):
              print("Your field is apporpriate for crop of TOMATO")
      # if((ph>5.9 or ph<7.6)and(st==8 or st==9 or st==7)and(t>25.9 and  t<29.1)and(h>11.9 or h <15.1) and (rf>84.9 or rf<100.1)):
       #       print("Your field is apporpriate for crop of GREEN GRAM (MOONG)")
       else:
                 print("Your field is not appropriate for Wheat,cotton,Mustard,Rice,Bajra,Jawar,Moong,Sugarcane,Teak,Waterlemon,Muskmelon,Marigold and Tomato crops as per our data of investagtion ")
                 print("DISCLAIMER :- OUR DATA IS GIVING OUTPUTS BASED ON YOUR CHOICES,WE ARE NOT RESPNOSIBLE FOR ANY TYPE OF LOSSES AND WE ARE NOT MUCH SURE ABOUT OUR THIS SOFTWARE THAT THIS IS PROVIDING 100% ACCURATE RESULT." )
elif(uc==2):
        print("Press 1 to know about the crop of WHEAT")
        print("Press 2 to know about the crop of MUSTARD")
        print("Press 3 to know about the crop of COTTON")
        print("Press 4 to know about the crop of RICE")
        print("Press 5 to know about the crop of PEARL MILLET(BAJRA)")
        print("Press 6 to know about the crop of KODO MILLET(JOWAR)")
        print("Press 7 to know about the crop of SUGARCANE ")
        print("Press 8 to know about the crop of TEAK")
        print("Press 9 to know about the crop of GREEN GRAM")
        print("Press 10 to know about the crop of SOYABEAN")
        print("Press 11 to know about the crop of BARLEY")
        print("Press 12 to know about the crop of CORN")
        print("Press 13 to know about the crop of FLAX")
        print("Press 14 to know about the crop of GRAM")
       #print("Press 1 to know about the crop of  WHEAT")
        #print("press 17 to get about WHEAT")
        #print("press 18 to get about WHEAT")
        cr=int(input("Enter Your Choice again :-"))
        if(cr==1):
              print("Wheat is mainly a rabi (winter) season crop in India.")
              print("Appropriate months for sowing--NOVEMBER,In beginning of DECEMBER/n")
              print("First irrigation 20-25 days after sowing (Crown root initiation stage).\nSecond Irrigation 40-45 days after sowing (tillering stage).\nThird Irrigation 70-75 days after sowing (late jointing stage).\nFourth Irrigation 90-95 days of sowing (flowering stage).")
              print("Proper time for ripen of you crop--About 4 months.")
              print("Need of fertilizers in your crop: ")
              print("Nitrogen (N)-- 50 to 150 kg/ha.")
              print("Phosphorus (P) -- 20 to 60 kg/ha.")
              print("Potassium (K) -- 20 to 60 kg/ha.")
              print("Micronutrients, such as zinc (Zn), copper (Cu), manganese (Mn), and boron (B), are required in small amounts but can significantly affect crop growth and yield.")
              print('''How can you remove weeds or insects from your field--- There are several herbicides available for use in wheat crops that can help control weeds. Here are some commonly used herbicides for weed control in wheat:

Glyphosate: Glyphosate is a non-selective herbicide that can be used to control a broad range of weeds in wheat crops. It is often used before planting or after harvest to control weeds in wheat stubble.

2,4-D: 2,4-D is a selective herbicide that is commonly used to control broadleaf weeds in wheat crops. It is typically applied during the early stages of crop growth.

Dicamba: Dicamba is another selective herbicide that is commonly used to control broadleaf weeds in wheat crops. It can be applied during the early stages of crop growth.

Atrazine: Atrazine is a selective herbicide that is commonly used to control grassy weeds in wheat crops. It is typically applied before planting or immediately after planting.

It is important to note that herbicides should be used only as directed and in accordance with label instructions. Farmers should also take appropriate safety precautions when handling and applying herbicides to ensure their own safety as well as the safety of the environment and neighboring communities. Additionally, farmers should always follow local regulations and guidelines for herbicide use to ensure that they are using these chemicals in a safe and responsible manner.''')
              print("Proper time for harvesting-- March,April")
        if(cr==2):
              print("Mustard is mainly a rabi (winter) season crop in India.")
              print("Appropriate months for sowing--september-october")
              print("First irrigation 20-25 days after sowing (Crown root initiation stage).\nSecond Irrigation 50-55 days after sowing (tillering stage).\nThird Irrigation 70-75 days after sowing (late jointing stage).")
              print("Proper time for ripen of you crop--About 3-4 months.")
              print("Need of fertilizers in your crop: ")
              print("Nitrogen (N)-- 50 to 80lbs/acre ")
              print("Phosphorus (P) -- 20 to 40 kg/ha.")
              print("Potassium (K) -- 20 to 40 kg/ha.")
              print("Micronutrients, such as zinc (Zn), copper (Cu), manganese (Mn), and boron (B), are required in small amounts but can significantly affect crop growth and yield.")
              print('''How can you remove weeds or insects from your field:-
                Contact herbicides (e.g., sulfuric acid, diquat, paraquat) kill 
                only the plant organs with which they are in contact.
                Translocated herbicides (e.g., amitrole, picloram, and 2,4-D) are
                effective against roots or other organs to which they are transported 
                from aboveground treated surfaces (i.e., soil). 
                in-crop herbicides, and pre-harvest herbicides.
                Within in-crop herbicides, there are soil active herbicides typically 
                applied prior to the seeding of the crop, and foliar
                herbicides applied after crop and weed emergence.''')
              print("Proper time for harvesting-- February-March.")
        if(cr==3):
              print("cotton is mainly a warm season(march-june) crop in India.")
              print("Appropriate months for sowing-(march-june)")
              print("First irrigation within a week  after sowing (Crown root initiation stage).\nSecond Irrigation 7-21 days after sowing (tillering stage).\nThird Irrigation 10-21(no fix days) days after sowing (late jointing stage).\nFourth Irrigation no fix days days of sowing (flowering stage).")
              print("Proper time for ripen of you crop--About 5-6 months.")
              print("Need of fertilizers in your crop: ")
              print("Nitrogen (N)-- 112 to 224 kg/ha.")
              print("Phosphorus (P) -- 45 to 112 kg/ha.")
              print("Potassium (K) -- 90 to 224 kg/ha.")
              print("Micronutrients, such as sulphur (s),  (Cu), manganeseium (Mg), and boron (B), are required in small amounts but can significantly affect crop growth and yield.")
              print('''for Weed Control:/n

1.Pre-emergent Herbicides: These are applied before the emergence of weeds to prevent their growth. Common pre-emergent herbicides used in cotton include pendimethalin, trifluralin, and metolachlor.

Post-emergent Herbicides: These are applied after weeds have emerged. Common post-emergent herbicides used in cotton include glyphosate, glufosinate, and dicamba. However, it's important to follow label instructions and guidelines, as herbicide resistance can be a concern.

Insect Control:

Insect Growth Regulators (IGRs): These insecticides target the growth and development of insect pests. Examples of IGRs used in cotton include methoxyfenozide and diflubenzuron.

Pyrethroids: Pyrethroid insecticides, such as bifenthrin, cypermethrin, and deltamethrin, are commonly used to control various insect pests in cotton, including bollworms, aphids, and whiteflies.

Neonicotinoids: Neonicotinoid insecticides, such as imidacloprid and thiamethoxam, are used for systemic control of sucking pests, including aphids and whiteflies.

Biological Controls: Some farmers employ biological control methods, such as using beneficial insects like ladybugs or releasing parasitic wasps, to manage specific pests in an environmentally friendly manner.

It's important to note that the use of pesticides should be done following proper guidelines, label instructions, and any local regulations in place. Integrated Pest Management (IPM) practices, which involve a combination of various control methods, including cultural, biological, and chemical methods, are generally recommended for sustainable pest management in cotton.

Again, consulting with local agricultural experts or extension services will provide specific recommendations on the most suitable and effective weed and insect control strategies for cotton in your area. ''')
              print("Proper time for harvesting-- july-nov but mainly in (August-October)")
        if(cr==5):
              print("Bajra is mainly a kharif (Summer/Rainy) season crop in India.")
              print("Appropriate months for sowing--July TO Mid-August,In beginning of July/n")
              print("As this crop is sown in rainy season so there is no need to irrigate your crop , if it is raining in your area within 4-6 Days .\n But if there is no raining then you have to irrigate your crop once when your feild is dry")
              print("Proper time for ripen of you crop--About 2-3 months.")
              print("Need of fertilizers in your crop:  ")
              print("Nitrogen (N)-- 80 to 150 kg/ha.")
              print("Phosphorus (P) -- 40 to 50 kg/ha.")
              print("Potassium (K) -- 40 to 60 kg/ha.")
              print("Micronutrients, such as zinc (Zn), copper (Cu), manganese (Mn), and iron (fe), are required in small amounts but can significantly affect crop growth and yield.")
              print('''How can you remove weeds or insects from your field--- There are several herbicides available for use in wheat crops that can help control weeds. Here are some commonly used herbicides for weed control in wheat:
oxadiargyl PE or oxadiargyl PE fb 2,4-D POE provide an effective weed control and better yield.
A mixture of atrazine and terbutryne (0.5 kg a.i.Jha each) was also lethal· to pearl· millet. However, crop was able to recover from phytotoxicity caused by atrazine at 0.75 a.i.Jha and terbutryne at 0.5 and 0.75 kg a.i.Jha in about 20 days
It is important to note that herbicides should be used only as directed and in accordance with label instructions. Farmers should also take appropriate safety precautions when handling and applying herbicides to ensure their own safety as well as the safety of the environment and neighboring communities. Additionally, farmers should always follow local regulations and guidelines for herbicide use to ensure that they are using these chemicals in a safe and responsible manner.''')
              print("Proper time for harvesting-- October To November")
        if(cr==6):
              print("Jowar is mainly a Kharif (Summer,rainy) season crop in India.")
              print("Appropriate months for sowing--june and july (In beginning of Rainy season)/n")
              print("Irrigation :-As this crop has been sown in rainy season ,so  there is no need to irrigate your crop ,if it is raining in your area within 4-6 days.\nBut if there is no rain then you have to irriagte ypur crop once, when your soil is dry. ")
              print("Proper time for ripen of you crop--90 to 120 days.")
              print("Need of fertilizers in your crop: ")
              print("Nitrogen (N)-- 80 to 120 kg/ha.")
              print("Phosphorus (P) -- 40 to 60 kg/ha.")
              print("Potassium (K) -- 40 to 60 kg/ha.")
              print("Micronutrients, such as zinc (Zn), copper (Cu), manganese (Mn), and boron (B), are required in small amounts but can significantly affect crop growth and yield.")
              print('''How can you remove weeds or insects from your field--- There are several herbicides available for use in wheat crops that can help control weeds. Here are some commonly used herbicides for weed control in wheat:

Glyphosate: Glyphosate is a non-selective herbicide that can be used to control a broad range of weeds in wheat crops. It is often used before planting or after harvest to control weeds in wheat stubble.

2,4-D: 2,4-D is a selective herbicide that is commonly used to control broadleaf weeds in wheat crops. It is typically applied during the early stages of crop growth.

Dicamba: Dicamba is another selective herbicide that is commonly used to control broadleaf weeds in wheat crops. It can be applied during the early stages of crop growth.

Atrazine: Atrazine is a selective herbicide that is commonly used to control grassy weeds in wheat crops. It is typically applied before planting or immediately after planting.

It is important to note that herbicides should be used only as directed and in accordance with label instructions. Farmers should also take appropriate safety precautions when handling and applying herbicides to ensure their own safety as well as the safety of the environment and neighboring communities. Additionally, farmers should always follow local regulations and guidelines for herbicide use to ensure that they are using these chemicals in a safe and responsible manner.''')
              print("Proper time for harvesting-- October and November")
        if(cr==7):
              print("Sugarcane is mainly a rabi (winter) season crop in India.")
              print("In general January to March is the period of planting sugarcane")
              print("the irrigations are given at 10-15 days interval during summer, 25-30 days interval during winter and if there is drought the crop should be irrigated during rainy season also as and when needed.")
              print("Proper time for ripen of you crop--About 10 months.")
              print("Need of fertilizers in your crop: ")
              print("Nitrogen (N)-- 50 to 75 kg/ha.")
              print("Phosphorus (P) -- 4 to 6 kg/ha.")
              print("Potassium (K) -- 15 to 25 kg/ha.")
              print("Micronutrients, such as zinc (Zn), copper (Cu), manganese (Mn), and boron (B), are required in small amounts but can significantly affect crop growth and yield.")
              print('''How can you remove weeds or insects from your field--- spraying is done with 2 kg Atrazine or Simazine in 500 litre water 
              after the sprouting of the sugarcane crop to check the weed's growth and spread.
              The mechanical method of weed control involves deep ploughing and collecting grass weeds, 
              burying weed seeds deep so they are ineffective, and hand weeding. This is the best way 
              to make sure that you are completely removing the weed problem, but due to its manual steps,
              it can be a very slow process.
              Some more practices include proper crop rotations, crop competition,
              clean cultivation, mulching, and more. By rotating your crops, you help break apart 
              the weeds so that they eventually die off. For mulching, you can use the trash you get 
              from your sugarcane to help suppress the growth of weeds.''')
              print("Proper time for harvesting-- December to March ")