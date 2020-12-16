# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 15:56:10 2020

@author: Admin
"""

#%%############################################################################
import pandas as pd
import datetime
import re
import numpy as np
import os
print(os.getcwd())
#%%############################################################################
df = pd.read_csv('data/저작물데이터.csv')

#%%############################################################################

변환_공표일자 = []
for _ in df['공표일자']:
   try:
       변환_공표일자.append(datetime.datetime.strptime(_, '%Y-%m-%d').date())
   except ValueError:
       변환_공표일자.append('')
   except TypeError:
       변환_공표일자.append('')
       
#%%############################################################################
def get_pure_nm(t):
    try:
        result = re.search(r'(.+)\b외 \d+ 명\b', t)
        answer = result.group(1).strip()
    except AttributeError:
        answer = t
    
    return answer

#%%############################################################################

순수_가수명 = []
for _ in df['가수명']:
    순수_가수명.append(get_pure_nm(_))
    
#%%############################################################################
df['변환_공표일자'] = 변환_공표일자
df['순수_가수명'] = 순수_가수명

#%%############################################################################
data = df.loc[:, ['순수_가수명', '저작물명', '작곡가', '작사가', '변환_공표일자']]

#%%############################################################################
# 이름 바꾸기
data['순수_가수명'] = data['순수_가수명'].replace('AILEE', '에일리')
data['순수_가수명'] = data['순수_가수명'].replace('LUCID FALL', '루시드폴')
data['순수_가수명'] = data['순수_가수명'].replace('IU', '아이유')
data['순수_가수명'] = data['순수_가수명'].replace('KAI(카이)', 'KAI')
data['순수_가수명'] = data['순수_가수명'].replace('YB(윤도현밴드)', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('YB', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('YB FEAT.RRM', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('YB 외10명', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('YB(윤도현밴드)', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('RUMBLE FISH(이원상,최진이,박천휘)', '럼블피쉬')
data['순수_가수명'] = data['순수_가수명'].replace('THE ONE(더원)', '더원')
data['순수_가수명'] = data['순수_가수명'].replace('윤도현밴드', '윤도현')
data['순수_가수명'] = data['순수_가수명'].replace('강균성(노을)', '강균성')
data['순수_가수명'] = data['순수_가수명'].replace('김범수 김다미', '김범수, 김다미')
data['순수_가수명'] = data['순수_가수명'].replace('신승훈외', '신승훈')
data['순수_가수명'] = data['순수_가수명'].replace('조규찬외', '조규찬')
data['순수_가수명'] = data['순수_가수명'].replace('환희(FLY TO THE SKY)', '환희')
data['순수_가수명'] = data['순수_가수명'].replace('NELL(넬)', 'NELL')
data['순수_가수명'] = data['순수_가수명'].replace('김윤아(자우림)', '김윤아')
data['순수_가수명'] = data['순수_가수명'].replace('김현철외', '김현철')
data['순수_가수명'] = data['순수_가수명'].replace('김흥국합창', '김흥국')
data['순수_가수명'] = data['순수_가수명'].replace('남인수(南仁樹)', '남인수')
data['순수_가수명'] = data['순수_가수명'].replace('더원(THE ONE)', '더원')
data['순수_가수명'] = data['순수_가수명'].replace('린 (LYN)', '린')
data['순수_가수명'] = data['순수_가수명'].replace('린(LYN)', '린')
data['순수_가수명'] = data['순수_가수명'].replace('바비킴(BOBBY KIM)', '바비킴')
data['순수_가수명'] = data['순수_가수명'].replace('비둘기씨스터즈', '비둘기시스터즈')
data['순수_가수명'] = data['순수_가수명'].replace('비비(BIBI)', 'BIBI')
data['순수_가수명'] = data['순수_가수명'].replace('비엔토(FEAT. 김수빈)', '비엔토')
data['순수_가수명'] = data['순수_가수명'].replace('성시경, 아이유', '성시경,아이유')
data['순수_가수명'] = data['순수_가수명'].replace('소녀시대(태연)', '태연')
data['순수_가수명'] = data['순수_가수명'].replace('소연(LABOUM)', '소연')
data['순수_가수명'] = data['순수_가수명'].replace('소연(라붐)', '소연')
data['순수_가수명'] = data['순수_가수명'].replace('솔지(EXID)', '솔지')
data['순수_가수명'] = data['순수_가수명'].replace('아이유(IU)', '아이유')
data['순수_가수명'] = data['순수_가수명'].replace('알리(ALI)', '알리')
data['순수_가수명'] = data['순수_가수명'].replace('왁스(WAX)', '왁스')
data['순수_가수명'] = data['순수_가수명'].replace('윤종신(FEAT.김범수)', '윤종신')
data['순수_가수명'] = data['순수_가수명'].replace('윤종신(WITH양파)', '윤종신')
data['순수_가수명'] = data['순수_가수명'].replace('이정선과해', '이정선')
data['순수_가수명'] = data['순수_가수명'].replace('임창정외15', '임창정')
data['순수_가수명'] = data['순수_가수명'].replace('임창정외15명', '임창정')
data['순수_가수명'] = data['순수_가수명'].replace('조관우(WITH 이세준 OF 유리상자)', '조관우')
data['순수_가수명'] = data['순수_가수명'].replace('패티김 외', '패티김')
data['순수_가수명'] = data['순수_가수명'].replace('패티김외8', '패티김')
data['순수_가수명'] = data['순수_가수명'].replace('폴킴(PAUL KIM)', '폴킴')
data['순수_가수명'] = data['순수_가수명'].replace('한영애(한영애3집1992년)', '한영애')
data['순수_가수명'] = data['순수_가수명'].replace('루나(LUNA0', '루나')
data['순수_가수명'] = data['순수_가수명'].replace('루나(에프엑스)', '루나')
data['순수_가수명'] = data['순수_가수명'].replace('이정선PROJECTBA', '이정선')
data['순수_가수명'] = data['순수_가수명'].replace('비둘기자매', '비둘기시스터즈')
data['순수_가수명'] = data['순수_가수명'].replace('우리동네음악대장', '하현우')
data['순수_가수명'] = data['순수_가수명'].replace('하늘에서비가내려와요우비소녀', '박진주')
data['순수_가수명'] = data['순수_가수명'].replace('동막골소녀', '솔지')
data['순수_가수명'] = data['순수_가수명'].replace('죠스가나타났다', '테이')
data['순수_가수명'] = data['순수_가수명'].replace('야생과함께세렝게티', '이성우')
data['순수_가수명'] = data['순수_가수명'].replace('10점만점에10점양궁소녀', '레이디제인')
data['순수_가수명'] = data['순수_가수명'].replace('4차원안드로메다', '모세')
data['순수_가수명'] = data['순수_가수명'].replace('굴러온복덩어리', '임정희')
data['순수_가수명'] = data['순수_가수명'].replace('내가가만히있으니까가마니로보이니(카이)', 'KAI')
data['순수_가수명'] = data['순수_가수명'].replace('니글니글버터플라이', '김필')
data['순수_가수명'] = data['순수_가수명'].replace('밤의제왕박쥐맨', '이현우')
data['순수_가수명'] = data['순수_가수명'].replace('사랑의불시착', '최재훈')
data['순수_가수명'] = data['순수_가수명'].replace('신명난다에헤라디오(정동하)', '정동하')
data['순수_가수명'] = data['순수_가수명'].replace('신선약초은행잎', '홍진영')
data['순수_가수명'] = data['순수_가수명'].replace('슬램덩크', '김태우')
data['순수_가수명'] = data['순수_가수명'].replace('심쿵주의눈꽃여왕', '다나')
data['순수_가수명'] = data['순수_가수명'].replace('아이러브커피', '유지')
data['순수_가수명'] = data['순수_가수명'].replace('어디서좀노셨군요', '송소희')
data['순수_가수명'] = data['순수_가수명'].replace('여전사캣츠걸', '차지연')
data['순수_가수명'] = data['순수_가수명'].replace('역도요정김복면', '김나영')
data['순수_가수명'] = data['순수_가수명'].replace('외줄타기인생왕의남자', '유승우')
data['순수_가수명'] = data['순수_가수명'].replace('읽어서남주나문학소녀(호란)', '호란')
data['순수_가수명'] = data['순수_가수명'].replace('주간아이돌', '성진우')
data['순수_가수명'] = data['순수_가수명'].replace('참외롭다', '허영생')
data['순수_가수명'] = data['순수_가수명'].replace('파리잡는파리넬리', 'KCM')
data['순수_가수명'] = data['순수_가수명'].replace('캡틴코리아', '박재정')
data['순수_가수명'] = data['순수_가수명'].replace('하면된다백수탈출', '더원')
data['순수_가수명'] = data['순수_가수명'].replace('감기조심하세요성냥팔이소녀', '하니')
data['순수_가수명'] = data['순수_가수명'].replace('노래덕후능력자', '김용준')
data['순수_가수명'] = data['순수_가수명'].replace('달려라지구촌', '김동명')
data['순수_가수명'] = data['순수_가수명'].replace('동막골소녀(솔지)', '솔지')
data['순수_가수명'] = data['순수_가수명'].replace('램프의요정', '김경호')
data['순수_가수명'] = data['순수_가수명'].replace('로맨틱흑기사', '로이킴')
data['순수_가수명'] = data['순수_가수명'].replace('별이빛나는밤', '자두')
data['순수_가수명'] = data['순수_가수명'].replace('보헤미안랩소디', '김연우')
data['순수_가수명'] = data['순수_가수명'].replace('불광동휘발유', '김연지')
data['순수_가수명'] = data['순수_가수명'].replace('이정선해바라기', '이정선')
data['순수_가수명'] = data['순수_가수명'].replace('이현석프로젝트', '이현석')
#%%############################################################################
# 날짜순으로 sorting
data.sort_values(by=['변환_공표일자', '저작물명', '순수_가수명'], inplace=True)

#%%############################################################################
# 본인곡 리메이크한 음원은 중복 제거
a = data[data.duplicated(['순수_가수명', '저작물명', '작곡가', '작사가'], keep=False)]  # 확인하기
data.drop_duplicates(['순수_가수명', '저작물명', '작곡가', '작사가'], keep='first', inplace=True)  # 첫 번째만 남기기(혹시모르니까)

#%%############################################################################
remake = data[data.duplicated(['저작물명', '작곡가', '작사가'], keep=False)]  # 리메이크곡들 뽑기
remake.sort_values(by=['저작물명','변환_공표일자', '순수_가수명'], inplace=True)

#%%############################################################################
# 리메이크곡들 뽑고 다시 본인곡 리메이크 삭제
a = remake[remake.duplicated(['순수_가수명', '저작물명', '작곡가', '작사가'], keep=False)]  # 본인이 본인 곡 리메이크
remake.drop_duplicates(['순수_가수명', '저작물명', '작곡가', '작사가'], inplace=True)

#%%############################################################################
unique_singers = pd.Series(remake['순수_가수명'].unique())
n_remake_singers = len(unique_singers)
remake_matrix = np.zeros((n_remake_singers, n_remake_singers))

#%%############################################################################
# 가수-가수 리메이크 Matrix 만들기

for _ in remake['저작물명'].unique():
    print(_)
    small_data = remake[remake['저작물명'] == _]
    original = small_data.iloc[0, 0]
    remake_singer = small_data.iloc[1:, 0]
    
    original_idx = unique_singers[unique_singers == original].index[0]
    print('original : {}'.format(original))
    for rs in remake_singer:
        remake_idx = unique_singers[unique_singers == rs].index[0]
        remake_matrix[remake_idx, original_idx] += 1
        print('리메이크한 가수 : {}'.format(rs))

#%%############################################################################

remake_df = pd.DataFrame(remake_matrix)
remake_df.index = unique_singers
remake_df.columns = unique_singers

#%%############################################################################
remake_df.to_csv('result.csv', encoding='utf-8-sig')

#%% 2-mode ####################################################################
# 가수-음원 2-mode Matrix 만들기

unique_songs = pd.Series(remake['저작물명'].unique())
n_remake_songs = len(unique_songs)
twomode_matrix = np.zeros((n_remake_singers, n_remake_songs))

for _ in range(len(remake)):
    line = remake.iloc[_, 0:2]
    singer = line['순수_가수명']
    song = line['저작물명']
    
    singer_idx = unique_singers[unique_singers == singer].index[0]
    song_idx = unique_songs[unique_songs == song].index[0]
    twomode_matrix[singer_idx][song_idx] += 1
    
    
#%%############################################################################
twomode_df = pd.DataFrame(twomode_matrix)
twomode_df.index = unique_singers
twomode_df.columns = unique_songs
#%%############################################################################
twomode_df.to_csv('result_2mode.csv', encoding='utf-8-sig')

#%%############################################################################
# 저작물명, 공표일자 Attribute 만들기

attribute = remake[['저작물명', '변환_공표일자']]
attribute.drop_duplicates(['저작물명'], keep='first', inplace=True)

date_att = []
for i, _ in enumerate(attribute['변환_공표일자']):
    print(i, _)
    try:
        if _ < datetime.datetime.strptime('1950-1-1', '%Y-%m-%d').date():
            date_att.append('1910')
        elif (_ >= datetime.datetime.strptime('1950-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('1960-1-1', '%Y-%m-%d').date()):
            date_att.append('1950')
        elif (_ >= datetime.datetime.strptime('1960-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('1970-1-1', '%Y-%m-%d').date()):
            date_att.append('1960')
        elif (_ >= datetime.datetime.strptime('1970-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('1980-1-1', '%Y-%m-%d').date()):
            date_att.append('1970')
        elif (_ >= datetime.datetime.strptime('1980-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('1990-1-1', '%Y-%m-%d').date()):
            date_att.append('1980')
        elif (_ >= datetime.datetime.strptime('1990-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('2000-1-1', '%Y-%m-%d').date()):
            date_att.append('1990')
        elif (_ >= datetime.datetime.strptime('2000-1-1', '%Y-%m-%d').date()) & (_ < datetime.datetime.strptime('2010-1-1', '%Y-%m-%d').date()):
            date_att.append('2000')
        elif _ >= datetime.datetime.strptime('2010-1-1', '%Y-%m-%d').date():
            date_att.append('2010')
    except TypeError:
        date_att.append('no data')
#%%############################################################################
attribute['시대구분'] = date_att
attribute = attribute[['저작물명', '시대구분']]

#%%############################################################################
attribute.to_csv('시대구분attribute.csv', encoding='utf-8-sig')



