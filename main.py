import csv

class PointCity():
    cities = {}
    points = {}
    def __init__(self,cities_file,points_file):
        self.csv_to_points(cities_file,self.cities,city=True)
        self.csv_to_points(points_file,self.points)

    def csv_to_points(self,file,dic,city=False):
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_num = 0
            for row in csv_reader:
                if line_num > 0:
                    try:
                        if city:
                            dic[row[0]] =((int(row[1]),int(row[2])),(int(row[3]),int(row[4])))
                        else:
                            dic[row[0]] = (int(row[1]), int(row[2]))
                    except Exception as ex:
                        print(ex)
                        pass
                line_num += 1

    def point_save(self,point,x,y,city='None'):
        self.points_wr.writerow([point,x,y,city])


    def check_points(self):
        print(self.cities,self.points)
        self.output_file = open('output_points.csv', mode='w')
        self.points_wr = csv.writer(self.output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for point,point_xy in self.points.items():
            for c_name,coords in self.cities.items():
                print(coords[0][0] <= point_xy[0] <= coords[1][0]) and (coords[0][1] <= point_xy[1] <= coords[1][1])
                if (coords[0][0] <= point_xy[0] <= coords[1][0]) and (coords[0][1] <= point_xy[1] <= coords[1][1]):
                    self.point_save(point,point_xy[0],point_xy[1],c_name)
                    break
            else:
                self.point_save(point,point_xy[0],point_xy[1])
        else:
            self.output_file.close()
T = PointCity('cities.csv','points.csv')
T.check_points()