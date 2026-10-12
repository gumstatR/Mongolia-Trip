import streamlit as st

st.title("🇲🇳 モンゴル旅行")
st.write(
    "2026年9月15日〜22日、新婚旅行でモンゴルに行ってきました。"
    "日本ではモンゴルの情報はそれほど多くないので、今後行く人の参考になればと思います。"
)
st.markdown("---")

st.markdown("📌 目次")
st.markdown(
    """
- [9月15日（1日目）](#day1)モンゴルへ
- [9月16日（2日目）](#day2)市内観光（ガンダン寺、アジアナレストラン、ザイサントルゴイ）
- [9月17日（3日目）](#day3)テレルジ観光（亀石、乗馬1回目、ゲル泊）
- [9月18日（4日目）](#day4)テレルジ観光（乗馬2回目、チンギスハーン騎馬像）
- [9月19日（5日目）](#day5)市内観光（子どもの宮殿）
- [9月20日（6日目）](#day6)市内観光（ノミンデパート、ザ・ブル）
- [9月21日（7日目）](#day7)市内観光（スフバートル広場、ナゴミ）
- [9月22日（8日目）](#day8)1日遅れの帰国
- その他（気候や交通など）
"""
)

# --- 1日目 ---
st.markdown('<div id="day1"></div>', unsafe_allow_html=True)
st.header("9月15日 (1日目)：モンゴルへ")
st.write( "HIS予約したMIAT航空成田空港14:40発チンギスハーン国際空港19:15着にてモンゴルへ。")
st.image("15th-inflightmeal.jpg", caption="機内食")
st.write("成田空港の滑走路の空き待ちで搭乗後ほぼ動かずで、30分くらい遅れで離陸しましたが、10分遅れくらいで無事にチンギスハーン国際空港に到着。")

google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d171685.9411022192!2d106.62930973437955!3d47.750554393343144!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d96ba829ac7f471%3A0x832c94f726f1a30e!2z44OB44Oz44Ku44K544O744OP44O844Oz5Zu96Zqb56m65riv!5e0!3m2!1sja!2sjp!4v1791699219960!5m2!1sja!2sjp" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.write("到着後キャリーケースを受け取り、空港で１万円を換金。225,000MNT入手。")
st.write("タクシーよりも格安なので、バスで空港からスフバートル広場へ。写真のX19の路線")
st.image("bus.jpeg", caption="バスの時刻表")
st.link_button(
    "🚌 参考Webサイト（チンギスハーン国際空港のWebページ）",
    "https://en.ulaanbaatar-airport.mn/public-transportation-service",
)
st.write("はじめは高速道路を快調に進む。しかし、ウランバートルに近づくにつれて様子が激変。渋滞による地獄のクラクション祭り😱どの車も車間距離がものすごく狭く、車線変更や脇道からの侵入は強引突破。ずっとどこかでクラクションが鳴っている感覚。本来は１時間かからない距離ですが、２時間くらいかかった。早くも日本に帰りたい気持ちになる。")
st.write("夜10時頃スフバートル広場に到着。チェックインの時間を過ぎていたためホテル（東横イン）まで急ぐ。")
st.image("15th-hotel1.jpg", caption="東横イン(撮影は9月17日)")
st.write("チェックイン時間が過ぎていてもチェックインできた。")
st.image("15th-hotel2.jpg", caption="東横イン（撮影は9月17日）")
st.write("ウランバートルにあっても東横インは東横イン。ホッとするお部屋のレイアウト")
st.image("15th-hotel3.jpg", caption="泊まったお部屋（一部加工あり）")
st.image("15th-hotel4.jpg", caption="泊まったお部屋（一部加工あり）")


st.markdown("---")


# --- 2日目 ---
st.markdown('<div id="day2"></div>', unsafe_allow_html=True)
st.header("9月16日 (2日目)：市内観光")
st.write("16日はウランバートル市内を主に徒歩で観光した。")
st.write("まずはホテルで朝食（バイキング形式）。")
st.image("16th-breakfast1.jpg", caption="東横イン（ウランバートル）の朝食")
st.image("16th-breakfast2.jpg", caption="東横イン（ウランバートル）の朝食")
st.write("まずはホテル近くのガンダン寺。モンゴル最大のチベット仏教寺院。")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.write("観音堂にある高さ26.5mの観音像")
st.image("16th-gandan2.jpg", caption="開眼観音像")
st.write("ガンダン寺から歩いて1時間くらいのアジアナレストランに行った。")
google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2675.5933314016233!2d106.90861937659413!3d47.88620026862803!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d9693c1eb0b3239%3A0xfa563058e299148a!2z44Ki44K444Ki44OK44Os44K544OI44Op44Oz!5e0!3m2!1sja!2sjp!4v1791768516372!5m2!1sja!2sjp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.image("16th-lunch1.jpg", caption="店内（ゲルのところは後から来た団体客に予約されていた）")
st.image("16th-lunch2.jpg", caption="前菜で出てきたボオルツォグ（Boortsog / ボールツォグ）モンゴルの伝統的な揚げパン")
st.image("16th-lunch3.jpg", caption="ホーショール（Khuushuur）小麦粉の生地でひき肉（主に羊肉や牛肉）とタマネギなどの具材を包み、油でカリッと揚げたモンゴルの定番料理。")
st.image("16th-lunch4.jpg", caption="ボーズ（Buuz）小麦粉の生地で刻んだ肉（主に羊肉や牛肉）とタマネギ、塩などを包み、蒸籠（セイロ）で蒸し上げたモンゴルの代表的な餃子（小籠包や肉まんのような形）。")
st.write("アジアナレストラン近くにあるザインサントルゴイに行った。")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.write("高いところにあるので、ここからの景色は良い。")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")

# --- 3日目 ---
st.markdown('<div id="day3"></div>', unsafe_allow_html=True)
st.header("9月17日 (3日目)：テレルジ観光")
st.write("ホテルで朝食をとり、チェックアウトした。HISの１泊２日のツアーに参加した。10時にホテルにガイドさんが迎えに来た。運転手さんが別にいた。")
st.image("17th-his1.jpeg", caption="予約したツアー")
st.image("17th-his2.jpeg", caption="ツアー行程")
st.write("やはりウランバートル市内は渋滞。運転手さんが細い路地に入っていき、渋滞を回避しようとするが、事故を起こしそうで怖い（多分運転手は運転が上手）。")
st.write("途中でノミンのスーパーマーケットに寄った。ガイドさんに勧められ水を買った。")
st.write("途中アスファルト舗装がないところもあったが、12時前に無事に亀石に到着した。30分くらい自由時間となった。ここではイヌワシを持つことができる。")
st.image("17th-kame.jpg", caption="亀石")
st.write("亀石から遊牧民宅を目指すが、道に迷う。途中で２、３回人に聞いたり、電話してたりして13時20分頃なんとか到着。HIS大丈夫か？")
st.write("ここで昼食をいただく。いわゆる課外学習用のゲルで、実際に住んでいるゲルには入らせてもらえなかった。")
st.image("17th-lunch.jpg", caption="モンゴルの代表的な麺料理「ツォイワン（Tsuivan）」")
st.write("昼食後、乗馬をした。自分で馬をコントロールすることはなく、遊牧民の人が前で馬の手綱を持っているため、乗っているだけ。")
st.write("山林は空気が良く、黄色く色づいた黄葉が綺麗。何箇所か川を渡ったりして、これには大満足。")
st.image("17th-joba1.png", caption="乗馬（一部写真を加工）")
st.image("17th-joba2.jpg", caption="休憩時")
st.write("乗馬の後、本日泊まるゲルに到着。場所はアロンゴ・ツーリストキャンプだった。")
st.image("17th-geru1.jpg", caption="アロンゴ・ツーリストキャンプ")
st.image("17th-geru2.jpg", caption="ゲル内")
st.image("17th-geru3.jpg", caption="ゲル（シャワー室とトイレ）")

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
st.header("9月19日 (5日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("19th-breakfast.jpg", caption="朝食")
st.image("19th-hotel.jpg", caption="ホテル")
st.image("19th-museum1.jpg", caption="博物館")
st.image("19th-museum2.jpg", caption="博物館")
st.image("19th-palace1.jpg", caption="子供の宮殿")
st.image("19th-palace2.jpg", caption="子供の宮殿")
st.image("19th-palace3.jpg", caption="子供の宮殿")
st.image("19th-dinner1.jpg", caption="夕食")
st.image("19th-dinner2.jpg", caption="夕食")
st.image("19th-dinner3.jpg", caption="夕食")
st.markdown("---")



# --- 6日目 ---
st.markdown('<div id="day6"></div>', unsafe_allow_html=True)
st.header("9月20日 (6日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("20th-depart1.jpg", caption="ノミンデパート")
st.image("20th-depart2.jpg", caption="ノミンデパート")
st.image("20th-ice1.jpg", caption="アイスクリーム")
st.image("20th-ice2.jpg", caption="アイスクリーム")
st.image("20th-lunch1.jpg", caption="昼食")
st.image("20th-lunch2.jpg", caption="昼食")
st.image("20th-flight.jpg", caption="１日遅れ確定")

st.markdown("---")




# --- 7日目 ---
st.markdown('<div id="day7"></div>', unsafe_allow_html=True)
st.header("9月21日 (7日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("21th-breakfast.jpg", caption="朝食")
st.image("21th-peace1.jpg", caption="平和の鐘")
st.image("21th-peace2.jpg", caption="平和の鐘")
st.image("21th-square1.jpg", caption="スフバートル広場")
st.image("21th-square2.jpg", caption="スフバートル広場")
st.image("21th-square3.jpg", caption="スフバートル広場")
st.image("21th-square4.jpg", caption="スフバートル広場")
st.image("21th-shop1.jpg", caption="お店")
st.image("21th-shop2.jpg", caption="お店")
st.image("21th-shop3.jpg", caption="お店")
st.image("21th-shop4.jpg", caption="お店")
st.image("21th-lunch1.jpg", caption="昼食")
st.image("21th-lunch2.jpg", caption="昼食")
st.image("21th-lunch3.jpg", caption="昼食")


st.markdown("---")





# --- 8日目 ---
st.markdown('<div id="day8"></div>', unsafe_allow_html=True)
st.header("9月22日 (8日目)：市内観光")
st.write("ウランバートル市内を主に徒歩で観光しました")
st.image("22th-port1.jpg", caption="チンギスハーン国際空港")
st.image("22th-port2.jpg", caption="チンギスハーン国際空港")
st.image("22th-port3.jpg", caption="チンギスハーン国際空港")
st.image("22th-port4.jpg", caption="チンギスハーン国際空港")
st.image("22th-port5.jpg", caption="チンギスハーン国際空港")
st.image("22th-flight1.jpg", caption="飛行機")
st.image("22th-flight2.jpg", caption="飛行機")

st.markdown("---")




# #おまけ
# #streamlit run main.pyでローカルで確認できる。
# #初期設定①git init, ②git remote add origin https:/// 
# #　①git add . ②git commit -m"◯◯◯" .　③git push origin main