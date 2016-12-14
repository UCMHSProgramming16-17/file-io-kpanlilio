#import module
import csv
#create file
csvfile = open('taehyung.csv', 'w')
#create csvwriter
csvwriter = csv.writer(csvfile, delimiter=',')
#write information
csvwriter.writerow(['I', 'Love', 'Taehyung'])
csvwriter.writerow(['Jin', 'Suga', 'Rapmon', 'Jhope', 'Jimin', 'Taehyung','Jungkook'])
#close file
csvfile.close()

# csbwriter.writerow(['a', 'b', 'hypotenuse'])
# for a in range(1, 101):
#     for b in range(1, 101):
#         hypotenuse = math.sqrt(a ** 2 + b ** 2)
#         csvwriter.writerow([a, b, hypotenuse])