import json, urllib.request


def BRCD_CD(apikey, startRow, endRow, BAR_BRCD_CD):
    output_list = []

    keyId = 'I2570'

    url = 'http://openapi.foodsafetykorea.go.kr/api/' + apikey + '/' + keyId + '/json/' + str(startRow) + '/' + str(
        endRow) + '/BRCD_NO=' + BAR_BRCD_CD

    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    output = output[keyId]

    try:
        output = output['row']
        output_1 = output[0]

        output_list.append(output_1['HTRK_PRDLST_NM'])
        output_list.append(output_1['HRNK_PRDLST_NM'])
        output_list.append(output_1['PRDLST_NM'])

        return output_list
    except:
        return 'no data'

    # (대분류,중분류,소분류) 리턴
    # 대분류 = HTRK_PRDLST_NM
    # 중분류 = HRNK_PRDLST_NM
    # 소분류 = PRDLST_NM


#########################################

def BAR_CD(apikey, startRow, endRow, BAR_BRCD_CD):
    output_list = []

    keyId = 'C005'

    url = 'http://openapi.foodsafetykorea.go.kr/api/' + apikey + '/' + keyId + '/json/' + str(startRow) + '/' + str(
        endRow) + '/BAR_CD=' + BAR_BRCD_CD
    
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)

    output = output[keyId]

    try:
        output = output['row']
        output_1 = output[0]

        output_list.append('기타')
        output_list.append(output_1['PRDLST_DCNM'])
        output_list.append(output_1['PRDLST_NM'])

        return output_list
    except:
        return 'no data'

    # ('기타',중분류,소분류) 리턴
    # 중분류 = PRDLST_DCNM
    # 소분류 = PRDLST_NM


#########################################

def main():
    apikey = '0acf2740895d47c4a77c'

    startRow = 1
    endRow = 1
    BAR_BRCD_CD = '8801005655163'
    # 8801007712031 소시지
    # 8801007552552 어묵

    BRCD_CD_output = BRCD_CD(apikey, startRow, endRow, BAR_BRCD_CD)
    BAR_CD_output = BAR_CD(apikey, startRow, endRow, BAR_BRCD_CD)

    if BRCD_CD_output != 'no data':
        print(BRCD_CD_output)
    elif BAR_CD_output != 'no data':
        print(BAR_CD_output)
    else:
        print(0)


if __name__ == "__main__":
    main()
