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
st.subheader("第4問：小麦粉の生地を揚げた伝統的なおやつ・パンの名前は？")
q4 = st.radio(
    "選択してください",
    ["ボオルツォグ", "ホーショール", "ウルム", "スーテーツァイ"],
    key="q4",
    index=None,
)
if q4 == "ボオルツォグ":
  st.success("正解！ 🎉")
  score += 1
elif q4 is not None:
  st.error("不正解… 正解は「ボオルツォグ（揚げパン）」です。")

st.markdown("---")

# 第5問
st.subheader("第5問：手打ちの平麺とお肉・野菜を炒め煮にした麺料理の名前は？")
q5 = st.radio(
    "選択してください", ["ツォイワン", "ボーズ", "ホーショール", "ラム BBQ"], key="q5", index=None
)
if q5 == "ツォイワン":
  st.success("正解！ 🎉")
  score += 1
elif q5 is not None:
  st.error("不正解… 正解は「ツォイワン」です。")

st.markdown("---")

# 第6問
st.subheader("第6問：モンゴルの通貨単位は何？")
q6 = st.radio(
    "選択してください", ["元 (CNY)", "ルーブル (RUB)", "トゥグルグ (MNT)", "ウォン (KRW)"], key="q6", index=None
)
if q6 == "トゥグルグ (MNT)":
  st.success("正解！ 🎉")
  score += 1
elif q6 is not None:
  st.error("不正解… 正解は「トゥグルグ（MNT）」です。")

st.markdown("---")

# 第7問
st.subheader("第7問：ウランバートルの中心にある大きな広場の名前は？")
q7 = st.radio(
    "選択してください",
    ["レニン広場", "スフバートル広場", "チンギスハーン広場", "ピース広場"],
    key="q7",
    index=None,
)
if q7 == "スフバートル広場":
  st.success("正解！ 🎉")
  score += 1
elif q7 is not None:
  st.error("不正解… 正解は「スフバートル広場」です。")

st.markdown("---")

# 第8問
st.subheader("第8問：テレルジ国立公園にある、有名な奇岩の名前は？")
q8 = st.radio(
    "選択してください", ["ラクダ岩", "象岩", "亀石", "馬岩"], key="q8", index=None
)
if q8 == "亀石":
  st.success("正解！ 🎉")
  score += 1
elif q8 is not None:
  st.error("不正解… 正解は「亀石」です。")

st.markdown("---")

# 第9問
st.subheader("第9問：郊外にある世界最大級の像として有名なのは、誰の騎馬像？")
q9 = st.radio(
    "選択してください",
    ["フビライ・ハーン", "チンギス・ハーン", "バトゥ", "タイチウト"],
    key="q9",
    index=None,
)
if q9 == "チンギス・ハーン":
  st.success("正解！ 🎉")
  score += 1
elif q9 is not None:
  st.error("不正解… 正解は「チンギス・ハーン」です。")

st.markdown("---")

# 第10問
st.subheader("第10問：モンゴルで伝統的に飲まれている、お茶の味付けは何ベース？")
q10 = st.radio(
    "選択してください", ["塩味", "甘い砂糖味", "スパイシーな辛口", "酸っぱい発酵味"], key="q10", index=None
)
if q10 == "塩味":
  st.success("正解！ 🎉")
  score += 1
elif q10 is not None:
  st.error("不正解… 正解は「塩味（スーテーツァイなど、お茶に塩やミルクが入る）」です。")

st.markdown("---")

# 結果発表ボタン
if st.button("🏆 結果を判定する"):
  st.balloons()
  st.markdown(f"### あなたのスコア： 10問中 **{score}問** 正解！")
  if score == 10:
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