import pandas as pd

class converter () :
    def __init__(self):
        self.dmc_list = pd.read_csv('static/pixel_converter/resource/DMC Cotton Floss converted to RGB Values.csv',
                               encoding=' CP949', engine='python')

    def rgb_to_dmc(self, rgb):
        dmc_list = self.dmc_list
        res = [[999, 'hello world']]
        for i in range(len(dmc_list)):
            r, g, b = dmc_list.loc[i][2], dmc_list.loc[i][3], dmc_list.loc[i][4]
            gap = abs(r - rgb[0]) + abs(g - rgb[1]) + abs(b - rgb[2])

            if res[-1][0] > gap:
                res.append([gap, dmc_list.loc[i][0]])
        return res[-1][1]

    def dmc_to_rgb(self, dmc_code):
        dmc_list = self.dmc_list
        row = dmc_list.loc[(dmc_list['Floss#'] == str(dmc_code))]
        r, g, b = int(row['Red'].values), int(row['Green'].values), int(row['Blue'].values)
        result = [r, g, b]
        return result

