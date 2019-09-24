#speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g) Where g = 9.8 m/s^2
#Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
import csv

class Solution:
    def  descendingOrder(self):
        fp1 = open("dataset1.csv", "r")
        fp1_data = fp1.read().split(' ')
        dino_dict = {}
        for i in xrange(1, len(fp1_data)-1):
            dino_dict[fp1_data[i].split(',')[0]] = {
                fp1_data[0].split(',')[1]: fp1_data[i].split(',')[1],
                fp1_data[0].split(',')[2]: fp1_data[i].split(',')[2]
            }
        fp1.close()

        fp2 = open("dataset2.csv", "r")
        fp2_data = fp2.read().split(' ')
        for i in xrange(1, len(fp2_data) - 1):

            if fp2_data[i].split(',')[0] in dino_dict:
                #import pdb;pdb.set_trace()
                dino_dict[fp1_data[i].split(',')[0]][fp1_data[0].split(',')[1]] = fp2_data[i].split(',')[1],
                dino_dict[fp1_data[i].split(',')[0]][fp1_data[0].split(',')[2]] = fp2_data[i].split(',')[2]
            else:
                dino_dict[fp2_data[i].split(',')[0]] = {
                    fp1_data[0].split(',')[1]: fp2_data[i].split(',')[1],
                    fp1_data[0].split(',')[2]: fp2_data[i].split(',')[2]
                }
        fp2.close()

        print dino_dict

    def descendingOrder2(self):
        with open('dataset1.csv','r') as f1:
            csv_obj = csv.reader(f1, delimiter=' ')
            print csv_obj
            print type(csv_obj)
            for line in csv_obj:
                print line
s=Solution()
s.descendingOrder2()


