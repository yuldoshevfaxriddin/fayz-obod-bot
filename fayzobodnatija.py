import requests

URL_VOTE_RESULTS_XORAZM = "https://openbudget.uz/api/v2/info/board/52?regionId=12&size=10&stage=PASSED&quality="
URL_VOTE_RESULTS_XORAZM_BOGOT = "https://openbudget.uz/api/v2/info/board/52?regionId=12&districtId=162&size=10&stage=PASSED&quality="

FAYZ_OBOD_ID = "052397474012"
MESSAGE_LENGTH = 50
def get_result(URL_MAIN:str)->str:
    FAYZ_OBOD_STATE = False
    response = requests.get(URL_MAIN)
    results = []
    message = ""
    if response.status_code == 200:
        data = response.json()
        totalPages = data["totalPages"]
        totalElements = data["totalElements"]
        counter = 0
        for page in range(totalPages):
            if FAYZ_OBOD_STATE:
                return message
            url = URL_MAIN + f"&page={page}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                content = data["content"]
                for item in content:
                    counter += 1
                    item['description'] = item['categoryName'] if item['description'] == "" else item['description']
                    if page == 0:
                        if item["publicId"] == FAYZ_OBOD_ID :
                            message += f"👉 <i><b>{counter}. {item['districtName']} ovozlar soni: {item['voteCount']}\n {item['description'][:MESSAGE_LENGTH]}\n</b></i>"
                            FAYZ_OBOD_STATE = True
                        else:
                            message += f"{counter}. {item['districtName']} ovozlar soni: {item['voteCount']}\n {item['description'][:MESSAGE_LENGTH]}\n"

                    else:
                        if item["publicId"] == FAYZ_OBOD_ID :
                            message += f"👉 <i><b>{counter}. {item['districtName']} ovozlar soni: {item['voteCount']}\n {item['description'][:MESSAGE_LENGTH]}\n</b></i>"
                            return message
            else:
                print(f"Error fetching page {page}: {response.status_code}")
if __name__ == '__main__':
    print(get_result(URL_VOTE_RESULTS_XORAZM))