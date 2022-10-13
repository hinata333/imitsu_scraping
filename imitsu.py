import streamlit as st
from bs4 import BeautifulSoup
import requests
import pandas as pd
from time import sleep
import base64

st.title('アイミツ　Webスクレイピング')

st.write(f'##### ・取得する都道府県を選択して下さい。')


###全国一括チェック作る
prefecture = []
st.write(f'###### < 全国 >')
zenkoku = st.checkbox('全国', value=False)

st.write(f'###### < 北海道・東北 >')
col1, col2, col3, col4, col5, col6, col7= st.columns(7)
st.write(f'###### < 関東 >')
col2_1, col2_2, col2_3, col2_4, col2_5, col2_6 = st.columns(6)
col2_1_2, col2_2_2, col2_3_2, col2_4_2, col2_5_2, col2_6_2 = st.columns(6)
st.write(f'###### < 北陸・甲信越 >')
col3_1, col3_2, col3_3, col3_4, col3_5, col3_6, col3_7= st.columns(7)
st.write(f'###### < 東海 >')
col4_1, col4_2, col4_3, col4_4, col4_5, col4_6, col4_7= st.columns(7)
st.write(f'###### < 近畿 >')
col5_1, col5_2, col5_3, col5_4, col5_5, col5_6= st.columns(6)
st.write(f'###### < 中国・四国 >')
col6_1, col6_2, col6_3, col6_4, col6_5, col6_6, col6_7 = st.columns(7)
col6_1_2, col6_2_2, col6_3_2, col6_4_2, col6_5_2, col6_6_2, col6_7_2 = st.columns(7)
st.write(f'###### < 九州・沖縄 >')
col7_1, col7_2, col7_3, col7_4, col7_5, col7_6 = st.columns(6)
col7_1_2, col7_2_2, col7_3_2, col7_4_2, col7_5_2, col7_6_2 = st.columns(6)
if zenkoku:
  with col1: pre_1 = st.checkbox('北海道', value=True)
  with col2: pre_2 = st.checkbox('青森県', value=True)
  with col3: pre_3 = st.checkbox('岩手県', value=True)
  with col4: pre_4 = st.checkbox('宮城県', value=True)
  with col5: pre_5 = st.checkbox('秋田県', value=True)
  with col6: pre_6 = st.checkbox('山形県', value=True)
  with col7: pre_7 = st.checkbox('福島県', value=True)
  if pre_1: prefecture.append('北海道')
  if pre_2: prefecture.append('青森県')
  if pre_3: prefecture.append('岩手県')
  if pre_4: prefecture.append('宮城県')
  if pre_5: prefecture.append('秋田県')
  if pre_6: prefecture.append('山形県')
  if pre_7: prefecture.append('福島県')
  with col2_1: pre2_1 = st.checkbox('茨城県', value=True)
  with col2_2: pre2_2 = st.checkbox('栃木県', value=True)
  with col2_3: pre2_3 = st.checkbox('群馬県', value=True)
  with col2_4: pre2_4 = st.checkbox('埼玉県', value=True)
  with col2_1_2: pre2_1_2 = st.checkbox('千葉県', value=True)
  with col2_2_2: pre2_2_2 = st.checkbox('東京都', value=True)
  with col2_3_2: pre2_3_2 = st.checkbox('神奈川県', value=True)
  if pre2_1: prefecture.append('茨城県')
  if pre2_2: prefecture.append('栃木県')
  if pre2_3: prefecture.append('群馬県')
  if pre2_4: prefecture.append('埼玉県')
  if pre2_1_2: prefecture.append('千葉県')
  if pre2_2_2: prefecture.append('東京都')
  if pre2_3_2: prefecture.append('神奈川県')
  with col3_1: pre3_1 = st.checkbox('新潟県', value=True)
  with col3_2: pre3_2 = st.checkbox('富山県', value=True)
  with col3_3: pre3_3 = st.checkbox('石川県', value=True)
  with col3_4: pre3_4 = st.checkbox('福井県', value=True)
  with col3_5: pre3_5 = st.checkbox('山梨県', value=True)
  with col3_6: pre3_6 = st.checkbox('長野県', value=True)
  if pre3_1: prefecture.append('新潟県')
  if pre3_2: prefecture.append('富山県')
  if pre3_3: prefecture.append('石川県')
  if pre3_4: prefecture.append('福井県')
  if pre3_5: prefecture.append('山梨県')
  if pre3_6: prefecture.append('長野県')
  with col4_1: pre4_1 = st.checkbox('静岡県', value=True)
  with col4_2: pre4_2 = st.checkbox('愛知県', value=True)
  with col4_3: pre4_3 = st.checkbox('三重県', value=True)
  with col4_4: pre4_4 = st.checkbox('岐阜県', value=True)
  if pre4_1: prefecture.append('静岡県')
  if pre4_2: prefecture.append('愛知県')
  if pre4_3: prefecture.append('三重県')
  if pre4_4: prefecture.append('岐阜県')
  with col5_1: pre5_1 = st.checkbox('滋賀県', value=True)
  with col5_2: pre5_2 = st.checkbox('京都府', value=True)
  with col5_3: pre5_3 = st.checkbox('大阪府', value=True)
  with col5_4: pre5_4 = st.checkbox('兵庫県', value=True)
  with col5_5: pre5_5 = st.checkbox('奈良県', value=True)
  with col5_6: pre5_6 = st.checkbox('和歌山県', value=True)
  if pre5_1: prefecture.append('滋賀県')
  if pre5_2: prefecture.append('京都府')
  if pre5_3: prefecture.append('大阪府')
  if pre5_4: prefecture.append('兵庫県')
  if pre5_5: prefecture.append('奈良県')
  if pre5_6: prefecture.append('和歌山県')
  with col6_1: pre6_1 = st.checkbox('鳥取県', value=True)
  with col6_2: pre6_2 = st.checkbox('島根県', value=True)
  with col6_3: pre6_3 = st.checkbox('岡山県', value=True)
  with col6_4: pre6_4 = st.checkbox('広島県', value=True)
  with col6_5: pre6_5 = st.checkbox('山口県', value=True)
  with col6_1_2: pre6_1_2 = st.checkbox('徳島県', value=True)
  with col6_2_2: pre6_2_2 = st.checkbox('香川県', value=True)
  with col6_3_2: pre6_3_2 = st.checkbox('愛媛県', value=True)
  with col6_4_2: pre6_4_2 = st.checkbox('高知県', value=True)
  if pre6_1: prefecture.append('鳥取県')
  if pre6_2: prefecture.append('島根県')
  if pre6_3: prefecture.append('岡山県')
  if pre6_4: prefecture.append('広島県')
  if pre6_5: prefecture.append('山口県')
  if pre6_1_2: prefecture.append('徳島県')
  if pre6_2_2: prefecture.append('香川県')
  if pre6_3_2: prefecture.append('愛媛県')
  if pre6_4_2: prefecture.append('高知県')
  with col7_1: pre7_1 = st.checkbox('福岡県', value=True)
  with col7_2: pre7_2 = st.checkbox('佐賀県', value=True)
  with col7_3: pre7_3 = st.checkbox('長崎県', value=True)
  with col7_4: pre7_4 = st.checkbox('熊本県', value=True)
  with col7_1_2: pre7_1_2 = st.checkbox('大分県', value=True)
  with col7_2_2: pre7_2_2 = st.checkbox('宮崎県', value=True)
  with col7_3_2: pre7_3_2 = st.checkbox('鹿児島県', value=True)
  with col7_4_2: pre7_4_2 = st.checkbox('沖縄県', value=True)
  if pre7_1: prefecture.append('福岡県')
  if pre7_2: prefecture.append('佐賀県')
  if pre7_3: prefecture.append('長崎県')
  if pre7_4: prefecture.append('熊本県')
  if pre7_1_2: prefecture.append('大分県')
  if pre7_2_2: prefecture.append('宮崎県')
  if pre7_3_2: prefecture.append('鹿児島県')
  if pre7_4_2: prefecture.append('沖縄県')
else:
  with col1: pre_1 = st.checkbox('北海道', value=False)
  with col2: pre_2 = st.checkbox('青森県', value=False)
  with col3: pre_3 = st.checkbox('岩手県', value=False)
  with col4: pre_4 = st.checkbox('宮城県', value=False)
  with col5: pre_5 = st.checkbox('秋田県', value=False)
  with col6: pre_6 = st.checkbox('山形県', value=False)
  with col7: pre_7 = st.checkbox('福島県', value=False)
  if pre_1: prefecture.append('北海道')
  if pre_2: prefecture.append('青森県')
  if pre_3: prefecture.append('岩手県')
  if pre_4: prefecture.append('宮城県')
  if pre_5: prefecture.append('秋田県')
  if pre_6: prefecture.append('山形県')
  if pre_7: prefecture.append('福島県')
  with col2_1: pre2_1 = st.checkbox('茨城県', value=False)
  with col2_2: pre2_2 = st.checkbox('栃木県', value=False)
  with col2_3: pre2_3 = st.checkbox('群馬県', value=False)
  with col2_4: pre2_4 = st.checkbox('埼玉県', value=False)
  with col2_1_2: pre2_1_2 = st.checkbox('千葉県', value=False)
  with col2_2_2: pre2_2_2 = st.checkbox('東京都', value=False)
  with col2_3_2: pre2_3_2 = st.checkbox('神奈川県', value=False)
  if pre2_1: prefecture.append('茨城県')
  if pre2_2: prefecture.append('栃木県')
  if pre2_3: prefecture.append('群馬県')
  if pre2_4: prefecture.append('埼玉県')
  if pre2_1_2: prefecture.append('千葉県')
  if pre2_2_2: prefecture.append('東京都')
  if pre2_3_2: prefecture.append('神奈川県')
  with col3_1: pre3_1 = st.checkbox('新潟県', value=False)
  with col3_2: pre3_2 = st.checkbox('富山県', value=False)
  with col3_3: pre3_3 = st.checkbox('石川県', value=False)
  with col3_4: pre3_4 = st.checkbox('福井県', value=False)
  with col3_5: pre3_5 = st.checkbox('山梨県', value=False)
  with col3_6: pre3_6 = st.checkbox('長野県', value=False)
  if pre3_1: prefecture.append('新潟県')
  if pre3_2: prefecture.append('富山県')
  if pre3_3: prefecture.append('石川県')
  if pre3_4: prefecture.append('福井県')
  if pre3_5: prefecture.append('山梨県')
  if pre3_6: prefecture.append('長野県')
  with col4_1: pre4_1 = st.checkbox('静岡県', value=False)
  with col4_2: pre4_2 = st.checkbox('愛知県', value=False)
  with col4_3: pre4_3 = st.checkbox('三重県', value=False)
  with col4_4: pre4_4 = st.checkbox('岐阜県', value=False)
  if pre4_1: prefecture.append('静岡県')
  if pre4_2: prefecture.append('愛知県')
  if pre4_3: prefecture.append('三重県')
  if pre4_4: prefecture.append('岐阜県')
  with col5_1: pre5_1 = st.checkbox('滋賀県', value=False)
  with col5_2: pre5_2 = st.checkbox('京都府', value=False)
  with col5_3: pre5_3 = st.checkbox('大阪府', value=False)
  with col5_4: pre5_4 = st.checkbox('兵庫県', value=False)
  with col5_5: pre5_5 = st.checkbox('奈良県', value=False)
  with col5_6: pre5_6 = st.checkbox('和歌山県', value=False)
  if pre5_1: prefecture.append('滋賀県')
  if pre5_2: prefecture.append('京都府')
  if pre5_3: prefecture.append('大阪府')
  if pre5_4: prefecture.append('兵庫県')
  if pre5_5: prefecture.append('奈良県')
  if pre5_6: prefecture.append('和歌山県')
  with col6_1: pre6_1 = st.checkbox('鳥取県', value=False)
  with col6_2: pre6_2 = st.checkbox('島根県', value=False)
  with col6_3: pre6_3 = st.checkbox('岡山県', value=False)
  with col6_4: pre6_4 = st.checkbox('広島県', value=False)
  with col6_5: pre6_5 = st.checkbox('山口県', value=False)
  with col6_1_2: pre6_1_2 = st.checkbox('徳島県', value=False)
  with col6_2_2: pre6_2_2 = st.checkbox('香川県', value=False)
  with col6_3_2: pre6_3_2 = st.checkbox('愛媛県', value=False)
  with col6_4_2: pre6_4_2 = st.checkbox('高知県', value=False)
  if pre6_1: prefecture.append('鳥取県')
  if pre6_2: prefecture.append('島根県')
  if pre6_3: prefecture.append('岡山県')
  if pre6_4: prefecture.append('広島県')
  if pre6_5: prefecture.append('山口県')
  if pre6_1_2: prefecture.append('徳島県')
  if pre6_2_2: prefecture.append('香川県')
  if pre6_3_2: prefecture.append('愛媛県')
  if pre6_4_2: prefecture.append('高知県')
  with col7_1: pre7_1 = st.checkbox('福岡県', value=False)
  with col7_2: pre7_2 = st.checkbox('佐賀県', value=False)
  with col7_3: pre7_3 = st.checkbox('長崎県', value=False)
  with col7_4: pre7_4 = st.checkbox('熊本県', value=False)
  with col7_1_2: pre7_1_2 = st.checkbox('大分県', value=False)
  with col7_2_2: pre7_2_2 = st.checkbox('宮崎県', value=False)
  with col7_3_2: pre7_3_2 = st.checkbox('鹿児島県', value=False)
  with col7_4_2: pre7_4_2 = st.checkbox('沖縄県', value=False)
  if pre7_1: prefecture.append('福岡県')
  if pre7_2: prefecture.append('佐賀県')
  if pre7_3: prefecture.append('長崎県')
  if pre7_4: prefecture.append('熊本県')
  if pre7_1_2: prefecture.append('大分県')
  if pre7_2_2: prefecture.append('宮崎県')
  if pre7_3_2: prefecture.append('鹿児島県')
  if pre7_4_2: prefecture.append('沖縄県')



st.write('選択中:', prefecture)
  

cates = []
ori_cte = [None]*101
ori_cte_index = [None]*101
# url = 'https://imitsu.jp/'
# while True:
#   try:
#     sleep(2)
#     r = requests.get(url, timeout=3)
#     r.raise_for_status()
#   except Exception as e:
#     print('-----ERROR(リトライ中)-----')
#   else:
#     break
# soup = BeautifulSoup(r.content, 'lxml')
# ori_cte_elem = soup.select('div.category-main a.ga_event')
ori_cte_elem = ['ホームページ制作', 'システム開発', 'アプリ開発', 'ECサイト構築', 'ITインフラ構築', '情報システム代行', 'データセンター', '動画制作・映像制作', 'イベント企画', 'PR','マス広告', '音楽制作', '商品撮影', '店舗コンサルティング', '交通広告', '編集プロダクション', '店舗販促・サンプリング', '資料作成', 'リスティング広告', 'SEO対策','マーケティングリサーチ', 'Web広告', '営業代行', 'DM発送', 'コールセンター', 'ノベルティ制作', '印刷', 'カーリース', '物流倉庫', '看板製作','OA機器', '福利厚生代行', '法人向けパソコン', '社員旅行', 'ビジネスフォン', '什器', 'コピー機', 'オンライン秘書', 'データ入力・集計', '産業廃棄物処理','社員研修', '人材紹介', '人材派遣', '求人広告', '採用コンサルティング・採用代行', 'オフィス清掃', 'オフィス警備', '店舗デザイン', 'オフィスデザイン', '電気工事','デザイン制作', '解体工事', '電気通信工事', '税理士', '資金調達', '社会保険労務士', 'M&A仲介', '行政書士', '助成金', 'コンサルティング', '司法書士', '風評被害対策', '通訳','翻訳']
# print(len(ori_cte_elem))
for c, cte in enumerate(ori_cte_elem):
  ori_cte[c] = str(c) + '_' + cte

st.write('カテゴリー数:', len(ori_cte_elem))
st.write(' ')
# all_cate = st.checkbox('一括チェック', value=False)
st.write('・取得するカテゴリーを選択して下さい。')
col_0, col_1, col_2, col_3 = st.columns(4)
col_0_2, col_1_2, col_2_2, col_3_2 = st.columns(4)
col_0_3, col_1_3, col_2_3, col_3_3 = st.columns(4)
col_0_4, col_1_4, col_2_4, col_3_4 = st.columns(4)
col_0_5, col_1_5, col_2_5, col_3_5 = st.columns(4)
col_0_6, col_1_6, col_2_6, col_3_6 = st.columns(4)
col_0_7, col_1_7, col_2_7, col_3_7 = st.columns(4)
col_0_8, col_1_8, col_2_8, col_3_8 = st.columns(4)
col_0_9, col_1_9, col_2_9, col_3_9 = st.columns(4)
col_0_10, col_1_10, col_2_10, col_3_10 = st.columns(4)
colu_0, colu_1, colu_2, colu_3 = st.columns(4)
colu_0_2, colu_1_2, colu_2_2, colu_3_2 = st.columns(4)
colu_0_3, colu_1_3, colu_2_3, colu_3_3 = st.columns(4)
colu_0_4, colu_1_4, colu_2_4, colu_3_4 = st.columns(4)
colu_0_5, colu_1_5, colu_2_5, colu_3_5 = st.columns(4)
colu_0_6, colu_1_6, colu_2_6, colu_3_6 = st.columns(4)

with col_0: elem_0 = st.checkbox(f'{ori_cte[0]}', value=False)
with col_1: elem_1 = st.checkbox(f'{ori_cte[1]}', value=False)
with col_2: elem_2 = st.checkbox(f'{ori_cte[2]}', value=False)
with col_3: elem_3 = st.checkbox(f'{ori_cte[3]}', value=False)
with col_0_2: elem_4 = st.checkbox(f'{ori_cte[4]}', value=False)
with col_1_2: elem_5 = st.checkbox(f'{ori_cte[5]}', value=False)
with col_2_2: elem_6 = st.checkbox(f'{ori_cte[6]}', value=False)
with col_3_2: elem_7 = st.checkbox(f'{ori_cte[7]}', value=False)
with col_0_3: elem_8 = st.checkbox(f'{ori_cte[8]}', value=False)
with col_1_3: elem_9 = st.checkbox(f'{ori_cte[9]}', value=False)
with col_2_3: elem_10 = st.checkbox(f'{ori_cte[10]}', value=False)
with col_3_3: elem_11 = st.checkbox(f'{ori_cte[11]}', value=False)
with col_0_4: elem_12 = st.checkbox(f'{ori_cte[12]}', value=False)
with col_1_4: elem_13 = st.checkbox(f'{ori_cte[13]}', value=False)
with col_2_4: elem_14 = st.checkbox(f'{ori_cte[14]}', value=False)
with col_3_4: elem_15 = st.checkbox(f'{ori_cte[15]}', value=False)
with col_0_5: elem_16 = st.checkbox(f'{ori_cte[16]}', value=False)
with col_1_5: elem_17 = st.checkbox(f'{ori_cte[17]}', value=False)
with col_2_5: elem_18 = st.checkbox(f'{ori_cte[18]}', value=False)
with col_3_5: elem_19 = st.checkbox(f'{ori_cte[19]}', value=False)
with col_0_6: elem_20 = st.checkbox(f'{ori_cte[20]}', value=False)
with col_1_6: elem_21 = st.checkbox(f'{ori_cte[21]}', value=False)
with col_2_6: elem_22 = st.checkbox(f'{ori_cte[22]}', value=False)
with col_3_6: elem_23 = st.checkbox(f'{ori_cte[23]}', value=False)
with col_0_7: elem_24 = st.checkbox(f'{ori_cte[24]}', value=False)
with col_1_7: elem_25 = st.checkbox(f'{ori_cte[25]}', value=False)
with col_2_7: elem_26 = st.checkbox(f'{ori_cte[26]}', value=False)
with col_3_7: elem_27 = st.checkbox(f'{ori_cte[27]}', value=False)
with col_0_8: elem_28 = st.checkbox(f'{ori_cte[28]}', value=False)
with col_1_8: elem_29 = st.checkbox(f'{ori_cte[29]}', value=False)
with col_2_8: elem_30 = st.checkbox(f'{ori_cte[30]}', value=False)
with col_3_8: elem_31 = st.checkbox(f'{ori_cte[31]}', value=False)
with col_0_9: elem_32 = st.checkbox(f'{ori_cte[32]}', value=False)
with col_1_9: elem_33 = st.checkbox(f'{ori_cte[33]}', value=False)
with col_2_9: elem_34 = st.checkbox(f'{ori_cte[34]}', value=False)
with col_3_9: elem_35 = st.checkbox(f'{ori_cte[35]}', value=False)
with col_0_10: elem_36 = st.checkbox(f'{ori_cte[36]}', value=False)
with col_1_10: elem_37 = st.checkbox(f'{ori_cte[37]}', value=False)
with col_2_10: elem_38 = st.checkbox(f'{ori_cte[38]}', value=False)
with col_3_10: elem_39 = st.checkbox(f'{ori_cte[39]}', value=False)
with colu_0: elem_40 = st.checkbox(f'{ori_cte[40]}', value=False)
with colu_1: elem_41 = st.checkbox(f'{ori_cte[41]}', value=False)
with colu_2: elem_42 = st.checkbox(f'{ori_cte[42]}', value=False)
with colu_3: elem_43 = st.checkbox(f'{ori_cte[43]}', value=False)
with colu_0_2: elem_44 = st.checkbox(f'{ori_cte[44]}', value=False)
with colu_1_2: elem_45 = st.checkbox(f'{ori_cte[45]}', value=False)
with colu_2_2: elem_46 = st.checkbox(f'{ori_cte[46]}', value=False)
with colu_3_2: elem_47 = st.checkbox(f'{ori_cte[47]}', value=False)
with colu_0_3: elem_48 = st.checkbox(f'{ori_cte[48]}', value=False)
with colu_1_3: elem_49 = st.checkbox(f'{ori_cte[49]}', value=False)
with colu_2_3: elem_50 = st.checkbox(f'{ori_cte[50]}', value=False)
with colu_3_3: elem_51 = st.checkbox(f'{ori_cte[51]}', value=False)
with colu_0_4: elem_52 = st.checkbox(f'{ori_cte[52]}', value=False)
with colu_1_4: elem_53 = st.checkbox(f'{ori_cte[53]}', value=False)
with colu_2_4: elem_54 = st.checkbox(f'{ori_cte[54]}', value=False)
with colu_3_4: elem_55 = st.checkbox(f'{ori_cte[55]}', value=False)
with colu_0_5: elem_56 = st.checkbox(f'{ori_cte[56]}', value=False)
with colu_1_5: elem_57 = st.checkbox(f'{ori_cte[57]}', value=False)
with colu_2_5: elem_58 = st.checkbox(f'{ori_cte[58]}', value=False)
with colu_3_5: elem_59 = st.checkbox(f'{ori_cte[59]}', value=False)
with colu_0_6: elem_60 = st.checkbox(f'{ori_cte[60]}', value=False)
with colu_1_6: elem_61 = st.checkbox(f'{ori_cte[61]}', value=False)
with colu_2_6: elem_62 = st.checkbox(f'{ori_cte[62]}', value=False)
with colu_3_6: elem_63 = st.checkbox(f'{ori_cte[63]}', value=False)

if elem_0: cates.append(f'{ori_cte[0]}')
if elem_1: cates.append(f'{ori_cte[1]}')
if elem_2: cates.append(f'{ori_cte[2]}')
if elem_3: cates.append(f'{ori_cte[3]}')
if elem_4: cates.append(f'{ori_cte[4]}')
if elem_5: cates.append(f'{ori_cte[5]}')
if elem_6: cates.append(f'{ori_cte[6]}')
if elem_7: cates.append(f'{ori_cte[7]}')
if elem_8: cates.append(f'{ori_cte[8]}')
if elem_9: cates.append(f'{ori_cte[9]}')
if elem_10: cates.append(f'{ori_cte[10]}')
if elem_11: cates.append(f'{ori_cte[11]}')
if elem_12: cates.append(f'{ori_cte[12]}')
if elem_13: cates.append(f'{ori_cte[13]}')
if elem_14: cates.append(f'{ori_cte[14]}')
if elem_15: cates.append(f'{ori_cte[15]}')
if elem_16: cates.append(f'{ori_cte[16]}')
if elem_17: cates.append(f'{ori_cte[17]}')
if elem_18: cates.append(f'{ori_cte[18]}')
if elem_19: cates.append(f'{ori_cte[19]}')
if elem_20: cates.append(f'{ori_cte[20]}')
if elem_21: cates.append(f'{ori_cte[21]}')
if elem_22: cates.append(f'{ori_cte[22]}')
if elem_23: cates.append(f'{ori_cte[23]}')
if elem_24: cates.append(f'{ori_cte[24]}')
if elem_25: cates.append(f'{ori_cte[25]}')
if elem_26: cates.append(f'{ori_cte[26]}')
if elem_27: cates.append(f'{ori_cte[27]}')
if elem_28: cates.append(f'{ori_cte[28]}')
if elem_29: cates.append(f'{ori_cte[29]}')
if elem_30: cates.append(f'{ori_cte[30]}')
if elem_31: cates.append(f'{ori_cte[31]}')
if elem_32: cates.append(f'{ori_cte[32]}')
if elem_33: cates.append(f'{ori_cte[33]}')
if elem_34: cates.append(f'{ori_cte[34]}')
if elem_35: cates.append(f'{ori_cte[35]}')
if elem_36: cates.append(f'{ori_cte[36]}')
if elem_37: cates.append(f'{ori_cte[37]}')
if elem_38: cates.append(f'{ori_cte[38]}')
if elem_39: cates.append(f'{ori_cte[39]}')
if elem_40: cates.append(f'{ori_cte[40]}')
if elem_41: cates.append(f'{ori_cte[41]}')
if elem_42: cates.append(f'{ori_cte[42]}')
if elem_43: cates.append(f'{ori_cte[43]}')
if elem_44: cates.append(f'{ori_cte[44]}')
if elem_45: cates.append(f'{ori_cte[45]}')
if elem_46: cates.append(f'{ori_cte[46]}')
if elem_47: cates.append(f'{ori_cte[47]}')
if elem_48: cates.append(f'{ori_cte[48]}')
if elem_49: cates.append(f'{ori_cte[49]}')
if elem_50: cates.append(f'{ori_cte[50]}')
if elem_51: cates.append(f'{ori_cte[51]}')
if elem_52: cates.append(f'{ori_cte[52]}')
if elem_53: cates.append(f'{ori_cte[53]}')
if elem_54: cates.append(f'{ori_cte[54]}')
if elem_55: cates.append(f'{ori_cte[55]}')
if elem_56: cates.append(f'{ori_cte[56]}')
if elem_57: cates.append(f'{ori_cte[57]}')
if elem_58: cates.append(f'{ori_cte[58]}')
if elem_59: cates.append(f'{ori_cte[59]}')
if elem_60: cates.append(f'{ori_cte[60]}')
if elem_61: cates.append(f'{ori_cte[61]}')
if elem_62: cates.append(f'{ori_cte[62]}')
if elem_63: cates.append(f'{ori_cte[63]}')


st.write('選択中:', cates)

# last_number = st.number_input('取得カテゴリー数を入力してください。', 1, 100, 1)
button = st.button('Start')
latest_interation = st.empty()
bar = st.progress(0)

pre_all = []
tohoku = []
kantou = []
hokuriku = []
tokai = []
kinki = []
tyugoku = []
kyusyu = []
def main(c_number, select_pre):
  if select_pre == '北海道': select_pre = 'hokkaido'
  elif select_pre == '青森県': select_pre = 'aomori'
  elif select_pre == '岩手県': select_pre = 'iwate'
  elif select_pre == '宮城県': select_pre = 'miyagi'
  elif select_pre == '秋田県': select_pre = 'akita'
  elif select_pre == '山形県': select_pre = 'yamagata'
  elif select_pre == '福島県': select_pre = 'fukushima'
  elif select_pre == '茨城県': select_pre = 'ibaraki'
  elif select_pre == '栃木県': select_pre = 'tochigi'
  elif select_pre == '群馬県': select_pre = 'gumma'
  elif select_pre == '埼玉県': select_pre = 'saitama'
  elif select_pre == '千葉県': select_pre = 'chiba'
  elif select_pre == '東京都': select_pre = 'tokyo'
  elif select_pre == '神奈川県': select_pre = 'kanagawa'
  elif select_pre == '新潟県': select_pre = 'niigata'
  elif select_pre == '富山県': select_pre = 'toyama'
  elif select_pre == '石川県': select_pre = 'ishikawa'
  elif select_pre == '福井県': select_pre = 'fukui'
  elif select_pre == '山梨県': select_pre = 'yamanashi'
  elif select_pre == '長野県': select_pre = 'nagano'
  elif select_pre == '岐阜県': select_pre = 'gifu'
  elif select_pre == '静岡県': select_pre = 'shizuoka'
  elif select_pre == '愛知県': select_pre = 'aichi'
  elif select_pre == '三重県': select_pre = 'mie'
  elif select_pre == '滋賀県': select_pre = 'shiga'
  elif select_pre == '京都府': select_pre = 'kyoto'
  elif select_pre == '大阪府': select_pre = 'osaka'
  elif select_pre == '兵庫県': select_pre = 'hyogo'
  elif select_pre == '奈良県': select_pre = 'nara'
  elif select_pre == '和歌山県': select_pre = 'wakayama'
  elif select_pre == '鳥取県': select_pre = 'tottori'
  elif select_pre == '島根県': select_pre = 'shimane'
  elif select_pre == '岡山県': select_pre = 'okayama'
  elif select_pre == '広島県': select_pre = 'hiroshima'
  elif select_pre == '山口県': select_pre = 'yamaguchi'
  elif select_pre == '徳島県': select_pre = 'tokushima'
  elif select_pre == '香川県': select_pre = 'kagawa'
  elif select_pre == '愛媛県': select_pre = 'ehime'
  elif select_pre == '高知県': select_pre = 'kochi'
  elif select_pre == '福岡県': select_pre = 'fukuoka'
  elif select_pre == '佐賀県': select_pre = 'saga'
  elif select_pre == '長崎県': select_pre = 'nagasaki'
  elif select_pre == '熊本県': select_pre = 'kumamoto'
  elif select_pre == '大分県': select_pre = 'oita'
  elif select_pre == '宮崎県': select_pre = 'miyazaki'
  elif select_pre == '鹿児島県': select_pre = 'kagoshima'
  elif select_pre == '沖縄県': select_pre = 'okinawa'

  url = 'https://imitsu.jp/'
  while True:
    try:
      sleep(2)
      r = requests.get(url, timeout=3)
      r.raise_for_status()
    except Exception as e:
      print('-----ERROR(リトライ中)-----')
    else:
      break
  soup = BeautifulSoup(r.content, 'lxml')
  jobs = soup.select('div.category-main a.ga_event')
  print(len(jobs))

  count = 0
  d_list = []
  for p, job in enumerate(jobs[:1]):
    job = jobs[c_number]
    print('*'*100)
    print(job.text)
    csv_name = f'{job.text}'
    page_url = job.get('href') + f'pr-{select_pre}/'
    print('*'*100)
    print(page_url)
    print('*'*100)
    retry = 0
    while retry < 5:
      try:
        sleep(2)
        page_r = requests.get(page_url, timeout=3)
        page_r.raise_for_status()
      except Exception as e:
        retry += 1
        print('-----ERROR(リトライ中)-----')
      else:
        break
    page_soup = BeautifulSoup(page_r.content, 'lxml')
    error_title = page_soup.select_one('h1.error_title')
    if error_title:
      print('404エラー')
      # detail = [None] * 5      
      d_list.append({
        '会社名': 'アクセスエラー',
        '設立年': 'アクセスエラー',
        '従業員数': 'アクセスエラー',
        '住所': 'アクセスエラー',
        '会社URL': 'アクセスエラー',
        'ソースURL': page_url,
      })
      df = pd.DataFrame(d_list)
    else:
      titel = page_soup.select_one('titel')
      if titel:
        print(titel.text)
      kensu = int(page_soup.select_one('div.service-count-hit').text.replace('件', '').replace(',', ''))
      print('件数:', kensu)
      n = int(kensu) // 20 + 1
      if int(kensu) % 20 == 0:
        n = int(kensu) // 20
      # n = 1 #####################################################################################################################
      for i in range(n):
        page_url = job.get('href') + f'pr-{select_pre}/' + f'?pn={i+1}#title'
        while True:
          try:
            sleep(1)
            page_r = requests.get(page_url, timeout=3)
            page_r.raise_for_status()
          except Exception as e:
            print('-----ERROR(リトライ中)-----')
          else:
            break
        page_soup = BeautifulSoup(page_r.content, 'lxml')
        companys = page_soup.select('h3.service-link')
        print('companys:', len(companys))

        for company in companys:
          count += 1
          print('='*10, f'{count}/{kensu}({i+1}/{n}ページ)', '='*10)
          bar.progress((count*100) // kensu)
          latest_interation.text(f'{count}/{kensu}({i+1}/{n}ページ)')
          company_name = '?'.join(company.text.split()).replace('?', '')
          print(company_name)
          detail_url = company.select_one('a').get('href')
          print(detail_url)
          retry = 0
          while retry < 10:
            try:
              sleep(1)
              detail_r = requests.get(detail_url, timeout=3)
              detail_r.raise_for_status()
            except Exception as e:
              retry += 1
              print('-----ERROR(リトライ中)-----')
            else:
              break
          detail_soup = BeautifulSoup(detail_r.content, 'lxml')
          div = detail_soup.select_one('section#company > div.service-information-content')
          dts = div.select('dl > dt')
          dds = div.select('dl > dd')
          detail = [None] * 5
          for k, dt in enumerate(dts):
            if '会社名' == dt.text: detail[0] = '?'.join(dds[k].text.split()).replace('?', '')
            elif '設立年' == dt.text: detail[1] = '?'.join(dds[k].text.split()).replace('?', '')
            elif '従業員数' == dt.text: detail[2] = '?'.join(dds[k].text.split()).replace('?', '')
            elif '住所' == dt.text: detail[3] = '?'.join(dds[k].text.split()).replace('?', '')
            elif '会社URL' == dt.text: detail[4] = '?'.join(dds[k].text.split()).replace('?', '')

          print('会社名:', detail[0])
          print('設立年:', detail[1])
          print('従業員数:', detail[2])
          print('住所:', detail[3])
          print('会社URL:', detail[4])

          d_list.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})

          df = pd.DataFrame(d_list)
          ##################################
          pre_all.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})

          if (select_pre == 'hokkaido') or (select_pre == 'aomori') or (select_pre == 'iwate') or (select_pre == 'miyagi') or (select_pre == 'akita') or (select_pre == 'yamagata') or (select_pre == 'fukushima'):
            tohoku.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'ibaraki') or (select_pre == 'tochigi') or (select_pre == 'gumma') or (select_pre == 'saitama') or (select_pre == 'chiba') or (select_pre == 'tokyo') or (select_pre == 'kanagawa'):
            kantou.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'niigata') or (select_pre == 'toyama') or (select_pre == 'ishikawa') or (select_pre == 'fukui') or (select_pre == 'yamanashi') or (select_pre == 'nagano'):
            hokuriku.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'gifu') or (select_pre == 'shizuoka') or (select_pre == 'aichi') or (select_pre == 'mie'):
            tokai.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'shiga') or (select_pre == 'kyoto') or (select_pre == 'osaka') or (select_pre == 'hyogo') or (select_pre == 'nara') or (select_pre == 'wakayama'):
            kinki.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'tottori') or (select_pre == 'shimane') or (select_pre == 'okayama') or (select_pre == 'hiroshima') or (select_pre == 'yamaguchi') or (select_pre == 'tokushima') or (select_pre == 'kagawa') or (select_pre == 'ehime') or (select_pre == 'kochi'):
            tyugoku.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
          elif (select_pre == 'fukuoka') or (select_pre == 'saga') or (select_pre == 'nagasaki') or (select_pre == 'kumamoto') or (select_pre == 'oita') or (select_pre == 'miyazaki') or (select_pre == 'kagoshima') or (select_pre == 'okinawa'):
            kyusyu.append({'会社名': detail[0],'設立年': detail[1],'従業員数': detail[2],'住所': detail[3],'会社URL': detail[4],'ソースURL': detail_url})
   
    return df

if button:
  csvs = []
  for i, cate_elem in enumerate(cates):
    c_number = int(str(cate_elem).split('_')[0])
    cate = str(cate_elem).split('_')[1]
    print('index:', int(c_number))
    print('cate:',cate)
    for k, select_pre in enumerate(prefecture):
      df = main(c_number, select_pre)
      st.write(f'### {cate} ({select_pre})結果 {k+i+1}/{len(cates)*len(prefecture)}', df)
      print(any(df))
      if any(df) == True:
        csv = df.to_csv(index=False, encoding='utf-8-sig')
        b64 = base64.b64encode(csv.encode('utf-8-sig')).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_{select_pre}.csv">Download</a>'
        st.markdown(f"{cate}_{select_pre}.csv: {href}", unsafe_allow_html=True)
  st.write(f'## --------------------------')
  #################################################
  df_pre_all = pd.DataFrame(pre_all)
  csv_pre_all = df_pre_all.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_pre_all.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_全国.csv">Download</a>'
  st.markdown(f"{cate}_全国.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_tohoku = pd.DataFrame(tohoku)
  csv_tohoku = df_tohoku.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_tohoku.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_北海道・東北.csv">Download</a>'
  st.markdown(f"{cate}_北海道・東北.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_kantou = pd.DataFrame(kantou)
  csv_kantou = df_kantou.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_kantou.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_関東.csv">Download</a>'
  st.markdown(f"{cate}_関東.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_hokuriku = pd.DataFrame(hokuriku)
  csv_hokuriku = df_hokuriku.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_hokuriku.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_北陸・甲信越.csv">Download</a>'
  st.markdown(f"{cate}_北陸・甲信越.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_tokai = pd.DataFrame(tokai)
  csv_tokai = df_tokai.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_tokai.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_東海.csv">Download</a>'
  st.markdown(f"{cate}_東海.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_kinki = pd.DataFrame(kinki)
  csv_kinki = df_kinki.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_kinki.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_近畿.csv">Download</a>'
  st.markdown(f"{cate}_近畿.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_tyugoku = pd.DataFrame(tyugoku)
  csv_tyugoku = df_tyugoku.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_tyugoku.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_中国・四国.csv">Download</a>'
  st.markdown(f"{cate}_中国・四国.csv: {href}", unsafe_allow_html=True)
  #################################################
  df_kyusyu = pd.DataFrame(kyusyu)
  csv_kyusyu = df_kyusyu.to_csv(index=False, encoding='utf-8-sig')
  b64 = base64.b64encode(csv_kyusyu.encode('utf-8-sig')).decode()
  href = f'<a href="data:application/octet-stream;base64,{b64}" download="{cate}_九州・沖縄.csv">Download</a>'
  st.markdown(f"{cate}_九州・沖縄.csv: {href}", unsafe_allow_html=True)
  st.write(f'## ---------Done----------')

