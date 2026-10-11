import streamlit as st

st.title("🇲🇳 モンゴル旅行")
st.write("2026年9月15日〜22日、新婚旅行でモンゴルに行ってきました。日本ではモンゴルの情報はそれほど多くないので、今後行く人の参考になればと思います。")
st.markdown("---")



# --- 1日目 ---
st.header("9月15日 (1日目)：モンゴルへ")
st.write("HISでMIAT航空成田空港14:40発チンギスハーン国際空港19:15着のチケットを購入していました。")
st.image("15th-inflightmeal.jpg", caption="機内食")
st.write("成田空港の滑走路の空き待ちで搭乗後ほぼ動かずで、30分くらい遅れで離陸しましたが、10分遅れくらいで無事にチンギスハーン国際空港に到着しました。")

google_map_html = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d171685.9411022192!2d106.62930973437955!3d47.750554393343144!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d96ba829ac7f471%3A0x832c94f726f1a30e!2z44OB44Oz44Ku44K544O744OP44O844Oz5Zu96Zqb56m65riv!5e0!3m2!1sja!2sjp!4v1791672244172!5m2!1sja!2sjp" width="400" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html, height=300)
st.write("到着後キャリーケースを受け取り、空港で１万円を換金しました。225,000MNTになりました。")
st.write("タクシーよりも格安なので、バスで空港からスフバートル広場に行きました。写真で言うとX19の路線です")
st.image("bus.jpeg", caption="バスの時刻表")


st.write("混んでいなければ１時間以内で行ける距離ですが、かなり渋滞していて、２時間くらいかかりました。しかも、バスの運転手さんがクラクションを鳴らしまくっていてとてもスリリング！😱")
st.markdown("---")


# --- 2日目 ---
st.header("9月16日 (2日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("16th-gandan.jpg", caption="ガンダン寺")
google_map_html = """

"""
st.components.v1.html(google_map_html, height=300)
st.markdown("---")

# #おまけ
# #streamlit run main.pyでローカルで確認できる。
# #初期設定①git init, ②git remote add origin https:/// 
# #　①git add . ②git commit -m"◯◯◯" .　③git push origin main