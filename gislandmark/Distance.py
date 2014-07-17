from math import sqrt

def main(infile):
    infile = open(infile)
    cabstop = []
    cabCcluster = []
    statcluster = []
    for line in infile:
        x = line.split()
        cabstop.append(x)
    
    booleanTest = []
    i = 0
    boolean = '1'
    for line in cabstop:
        # tests to see if there has been a pick up or drop off change
        if line[2] == boolean:
            booleanTest.append(line)
            if boolean == '1':
                boolean = '0'
            else:
                boolean = '1'
    landmarks = [['Cab Company', 37.7513273, -122.3947337],['Montgomery Station',37.789256, -122.401407]]
    # 0.00082 degrees approx 300 ft. 
    onehun_ft_2_deg = 0.00082
    cabCx1 = landmarks[0][1]
    cabCy1 = landmarks[0][2]
    statx1 = landmarks[1][1]
    staty1 = landmarks[1][2]
    for droponoff in cabstop:
        
        x2 = float(droponoff[0])
        y2 = float(droponoff[1])
        #dist = sqrt((x2-x1)**2 + (y2-y1)**2)
        distcab = sqrt((x2-cabCx1)**2 + (y2-cabCy1)**2)
        diststat = sqrt((x2 - statx1 )**2 + (y2 - staty1)**2)
        if distcab < onehun_ft_2_deg:
            cabCcluster.append(droponoff)
        elif diststat < onehun_ft_2_deg:
            statcluster.append(droponoff)
        else:
            None
            
    print cabCcluster
    print '\n'
    print '\n'
    print '\n'
    print '\n'
    print statcluster
        
main('new_abcoij.txt')    