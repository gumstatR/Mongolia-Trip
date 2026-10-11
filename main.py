import streamlit as st

st.title("🇲🇳 モンゴル旅行")
st.write(
    "2026年9月15日〜22日、新婚旅行でモンゴルに行ってきました。"
    "日本ではモンゴルの情報はそれほど多くないので、今後行く人の参考になればと思います。"
)
st.markdown("---")

# --- 最初から見えている目次 ---
st.markdown("### 📌 目次")
st.markdown(
    """
- [9月15日（1日目）：モンゴルへ](#day1)
- [9月16日（2日目）：市内観光（ガンダン寺、ザイサントルゴイ）](#day2)
- [9月17日（3日目）：テレルジ観光（亀石、乗馬1回目、ゲル泊）](#day3)
- [9月18日（4日目）：テレルジ観光（乗馬2回目、チンギスハーン騎馬像）](#day4)
- [9月19日（5日目）：市内観光（ノミンデパート、子どもの宮殿）](#day5)
- [9月20日（6日目）：市内観光（マリーマーサ、昼食）](#day6)
- [9月21日（7日目）：市内観光（ザナバザル美術館）](#day7)
- [9月22日（8日目）：1日遅れの帰国](#day8)


"""
)
st.markdown("---")

# --- 1日目 ---
st.markdown('<div id="day1"></div>', unsafe_allow_html=True)
st.header("9月15日 (1日目)：モンゴルへ")
st.write( "HISでMIAT航空成田空港14:40発チンギスハーン国際空港19:15着のチケットを購入していました。")
st.image("15th-inflightmeal.jpg", caption="機内食")
st.write("成田空港の滑走路の空き待ちで搭乗後ほぼ動かずで、30分くらい遅れで離陸しましたが、10分遅れくらいで無事にチンギスハーン国際空港に到着しました。")

google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d171685.9411022192!2d106.62930973437955!3d47.750554393343144!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d96ba829ac7f471%3A0x832c94f726f1a30e!2z44OB44Oz44Ku44K544O744OP44O844Oz5Zu96Zqb56m65riv!5e0!3m2!1sja!2sjp!4v1791699219960!5m2!1sja!2sjp" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.write("到着後キャリーケースを受け取り、空港で１万円を換金しました。225,000MNTになりました。")
st.write("タクシーよりも格安なので、バスで空港からスフバートル広場に行きました。写真で言うとX19の路線です")
st.image("bus.jpeg", caption="バスの時刻表")
st.link_button(
    "🚌 参考Webサイト（チンギスハーン国際空港のWebページ）",
    "https://en.ulaanbaatar-airport.mn/public-transportation-service",
)
st.write("混んでいなければ１時間以内で行ける距離ですが、かなり渋滞していて、２時間くらいかかりました。しかも、バスの運転手さんがクラクションを鳴らしまくっていてとてもスリリング！😱")
st.markdown("---")


# --- 2日目 ---
st.markdown('<div id="day2"></div>', unsafe_allow_html=True)
st.header("9月16日 (2日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.image("16th-lunch1.jpg", caption="昼食")
st.image("16th-lunch2.jpg", caption="昼食")
st.image("16th-lunch3.jpg", caption="昼食")
st.image("16th-lunch4.jpg", caption="昼食")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")

# --- 3日目 ---
st.markdown('<div id="day3"></div>', unsafe_allow_html=True)
st.header("9月17日 (3日目)：テレルジ観光")
st.write("HISのツアーに参加しました。亀石、乗馬1回目、ゲル泊を体験しました。")
st.image("17th-kame.jpg", caption="亀石")
st.image("17th-lunch.jpg", caption="昼食")
st.image("17th-joba1.jpg", caption="乗馬")
st.image("17th-joba2.jpg", caption="乗馬")
st.image("17th-geru1.jpg", caption="ゲル")
st.image("17th-geru2.jpg", caption="ゲル")
st.image("17th-geru3.jpg", caption="ゲル")

st.markdown("---")





# --- 4日目 ---
st.markdown('<div id="day4"></div>', unsafe_allow_html=True)
st.header("9月18日 (4日目)：ツアー２日目")
st.write("HISのツアーに参加しました。乗馬2回目、チンギスハーン騎馬像を観光しました。")
st.image("18th-breakfast1.jpg", caption="朝食")
st.image("18th-breakfast2.jpg", caption="朝食")
st.image("18th-joba1.jpg", caption="乗馬")
st.image("18th-joba2.jpg", caption="乗馬")
st.image("18th-lunch.jpg", caption="昼食")
st.image("18th-kibazou1.jpg", caption="騎馬像")
st.image("18th-kibazou2.jpg", caption="騎馬像")
st.image("18th-kibazou3.jpg", caption="騎馬像")
st.image("18th-hotel1.jpg", caption="ホテル")
st.image("18th-hotel2.jpg", caption="ホテル")
st.image("18th-hotel3.jpg", caption="ホテル")
st.image("18th-dinner1.jpg", caption="夕食")
st.image("18th-dinner2.jpg", caption="夕食")
st.image("18th-dinner3.jpg", caption="夕食")

st.markdown("---")



# --- 5日目 ---
st.markdown('<div id="day5"></div>', unsafe_allow_html=True)
st.header("9月18日 (5日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.image("16th-lunch1.jpg", caption="昼食")
st.image("16th-lunch2.jpg", caption="昼食")
st.image("16th-lunch3.jpg", caption="昼食")
st.image("16th-lunch4.jpg", caption="昼食")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")



# --- 6日目 ---
st.markdown('<div id="day6"></div>', unsafe_allow_html=True)
st.header("9月19日 (6日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.image("16th-lunch1.jpg", caption="昼食")
st.image("16th-lunch2.jpg", caption="昼食")
st.image("16th-lunch3.jpg", caption="昼食")
st.image("16th-lunch4.jpg", caption="昼食")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")




# --- 7日目 ---
st.markdown('<div id="day7"></div>', unsafe_allow_html=True)
st.header("9月20日 (7日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.image("16th-lunch1.jpg", caption="昼食")
st.image("16th-lunch2.jpg", caption="昼食")
st.image("16th-lunch3.jpg", caption="昼食")
st.image("16th-lunch4.jpg", caption="昼食")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")





# --- 8日目 ---
st.markdown('<div id="day2"></div>', unsafe_allow_html=True)
st.header("9月16日 (2日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.image("16th-lunch1.jpg", caption="昼食")
st.image("16th-lunch2.jpg", caption="昼食")
st.image("16th-lunch3.jpg", caption="昼食")
st.image("16th-lunch4.jpg", caption="昼食")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")




# #おまけ
# #streamlit run main.pyでローカルで確認できる。
# #初期設定①git init, ②git remote add origin https:/// 
# #　①git add . ②git commit -m"◯◯◯" .　③git push origin main