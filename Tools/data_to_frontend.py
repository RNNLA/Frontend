import pandas as pd
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from datetime import datetime, timedelta, date
from collections import Counter
from itertools import chain
import argparse

# input : dataframe, path
# ouput : csv

"""
type VerificationNewsDataModel = {
    id: number;
    title: string;
    link: string;
    is_checked: boolean;
    is_semicon: boolean;
    is_not_risk: boolean;
    is_semicon_by_human: boolean;
    is_not_risk_by_human: boolean;
    timestamp: string;
}
"""

yesterday = date.today() - timedelta(days=1)

def verfication_csv(data : pd.DataFrame,
              target_columns : list) :
    def _add_boolean(data : pd.DataFrame) :
        data['is_checked'] = False
        data['is_semicon_by_human'] = False
        data['is_risk_by_human'] = False
        data['is_not_risk'] = data['is_not_risk'].fillna(False)
        return data

    verification_data = data[target_columns]
    verification_data = verification_data.copy()
    verification_data.sort_values(by='timestamp', ascending=False, inplace=True)
    verification_data['isSemicon'] = verification_data['isSemicon'].apply(lambda x : False if x == 1 else True)
    verification_data['isRisk'] = verification_data['isRisk'].apply(lambda x : True if x == 1 else False)
    verification_data.rename(columns={"url":"link", "isRisk":"is_not_risk", "isSemicon":"is_not_semicon"}, inplace=True)
    verification_data = _add_boolean(verification_data)
    verification_data.reset_index(drop=True, inplace=True)
    verification_data.reset_index(inplace=True)
    verification_data.rename(columns={"index":"id"}, inplace=True)
    return verification_data

"""
type GraphDataModel = {
    date: string;
    positive_count: number;
    negative_count: number;
}
"""
def tendency_csv(data : pd.DataFrame,
                 data_directory : str,
                 target_columns : list,
                 date : str,
                 date_count : int = 20,
                 ) :
    def _count(data : pd.DataFrame,
               using_columns : list) :
        processed_data = data.groupby(using_columns).count().reset_index().sort_values(by=using_columns, ascending=True)
        return processed_data

    tendency_data = data[target_columns]
    tendency_data = tendency_data.loc[(tendency_data.isRisk==0) | (tendency_data.isRisk==1)]
    tendency_data = tendency_data.copy()
    using_columns = ['time', 'isRisk']
    final_df = _count(tendency_data, using_columns)

    for i in range(2, date_count):
        try :
            date_calculated = datetime.strptime(date, "%Y-%m-%d") - timedelta(days=i)
            date_str = date_calculated.strftime("%Y-%m-%d")
            df = pd.read_csv(data_directory + date_str + "_front.csv")
            df['time'] = df['timestamp'].str.slice(0,11)
            df = df[target_columns]
            df = _count(df, using_columns)
            final_df = pd.concat([df, final_df])
        except FileNotFoundError :
            print(f"You don't have enought files. You've got {i-2} files.")
            break
    final_df.rename(columns={"isRisk":"is_not_risk", "content":"count"}, inplace=True)
    final_df = final_df.copy()
    final_df['is_not_risk'] = final_df['is_not_risk'].apply(lambda x : True if x == 1.0 else False)

    risk_df = final_df.loc[final_df.is_not_risk == False].drop(columns=['is_not_risk']).rename(columns={"count":"negative_count"})
    final_df = final_df.loc[final_df.is_not_risk == True].drop(columns=['is_not_risk']).rename(columns={"count":"positive_count"})

    final_df = pd.merge(risk_df, final_df, how="outer", on="time").fillna(0)
    
    return final_df

"""
type WordCloudDataModel = {
    rank: number;
    word: string;
    is_not_risk: boolean;
    count: number;
}
"""
def count_csv(data : pd.DataFrame) :
    def _count_per_dataframe(data : pd.DataFrame,
                             index : int) :
        df_to_list = list(data['content'].values)
        result = list(chain(*df_to_list))
        result = [x for x in result if x != '0']
        counter = Counter(result)
        counted_df = pd.DataFrame({'word' : list(counter.keys()), 'count' : list(counter.values()), 'isRisk' : index})
        return counted_df
    
    data0 = _count_per_dataframe(data.loc[data['isRisk'] == 0], 0)
    data1 = _count_per_dataframe(data.loc[data['isRisk'] == 1], 1)
    count_data = pd.concat([data0, data1])
    count_data.rename(columns={'isRisk': 'is_not_risk'}, inplace=True)
    count_data = count_data.copy()
    count_data['is_not_risk'] = count_data['is_not_risk'].apply(lambda x : True if x == 1 else False) #since we use is_not_risk in frontend, reverse it.
    count_data.sort_values(by="count", ascending=False, inplace=True)
    count_data.drop_duplicates(subset='word', keep='first', inplace=True) # remove duplicates if a word exists in both isrisk condition.
    count_data.reset_index(drop=True, inplace=True) # make index to 0~n
    count_data.reset_index(inplace=True) # make index to column
    count_data.rename(columns={"index" : "rank"}, inplace=True) # change index name to rank
    count_data['rank'] = count_data['rank'].apply(lambda x : x + 1)
    return count_data

def csv_to_json(data : pd.DataFrame,
                path : str,
                date : str,
                added_name : str):

    try :
        data.to_json(path_or_buf=path+date+added_name+".json", orient="records", force_ascii=False, indent=1)
    
    except FileNotFoundError as fe:
        print(f"A wrong file or directory is given. Please Check your path : {path}")

def wordcloud_to_img(data : pd.DataFrame,
                     path : str,
                     date : str,
                    added_name : str):
    cloud_data = data[['word', 'count']].iloc[:20].set_index('word').to_dict()['count']

    class SimpleGroupedColorFunc(object):
        def __init__(self, data):
            self.data = data

        def __call__(self, word, **kwargs):
            return "rgb(152,192,57)" if self.data[self.data['word']==word]['is_not_risk'].values[0] else "rgb(212,60,54)"
    
    color_func = SimpleGroupedColorFunc(data)
    wordCloud = WordCloud(font_path = './SpoqaHanSansNeo-Bold.ttf',
                          width=490, 
                          height=310, 
                          max_font_size=80,
                          background_color='white',
                          color_func=color_func
                          ).generate_from_frequencies(cloud_data)
    wordCloud.to_file(path+date+added_name+'.png')
    

def data_to_frontend(data_name : str,
                     source_path : str,
                     save_path : str) :
    date = datetime.strptime(data_name[:10], "%Y-%m-%d")
    save_date = date
    date = date.strftime("%Y-%m-%d")
    isNotToday = False
    isNotYesterday = False

    try:
        data = pd.read_csv(source_path + data_name)
        data['content'] = data['content'].apply(lambda x : x.replace("'", '"'))
        data['content'] = data['content'].apply(lambda x : json.loads(x))

        data['time'] = data['timestamp'].str.slice(0,11)
    except FileNotFoundError :
        isNotToday = True
        data = pd.DataFrame()
        print(f"Not such file, {source_path + data_name} in the path {source_path}. Maybe No File Today.")

    yesterday_date = save_date - timedelta(1)
    yesterday_date = yesterday_date.strftime("%Y-%m-%d") + "_" + data_name[11:]
    
    
    try:
        yesterday_path = source_path + yesterday_date
        yesterday_data = pd.read_csv(yesterday_path)
        yesterday_data['content'] = yesterday_data['content'].apply(lambda x : x.replace("'", '"'))
        yesterday_data['content'] = yesterday_data['content'].apply(lambda x : json.loads(x))

        
        yesterday_data['time'] = yesterday_data['timestamp'].str.slice(0,11)

        data = pd.concat([yesterday_data, data]).reset_index(drop=True) if data.empty else yesterday_data
        
    except FileNotFoundError :
        isNotYesterday = True
        print(f"Not such file, {yesterday_path} in the path {source_path}. Maybe No File Yesterday.")
    finally:
        if isNotToday and isNotYesterday :
            return
        verification_df = verfication_csv(data, ['title', 'url', 'isSemicon', 'isRisk', 'timestamp'])
        tendency_df = tendency_csv(data, source_path, ['time', 'isRisk', 'content'], date, 20)
        count_df = count_csv(data)

        csv_to_json(verification_df, save_path, date, "_VerificationNewsData")
        csv_to_json(tendency_df, save_path, date, "_GraphData")
        csv_to_json(count_df, save_path, date, "_WordCloudData")
        wordcloud_to_img(count_df, save_path, date, "_WordCloud")
    



if __name__ == '__main__' :
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', default=yesterday)
    args = parser.parse_args()

    yesterday = args.date

    source_path = './data/'
    save_path = './data/'
    
    # today = datetime.now()
    # today = today.strftime("%Y-%m-%d")
    # data_name = today + "_front.csv"
    data_name = f'{yesterday}_front.csv'
    data_to_frontend(data_name, source_path, save_path)
    



# count_csv(data, './count', 'content')
