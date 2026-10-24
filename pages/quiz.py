import streamlit as st

st.set_page_config(page_title="モンゴルクイズ", page_icon="🎯")

st.title("🎯 モンゴルクイズ（全10問）")
st.write(
    "モンゴルにまつわるクイズです。全問正解を目指そう！"
)
st.markdown("---")

# スコア初期化
score = 0

# 第1問
st.subheader("第1問：モンゴルの首都の名前は？")
q1 = st.radio(
    "選択してください",
    ["アスタナ", "ウランバートル", "ビシュケク", "タシケント"],
    key="q1",
    index=None,
)
if q1 == "ウランバートル":
  st.success("正解！ 🎉")
  score += 1
elif q1 is not None:
  st.error("不正解… 正解はウランバートルです。")

st.markdown("---")

# 第2問
st.subheader("第2問：モンゴルの伝統的な移動式住居の名前は？")
q2 = st.radio(
    "選択してください", ["パオ", "ゲル", "ユルト", "ティピ"], key="q2", index=None
)
if q2 == "ゲル":
  st.success("正解！ 🎉")
  score += 1
elif q2 is not None:
  st.error("不正解… 正解は「ゲル」です。")

st.markdown("---")

# 第3問（画像クイズ）
st.subheader("第3問：現在のモンゴル国旗はどれでしょう？")

# use_column_width=True に修正（または引数なしでもOKです）
st.image("kokki.png", use_column_width=True)

q3 = st.radio(
    "1〜4の中から番号を選んでください",
    ["1", "2", "3", "4"],
    key="q3",
    index=None,
)

if q3 == "4":
  st.success("正解！ 🎉モンゴルの国旗は、赤・青・赤の順で、左側の赤地にソヨンボという意匠を配した旗。ソヨンボ文字はかつてモンゴルで使われていた文字で、ソヨンボの意味には色々な説がある。それぞれの図形は上から、火・太陽・月・矢・槍・長方形・巴をあらわしている。")
  score += 1
elif q3 is not None:
  st.error(
      "不正解… 正解は【4】です！"
  )

st.markdown("---")
# 第4問
st.subheader("第4問：モンゴルの国土面積は、日本の約何倍でしょう？")
q4 = st.radio(
    "選択してください",
    ["約2倍", "約4倍", "約8倍", "約10倍"],
    key="q4",
    index=None,
)
if q4 == "約4倍":
  st.success("正解！ 🎉")
  st.write(
      "正解は【約4倍】です！\n"
      "モンゴルの面積は約156万4,000平方キロメートルあり、日本の約4倍という広大な国土を持っています。"
  )
  score += 1
elif q4 is not None:
  st.error("不正解… 正解は「約4倍」です！")

st.markdown("---")


# 第5問
st.subheader("第5問：モンゴルの総人口はどれくらいでしょう？")
q5 = st.radio(
    "選択してください",
    ["約359万人", "約654万人", "約1,201万人", "約6,169万人"],
    key="q5",
    index=None,
)
if q5 == "約359万人":
  st.success("正解！ 🎉")
  st.write(
      "正解は【約359万人】です！\n"
      "日本の約4倍もの広大な国土がありながら、総人口は約359万人と非常に人口密度が低い国です。"
  )
  score += 1
elif q5 is not None:
  st.error("不正解… 正解は「約359万人」です！")

st.markdown("---")




# 第6問
st.subheader("第6問：モンゴル全土で飼育されている家畜（羊・ヤギ・馬・牛・ラクダ）の数はどれくらい？")
q6 = st.radio(
    "選択してください",
    ["約500万頭", "約1,500万頭", "約3,000万頭", "約6,500万頭"],
    key="q6",
    index=None,
)
if q6 == "約6,500万頭":
  st.success("正解！ 🎉")
  st.write(
      "正解は【約6,500万頭】です！\n"
      "家畜の数は約6,500万頭以上！"
      "1人あたり約20頭近くの家畜がいる計算になります。"
  )
  score += 1
elif q6 is not None:
  st.error("不正解… 正解は「約6,500万頭」です！")


st.markdown("---")



# 第7問

st.subheader("第7問：モンゴルの全人口（約350万人）のうち、首都ウランバートルに住んでいる人の割合はどれくらい？")
q7 = st.radio(
    "選択してください",
    ["約10％（10人に1人）", "約30％（3人に1人）", "約50％（約半分）", "約80％（ほとんど）"],
    key="q7",
    index=None,
)
if q7 == "約50％（約半分）":
  st.success("正解！ 🎉")
  st.write(
      "正解は【約50％（約半分）】です！\n"
      "モンゴルの総人口約350万人のうち、およそ160万〜170万人が首都ウランバートルに集中しています。"
      "広大な国土を持ちながら、一極集中が進んでいるのが特徴です。"
  )
  score += 1
elif q7 is not None:
  st.error("不正解… 正解は「約50％（約半分）」です！")

st.markdown("---")



# 第8問
st.subheader("第8問：モンゴルの通貨単位は何？")
q8 = st.radio(
    "選択してください", ["元 (CNY)", "ルーブル (RUB)", "トゥグルグ (MNT)", "ウォン (KRW)"], key="q8", index=None
)
if q8 == "トゥグルグ (MNT)":
  st.success("正解！ 🎉")
  score += 1
elif q8 is not None:
  st.error("不正解… 正解は「トゥグルグ（MNT）」です。")

st.markdown("---")



# 第9問
st.subheader("第9問：モンゴルの首都ウランバートルの標高は、およそどれくらいでしょう？")
q9 = st.radio(
    "選択してください",
    ["約126m", "約420m", "約850m", "約1,300m"],
    key="q9",
    index=None,
)
if q9 == "約1,300m":
  st.success("正解！ 🎉")
  st.write(
      "正解は【約1,300m】です！\n"
      "ウランバートルは標高約1,300m〜1,350mの高地に位置しています。"
      "日本の代表的な避暑地である軽井沢（約1,000m）よりも標高が高いため、年間を通して湿度が低く、夏でも朝晩は冷え込むのが特徴です。"
  )
  score += 1
elif q9 is not None:
  st.error("不正解… 正解は「約1,300m」です！")

st.markdown("---")




# 第10問
st.subheader("第10問：モンゴルの首都「ウランバートル」の言葉の意味はどれでしょう？")
q10 = st.radio(
    "選択してください",
    ["赤い英雄", "青い天空", "広い草原", "聖なる川"],
    key="q10",
    index=None,
)
if q10 == "赤い英雄":
  st.success("正解！ 🎉")
  st.write(
      "正解は【赤い英雄】です！\n"
      "モンゴル語で「ウラン（Улаан）」が赤、「バートル（Баатар）」が英雄を意味しています。1924年に現在の名称へ変更されました。"
  )
  score += 1
elif q10 is not None:
  st.error("不正解… 正解は「赤い英雄」です！")

st.markdown("---")




# 結果発表ボタン
# 結果発表ボタン
if st.button("🏆 結果を判定する"):
  st.markdown(f"### あなたのスコア： 10問中 **{score}問** 正解！")

  if score == 10:
    st.balloons()  # ← 全問正解（10点）の時だけ風船を飛ばす！
    st.write(
        "おめでとうございます！完全なるモンゴルマスターですね！新婚旅行の思い出が完璧に詰まっています✨"
    )
  elif score >= 7:
    st.write(
        "すごい！かなりのモンゴル通ですね！旅行の思い出がしっかり残っています。"
    )
  else:
    st.write("お疲れ様でした！旅行記をもう一度読み返すと新しい発見があるかも？")

# メインページに戻るリンク
st.markdown("---")
st.page_link("main.py", label="🏠 旅行記のトップに戻る", icon="⬅️")