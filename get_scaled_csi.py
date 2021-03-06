import numpy as np
import math
import matplotlib.pyplot as plt
    
def dbinv(csi_st):
    ret = pow(10, csi_st/10)
    return ret 

def db(csi_st):
    ret = np.log10(csi_st) * 10
    return ret

def get_total_rss(csi_st):
    rssi_mag = 0;
    if csi_st[4] != 0:
        rssi_mag = rssi_mag + dbinv(csi_st[4])
    if csi_st[5] != 0:
        rssi_mag = rssi_mag + dbinv(csi_st[5])
    if csi_st[6] != 0:
        rssi_mag = rssi_mag + dbinv(csi_st[6])
        
    ret = db(rssi_mag) - 44 - csi_st[8]    
    return ret


def get_scaled_csi(csi_st):
    
    csi = csi_st[11];

    csi_sq = csi * np.conjugate(csi).real
    csi_pwr = sum(csi_sq.flatten())
    rssi_pwr = dbinv(get_total_rss(csi_st))

    scale = rssi_pwr / (csi_pwr / 30)

    if csi_st[7] == -127:
        noise_db = -92
    else:
        noise_db = csi_st[7]
    thermal_noise_pwr = dbinv(noise_db)
    
    quant_error_pwr = scale * (csi_st[2] * csi_st[3])

    total_noise_pwr = thermal_noise_pwr + quant_error_pwr;

    ret = csi * math.sqrt(scale / total_noise_pwr);
    if csi_st[3] == 2:
        ret = ret * math.sqrt(2);
    elif csi_st[3] == 3:
        ret = ret * math.sqrt(dbinv(4.5));

    return ret

'''
if __name__ == '__main__':
    tmp = [4, 72, 3, 1, 33, 37, 41, 129, 38, [3, 2, 1], 256, np.array([[[  3.83500000e+03 +2.57400000e+03j,
           1.20000000e+01 +1.60000000e+01j,
           3.15110000e+04 +3.19950000e+04j,
           1.80000000e+03 +2.31000000e+02j,
           2.38000000e+02 +4.90000000e+02j,
           9.93000000e+02 +1.02700000e+03j,
           7.49000000e+02 +2.82000000e+02j,
           8.20300000e+03 +4.64000000e+03j,
           3.10500000e+03 +1.29200000e+03j,
           2.87000000e+02 +2.37000000e+02j,
           2.38130000e+04 +2.81250000e+04j,
           1.76800000e+03 +7.42000000e+02j,
           4.78000000e+02 +2.57000000e+02j,
           6.63500000e+03 +3.60900000e+03j,
           2.03900000e+03 +5.43000000e+02j,
           6.67200000e+03 +4.12200000e+03j,
           1.82200000e+03 +1.54300000e+03j,
           7.93000000e+02 +7.51000000e+02j,
           2.50930000e+04 +2.73620000e+04j,
           2.03000000e+03 +3.55900000e+03j,
           2.25000000e+02 +5.08000000e+02j,
           5.86400000e+03 +5.14200000e+03j,
           5.14000000e+02 +5.46000000e+02j,
           5.40400000e+03 +2.83700000e+03j,
           5.40900000e+03 +4.85300000e+03j,
           5.22000000e+02 +4.78000000e+02j,
           2.60880000e+04 +2.96690000e+04j,
           2.52700000e+03 +3.59300000e+03j,
           2.49000000e+02 +3.20000000e+01j,
           6.66600000e+03 +3.86600000e+03j],
        [  1.54600000e+03 +2.82200000e+03j,
           1.20000000e+01 +1.01600000e+03j,
           2.89240000e+04 +3.01920000e+04j,
           2.80000000e+03 +7.62000000e+02j,
           4.99000000e+02 +1.30000000e+01j,
           4.86800000e+03 +3.09100000e+03j,
           2.73000000e+02 +9.00000000e+00j,
           6.32500000e+04 +1.78300000e+03j,
           3.07700000e+03 +6.38000000e+03j,
           2.44000000e+02 +1.00800000e+03j,
           3.24930000e+04 +3.07180000e+04j,
           3.82600000e+03 +3.85400000e+03j,
           2.57000000e+02 +1.90000000e+01j,
           3.08600000e+03 +2.57200000e+03j,
           1.55400000e+03 +5.18000000e+02j,
           6.32480000e+04 +1.78300000e+03j,
           3.33400000e+03 +7.91700000e+03j,
           7.58000000e+02 +7.50000000e+02j,
           3.17220000e+04 +2.96910000e+04j,
           3.82100000e+03 +2.57400000e+03j,
           5.11000000e+02 +2.50000000e+01j,
           4.37200000e+03 +3.34500000e+03j,
           5.38000000e+02 +1.01800000e+03j,
           5.91470000e+04 +4.87000000e+02j,
           2.80200000e+03 +5.86600000e+03j,
           2.29000000e+02 +0.00000000e+00j,
           6.13100000e+03 +3.17670000e+04j,
           7.82000000e+02 +2.06700000e+03j,
           2.78000000e+02 +5.09000000e+02j,
           1.33270000e+04 +2.03600000e+03j],
        [  7.43500000e+03 +2.53000000e+02j,
           7.71000000e+02 +2.43000000e+02j,
           3.09650000e+04 +1.66320000e+04j,
           1.77800000e+03 +6.00000000e+00j,
           5.10000000e+02 +1.50000000e+01j,
           2.57200000e+03 +1.02500000e+04j,
           1.29600000e+03 +2.53000000e+02j,
           6.17020000e+04 +2.28900000e+03j,
           5.11200000e+03 +6.38700000e+03j,
           7.55000000e+02 +2.54000000e+02j,
           2.03900000e+03 +1.63910000e+04j,
           3.07100000e+03 +1.10000000e+01j,
           2.62000000e+02 +9.00000000e+00j,
           5.22000000e+02 +1.43380000e+04j,
           1.54600000e+03 +2.54000000e+02j,
           6.32380000e+04 +6.16870000e+04j,
           5.63000000e+03 +2.29300000e+03j,
           5.02000000e+02 +2.49000000e+02j,
           1.26700000e+03 +2.86760000e+04j,
           3.32200000e+03 +2.06000000e+03j,
           2.62000000e+02 +1.30000000e+01j,
           7.81000000e+02 +4.09900000e+03j,
           1.10000000e+01 +2.48000000e+02j,
           6.22090000e+04 +2.29100000e+03j,
           6.39000000e+03 +4.34400000e+03j,
           1.01200000e+03 +3.00000000e+00j,
           3.32400000e+03 +3.07320000e+04j,
           2.31200000e+03 +2.05700000e+03j,
           2.67000000e+02 +2.53000000e+02j,
           1.43430000e+04 +2.48000000e+02j]]],dtype = 'complex')]
    csi = get_scaled_csi(tmp)
    index = 0;
    p = np.zeros((30,30), dtype='double', order = 'C')
    p[index*3] = db(abs(csi[0,0,:].flatten()));
    p[index*3+1] = db(abs(csi[0,1,:].flatten()));
    p[index*3+2] = db(abs(csi[0,2,:].flatten()));
    plt.close('all')
    for i in range(0,10):
        plt.plot(p[i*3], 'r')
        plt.plot(p[i*3+1], 'b')
        plt.plot(p[i*3+2], 'g')
'''