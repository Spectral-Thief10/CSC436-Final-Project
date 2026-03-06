import requests
import json
cookies = {
    'zguid': '24|%24ce180a45-468e-48b9-b2ee-b8aec64e8904',
    'zgsession': '1|ca46c121-1c15-45f3-9900-1de2ff16c594',
    '_ga': 'GA1.2.204694719.1772742663',
    '_gid': 'GA1.2.707283442.1772742663',
    'zjs_anonymous_id': '%22ce180a45-468e-48b9-b2ee-b8aec64e8904%22',
    'zjs_user_id': 'null',
    'zg_anonymous_id': '%22d0733bc9-8e29-4a20-bf92-b1ce23afd729%22',
    'zjs_user_id_type': '%22encoded_zuid%22',
    '_pxvid': '3a8dc488-18d2-11f1-a67e-f2ef9b80a41d',
    'pxcts': '3a8dccfa-18d2-11f1-a67e-66eed7e27a83',
    '_gcl_au': '1.1.921206453.1772742666',
    'datagrail_consent_id': '7e84c9ce-057e-4c91-87ef-56e6d4914637.b0c71c78-349c-4016-940a-6f72266b55a9',
    'datagrail_consent_id_s': '7e84c9ce-057e-4c91-87ef-56e6d4914637.36657c5c-5729-4f85-a931-58d294324f40',
    '_scid': '5BC76Is7S4C9vbZVQWMZ3-sld2xHK_qK',
    'DoubleClickSession': 'true',
    '_ScCbts': '%5B%22230%3Bchrome.2%3A2%3A5%22%5D',
    '_pin_unauth': 'dWlkPU1XRTFaRFZoT1dZdE0yTXpaQzAwTldJd0xUZzVaV1l0WVRBeFpHTXdZMk16WkRNeg',
    '_tt_enable_cookie': '1',
    '_ttp': '01KJZV4X5QYVANT4YYPJBFEG2Y_.tt.1',
    '_fbp': 'fb.1.1772742669836.461872833728307676',
    '_sctr': '1%7C1772694000000',
    '_lr_geo_location_state': 'AZ',
    '_lr_geo_location': 'US',
    'g_state': '{"i_l":0,"i_ll":1772759221155,"i_b":"x4sgqkM3VznTgZEAHVfJj3WFwZantT/XhQgwzC1k1hI","i_e":{"enable_itp_optimization":16}}',
    'tfpsi': 'e37356a2-283a-4b5f-b218-c5abe6eef138',
    '_clck': '477glm%5E2%5Eg44%5E0%5E2255',
    'AWSALB': 'uuUUdsAfn5H9LBVpQ5iMNx9op+YFhT5SG9/12QfunOxEM75mEVRt1Zxyrs9fWb5qcG610H7S88S4457PHFt9yjw+TFHCBQ+ggKs9YHONYx7emuKPTknj3hpx71L4',
    'AWSALBCORS': 'uuUUdsAfn5H9LBVpQ5iMNx9op+YFhT5SG9/12QfunOxEM75mEVRt1Zxyrs9fWb5qcG610H7S88S4457PHFt9yjw+TFHCBQ+ggKs9YHONYx7emuKPTknj3hpx71L4',
    'JSESSIONID': '0B8C227020607B620399DE5F5A0E1530',
    '_px3': '5f80727a6ce21f23945870f12fa4a9a90bd5f8b26fc42399a81e6742066eaa51:CDp+bAi5NsWYmzH0vayS834h3mmGWXR9tVGbUS/l+GkYoEpCwSLhguUPWs5MnmxqHiDhDLUxzuU8iOnacrMqHQ==:1000:fL3gZsuDejxpadJHwzYlhs+EWY/Xaif79/fwTgadgdwajHJd0wXsV7RJ8y+0441g9CXHCR5abs06pufTWV+2SqAhwwm6pSBNSPz2xzCN0P5Qq6KDtGBQ2hrWhypDKWsyjMD5ssK5a/+gNQTQvpHPZqvN9YN2cxBL2HSEhsBHpcTCsAcA15qaglqElN2CTvT/ssGL5dGy04gCUQtFar/MwQZ2/c4xJ5ovKvdzjcRpR4TCANpkvzS+HdLKGlM5/onoFDldKOXHC5Xl5SdencaA0IvFWpduZa5oC6TaA+y2fQ7pvUi5o6cpbC3t8HKDiqTGIkUHeoegmV8cewPbH7YbWsdChoMSCRudjMpRiiCJ09pKdQD1jH/nDCisxpkGDBCZpU7ofIj54iyS3jrjVtMeNOz0NaAdRcummjy1zlv5xea+dp5Zu75PtC9o0AmN6LOs3cfOjsKA9sDtBzj9OQceH9RfnqnBfS40H7akVbdMnus=',
    '_rdt_uuid': '1772742667212.9e2331c2-136d-4cf8-803d-455eb8bcb12e',
    '_scid_r': '_pC76Is7S4C9vbZVQWMZ3-sld2xHK_qKDFsmHw',
    '_uetsid': '3e7c588018d211f19e0129d61a860c86',
    '_uetvid': '3e7cb07018d211f1b8e36bfcd3d010a1',
    '_derived_epik': 'dj0yJnU9SnBSZmxCTGtIYV85NjA4cTBfekJHMmFzbENxRjJJYkwmbj1EVGRkU2JQMUFQaWtyNkJfUzIxaFJ3Jm09NyZ0PUFBQUFBR21xS3c4JnJtPWYmcnQ9QUFBQUFHZ2Jualkmc3A9Mg',
    '_clsk': 'vgyx48%5E1772759824319%5E3%5E0%5Ei.clarity.ms%2Fcollect',
    'ttcsid': '1772759224039::L5DcN3mVD4Sifx9wqGho.2.1772759999630.0',
    'ttcsid_CN5P33RC77UF9CBTPH9G': '1772759224037::ufCVmj-zs6Kw5NpuS8eC.2.1772759999630.1',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.zillow.com',
    'priority': 'u=1, i',
    'referer': 'https://www.zillow.com/profile/theresasimmonsbrown',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-caller-id': 'professional-profile-page',
    'x-z-enable-oauth-conversion': 'true',
    # 'cookie': 'zguid=24|%24ce180a45-468e-48b9-b2ee-b8aec64e8904; zgsession=1|ca46c121-1c15-45f3-9900-1de2ff16c594; _ga=GA1.2.204694719.1772742663; _gid=GA1.2.707283442.1772742663; zjs_anonymous_id=%22ce180a45-468e-48b9-b2ee-b8aec64e8904%22; zjs_user_id=null; zg_anonymous_id=%22d0733bc9-8e29-4a20-bf92-b1ce23afd729%22; zjs_user_id_type=%22encoded_zuid%22; _pxvid=3a8dc488-18d2-11f1-a67e-f2ef9b80a41d; pxcts=3a8dccfa-18d2-11f1-a67e-66eed7e27a83; _gcl_au=1.1.921206453.1772742666; datagrail_consent_id=7e84c9ce-057e-4c91-87ef-56e6d4914637.b0c71c78-349c-4016-940a-6f72266b55a9; datagrail_consent_id_s=7e84c9ce-057e-4c91-87ef-56e6d4914637.36657c5c-5729-4f85-a931-58d294324f40; _scid=5BC76Is7S4C9vbZVQWMZ3-sld2xHK_qK; DoubleClickSession=true; _ScCbts=%5B%22230%3Bchrome.2%3A2%3A5%22%5D; _pin_unauth=dWlkPU1XRTFaRFZoT1dZdE0yTXpaQzAwTldJd0xUZzVaV1l0WVRBeFpHTXdZMk16WkRNeg; _tt_enable_cookie=1; _ttp=01KJZV4X5QYVANT4YYPJBFEG2Y_.tt.1; _fbp=fb.1.1772742669836.461872833728307676; _sctr=1%7C1772694000000; _lr_geo_location_state=AZ; _lr_geo_location=US; g_state={"i_l":0,"i_ll":1772759221155,"i_b":"x4sgqkM3VznTgZEAHVfJj3WFwZantT/XhQgwzC1k1hI","i_e":{"enable_itp_optimization":16}}; tfpsi=e37356a2-283a-4b5f-b218-c5abe6eef138; _clck=477glm%5E2%5Eg44%5E0%5E2255; AWSALB=uuUUdsAfn5H9LBVpQ5iMNx9op+YFhT5SG9/12QfunOxEM75mEVRt1Zxyrs9fWb5qcG610H7S88S4457PHFt9yjw+TFHCBQ+ggKs9YHONYx7emuKPTknj3hpx71L4; AWSALBCORS=uuUUdsAfn5H9LBVpQ5iMNx9op+YFhT5SG9/12QfunOxEM75mEVRt1Zxyrs9fWb5qcG610H7S88S4457PHFt9yjw+TFHCBQ+ggKs9YHONYx7emuKPTknj3hpx71L4; JSESSIONID=0B8C227020607B620399DE5F5A0E1530; _px3=5f80727a6ce21f23945870f12fa4a9a90bd5f8b26fc42399a81e6742066eaa51:CDp+bAi5NsWYmzH0vayS834h3mmGWXR9tVGbUS/l+GkYoEpCwSLhguUPWs5MnmxqHiDhDLUxzuU8iOnacrMqHQ==:1000:fL3gZsuDejxpadJHwzYlhs+EWY/Xaif79/fwTgadgdwajHJd0wXsV7RJ8y+0441g9CXHCR5abs06pufTWV+2SqAhwwm6pSBNSPz2xzCN0P5Qq6KDtGBQ2hrWhypDKWsyjMD5ssK5a/+gNQTQvpHPZqvN9YN2cxBL2HSEhsBHpcTCsAcA15qaglqElN2CTvT/ssGL5dGy04gCUQtFar/MwQZ2/c4xJ5ovKvdzjcRpR4TCANpkvzS+HdLKGlM5/onoFDldKOXHC5Xl5SdencaA0IvFWpduZa5oC6TaA+y2fQ7pvUi5o6cpbC3t8HKDiqTGIkUHeoegmV8cewPbH7YbWsdChoMSCRudjMpRiiCJ09pKdQD1jH/nDCisxpkGDBCZpU7ofIj54iyS3jrjVtMeNOz0NaAdRcummjy1zlv5xea+dp5Zu75PtC9o0AmN6LOs3cfOjsKA9sDtBzj9OQceH9RfnqnBfS40H7akVbdMnus=; _rdt_uuid=1772742667212.9e2331c2-136d-4cf8-803d-455eb8bcb12e; _scid_r=_pC76Is7S4C9vbZVQWMZ3-sld2xHK_qKDFsmHw; _uetsid=3e7c588018d211f19e0129d61a860c86; _uetvid=3e7cb07018d211f1b8e36bfcd3d010a1; _derived_epik=dj0yJnU9SnBSZmxCTGtIYV85NjA4cTBfekJHMmFzbENxRjJJYkwmbj1EVGRkU2JQMUFQaWtyNkJfUzIxaFJ3Jm09NyZ0PUFBQUFBR21xS3c4JnJtPWYmcnQ9QUFBQUFHZ2Jualkmc3A9Mg; _clsk=vgyx48%5E1772759824319%5E3%5E0%5Ei.clarity.ms%2Fcollect; ttcsid=1772759224039::L5DcN3mVD4Sifx9wqGho.2.1772759999630.0; ttcsid_CN5P33RC77UF9CBTPH9G=1772759224037::ufCVmj-zs6Kw5NpuS8eC.2.1772759999630.1',
}

json_data = {
    'operationName': 'Reviews',
    'variables': {
        'input': {
            'encodedZuid': 'X1-ZU13pnwe6o177yh_5dugv',
            'pageNumber': 2,
            'pageSize': 10,
            'serviceProvidedTypeIds': [],
            'sortOrder': 2,
            'sortType': 2,
        },
    },
    'query': 'query Reviews($input: ProfessionalProfileDisplayReviewsByEncodedZuidInput!) {\n  professionalProfileDisplayReviewsByEncodedZuid(input: $input) {\n    reviews {\n      ...ReviewFields\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ReviewFields on ProfessionalProfileDisplayReview {\n  reviewId\n  ariaLabel\n  isActionable\n  moderationUrl\n  reviewMetadataTexts\n  shareFacebookText\n  shareFacebookUrl\n  shareXText\n  shareXUrl\n  subRatings {\n    ariaLabel\n    label\n    value\n    __typename\n  }\n  transactionSummary\n  rating\n  ratingAriaLabel\n  ratingText\n  reportAProblemText\n  response {\n    authorDisplayName\n    authorProfileImageUrl\n    authorProfileUrl\n    comment\n    date\n    __typename\n  }\n  reviewComment\n  reviewForLabel\n  reviewForUrl\n  reviewForValue\n  __typename\n}',
}



def WriteToFile():
    response = requests.post('https://www.zillow.com/graphql', cookies=cookies, headers=headers, json=json_data)
    with open("reviews.json","w") as f:
        json.dump(response.json(), f, indent=4)
WriteToFile()
