import streamlit as st
st.set_page_config(
    page_title="モンゴル旅行の記録",
    page_icon="🇲🇳",
    initial_sidebar_state="collapsed",  # ← これで最初からサイドバーが閉じます！
)
st.sidebar.header("🎵 モンゴルの雰囲気を音楽で")

# st.sidebar.video にYouTubeのURLを渡すだけで、プレイヤーが設置されます
# （デフォルトで自動再生はオフ＝ユーザーが再生ボタンを押さないと再生されません）
st.sidebar.video("https://www.youtube.com/watch?v=p_5yt5IX38I")
st.title("🇲🇳 モンゴル旅行")
st.write(
    "2026年9月15日〜22日、モンゴルに行ってきました。"
    "日本ではモンゴルの情報はそれほど多くないので、皆様の参考になればと思います。"
    "クイズのページも用意したので、ぜひお楽しみください（ページ最下部か左サイドバーのリンクから飛べます）。"

)
st.markdown("---")

st.markdown("📌 目次")
st.markdown(
    """
- [9月15日（1日目）](#day1)モンゴルへ
- [9月16日（2日目）](#day2)市内観光（ガンダン寺、アジアナレストラン、ザイサントルゴイ）
- [9月17日（3日目）](#day3)テレルジ観光（亀石、乗馬1回目、ゲル泊）
- [9月18日（4日目）](#day4)テレルジ観光（乗馬2回目、チンギスハーン騎馬像）
- [9月19日（5日目）](#day5)市内観光（チンギスハーン国立博物館、子供の宮殿）
- [9月20日（6日目）](#day6)市内観光（ノミンデパート、ザ・ブル）
- [9月21日（7日目）](#day7)市内観光（スフバートル広場、ナゴミ）
- [9月22日（8日目）](#day8)1日遅れの帰国
- おまけ

"""
)

# --- 1日目 ---
st.markdown('<div id="day1"></div>', unsafe_allow_html=True)
st.header("9月15日 (1日目)：モンゴルへ")
st.write( "HIS予約したMIAT航空成田空港14:40発チンギスハーン国際空港19:15着の便にてモンゴルへ。")
st.image("15th-inflightmeal.jpg", caption="機内食")
st.write("成田空港の滑走路の空き待ちで搭乗後しばらく動かず。30分くらい遅れで離陸。10分遅れくらいで無事にチンギスハーン国際空港に到着。")

google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d171685.9411022192!2d106.62930973437955!3d47.750554393343144!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d96ba829ac7f471%3A0x832c94f726f1a30e!2z44OB44Oz44Ku44K544O744OP44O844Oz5Zu96Zqb56m65riv!5e0!3m2!1sja!2sjp!4v1791699219960!5m2!1sja!2sjp" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.write("到着後キャリーケースを受け取り、空港で１万円を換金。225,000MNT(トゥグルグ)入手。")
st.write("タクシーよりも格安なので、バスで空港からスフバートル広場へ。写真のX19の路線。")
st.image("bus.jpeg", caption="バスの時刻表")
st.link_button(
    "🚌 参考Webサイト（チンギスハーン国際空港のWebページ）",
    "https://en.ulaanbaatar-airport.mn/public-transportation-service",
)
st.write("はじめは高速道路を快調に進む。しかし、ウランバートルに近づくにつれて様子が激変。渋滞による地獄のクラクション祭り😱どの車も車間距離がものすごく狭く、車線変更や脇道からの侵入は強引突破。ずっとどこかでクラクションが鳴っている感覚。本来は１時間かからない距離だが、２時間くらいかかった。早くも日本に帰りたい気持ちになる。")
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
st.write("16日はウランバートル市内を観光することとしていた。")
st.write("まずはホテルで朝食（バイキング形式）。日本の東横インとほぼ同じ感じ。")
st.image("16th-breakfast1.jpg", caption="東横イン（ウランバートル）の朝食")
st.image("16th-breakfast2.jpg", caption="東横イン（ウランバートル）の朝食")
st.write("まずはホテル近くのガンダン寺。モンゴル最大のチベット仏教寺院。")
st.image("16th-gandan.jpg", caption="ガンダン寺")
st.write("観音堂にある高さ26.5mの観音像")
st.image("16th-gandan2.jpg", caption="開眼観音像")
st.write("ガンダン寺から歩いて1時間くらいのアジアナレストランに行った。2人で4,078円かかったがモンゴル料理を堪能できて満足した。")
google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2675.5933314016233!2d106.90861937659413!3d47.88620026862803!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d9693c1eb0b3239%3A0xfa563058e299148a!2z44Ki44K444Ki44OK44Os44K544OI44Op44Oz!5e0!3m2!1sja!2sjp!4v1791768516372!5m2!1sja!2sjp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.image("16th-lunch1.jpg", caption="店内（ゲルのところは後から来た団体客に予約されていた）")
st.image("16th-lunch2.jpg", caption="前菜で出てきたボオルツォグ（Boortsog / ボールツォグ）モンゴルの伝統的な揚げパン。右側の白いのをかじってみたらお手拭きだった💦")
st.image("16th-lunch3.jpg", caption="ホーショール（Khuushuur）小麦粉の生地でひき肉（主に羊肉や牛肉）とタマネギなどの具材を包み、油でカリッと揚げたモンゴルの定番料理。")
st.image("16th-lunch4.jpg", caption="ボーズ（Buuz）小麦粉の生地で刻んだ肉（主に羊肉や牛肉）とタマネギ、塩などを包み、蒸籠（セイロ）で蒸し上げたモンゴルの代表的な餃子（小籠包や肉まんのような形）。")
st.write("ご飯を食べた後は近くにあるザイサントルゴイに行った。途中までエレベーターで登ることができるが、最初から徒歩で階段をかけ登った。")
st.image("16th-zaisan1.jpg", caption="ザイサントルゴイ")
st.write("高いところにあるので、ここからの景色は良い。")
st.image("16th-zaisan2.jpg", caption="ザイサントルゴイ")

st.markdown("---")

# --- 3日目 ---
st.markdown('<div id="day3"></div>', unsafe_allow_html=True)
st.header("9月17日 (3日目)：テレルジ観光１日目")
st.write("ホテルで朝食をとり、チェックアウトした。HISの１泊２日のツアーに参加した。10時にホテルにガイドさんが迎えに来た。運転手さんが別にいた。")
st.image("17th-his1.jpeg", caption="予約したツアー")
st.image("17th-his2.jpeg", caption="ツアー行程")
st.write("やはりウランバートル市内は渋滞。運転手さんが細い路地に入っていき、渋滞を回避しようとするが、事故を起こしそうで怖い（多分運転手は運転が上手）。")
st.write("途中でノミンのスーパーマーケットに寄った。ガイドさんに勧められ水を買った。")
st.write("途中アスファルト舗装がないところもあったが、12時前に無事に亀石に到着した。30分くらい自由時間となった。ここではイヌワシを持つことができる（有料）。")
st.image("17th-kame.jpg", caption="亀石")
st.write("亀石から遊牧民宅を目指すが、道に迷う。ガイドさんが途中で２、３回人に聞いたり、電話してたりして13時20分頃なんとか到着。HIS大丈夫か？")
st.write("ここで昼食をいただく。いわゆる課外学習用のゲルで、実際に住んでいるゲルには入らせてもらえなかった。")
st.image("17th-lunch.jpg", caption="モンゴルの代表的な麺料理「ツォイワン（Tsuivan）」")
st.write("昼食後、乗馬をした。自分で馬をコントロールすることはなく、遊牧民の人が前で馬の手綱を持っているため、乗っているだけ。")
st.write("山林は空気が良く、黄色く色づいた紅葉が綺麗。何箇所か川を渡ったりして、これには大満足。")
st.image("17th-joba1.png", caption="乗馬（一部写真を加工）")
st.image("17th-joba2.jpg", caption="休憩時")
st.write("乗馬の後、泊まるゲルに到着。場所はアロンゴ・ツーリストキャンプだった。")
google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1570.197108780571!2d107.43011274639122!3d47.87709665864826!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d942f6f5fb48101%3A0x7976dbf7545edfee!2z44Ki44Ot44Oz44K044O744OE44O844Oq44K544OI44Kt44Oj44Oz44OX!5e0!3m2!1sja!2sjp!4v1791946310631!5m2!1sja!2sjp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)

st.image("17th-geru1.jpg", caption="アロンゴ・ツーリストキャンプ")
st.write("夕食はここの食堂でガイドさん、運転手さんと一緒に食べた。")
st.image("17th-dinner1.jpg", caption="夕食")
st.image("17th-dinner2.jpg", caption="夕食")
st.write("ゲル内の様子。寝る前には虫が入ってきた。")
st.image("17th-geru2.jpg", caption="ゲル内")
st.write("デラックスプランにしていたため、シャワーとトイレがついていた。しかし、建てつけが悪くシャワーの扉はちゃんと閉じない。ドライヤーがあったが途中で壊れた。")
st.image("17th-geru3.jpg", caption="シャワー室とトイレ")
st.write("昼間は天気が良かったが、夕方ごろから雨が降ってきて、かなり冷えた。暖炉があり、薪を入れてもらうとすごく暖かくなるが、２時間もしたらまたすぐ冷えた。あと、写真のとおり雨漏りしていた。")
st.image("17th-geru4.jpg", caption="暖炉と雨漏り")


st.markdown("---")





# --- 4日目 ---
st.markdown('<div id="day4"></div>', unsafe_allow_html=True)
st.header("9月18日 (4日目)：テレルジ観光２日目")
st.write("HISツアー２日目。")
st.write("朝８時に食堂で朝食を食べた（バイキング形式）。ガイドさんも来ると思っており待っていたが、朝食時は来なかった。")
st.image("18th-breakfast1.jpg", caption="朝食")
st.image("18th-breakfast2.jpg", caption="朝食")
st.write("９時４５分ガイドさん合流。雨が降っているので、この日の乗馬をやめるか、時間を短縮するか等検討したが、やることにした。")
st.write("１０時頃アロンゴ・ツーリストキャンプから移動。すぐに乗馬する遊牧民宅に到着（昨日とは別のところ）。雨のため、遊牧民の方が乗馬の準備をしていなかったが、準備してもらった。雨の中、１０時３０分頃から乗馬開始。")
st.image("18th-joba1.png", caption="乗馬の様子（一部加工あり）")
st.write("乗馬開始後、雨が止んできた。この日は草原のコースだった。これはこれで良かった。風は冷たく、寒かった。")
st.image("18th-joba1.jpg", caption="休憩時")
st.write("乗馬後、再びアロンゴ・ツーリストキャンプに戻って、１３時頃から昼食。ホーショルが出てきた。")
st.image("18th-lunch.jpg", caption="昼食（ホーショル）")
st.write("昼食後移動し、１４時３０分ごろチンギスハーン騎馬像に到着。到着時の天気は曇りだったが、帰る際には晴天になっていた。高さ４０ｍは迫力満点。")
st.image("18th-kibazou1.jpg", caption="チンギスハーン騎馬像")
st.link_button(
    "🔍チンギス・カン騎馬像ホームページ",
    "https://giantkhanstatue.com/ja/",
)
st.write("施設の中から登ることができた。")
st.image("18th-kibazou2.jpg", caption="チンギスハーン騎馬像")
st.write("中は複合施設になっていて見学できた。")
st.image("18th-kibazou3.jpg", caption="複合施設内")
st.image("18th-kibazou4.jpg", caption="複合施設内")
st.write("また、ここではラクダに乗ることができた。ラクダが座った状態からラクダに跨いだが、勢いよく立ち上がるため、一瞬怖いが、一周して楽しかった。他にも弓矢も体験できる。")
st.image("18th-kibazou5.png", caption="ラクダ")
st.write("１７時頃ホテルに到着し、HISのツアー終了。")
st.image("18th-hotel1.jpg", caption="ウランバートルホテル（19時30分頃撮影）")
st.write("お部屋は広く、快適。")
st.image("18th-hotel2.jpg", caption="ウランバートルホテルのお部屋")
st.write("バスルームに大きなバスタブとトイレ、奥にシャワールームがあった。")
st.image("18th-hotel3.jpg", caption="バスルーム")
st.write("散歩をしつつ、20時30頃たまたま見つけたお店でラーメンを食べた。")
google_map_html_1 = """
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d905.3939774088424!2d106.92331209676534!3d47.91279884058488!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5d96932ac3ef43c3%3A0xf1c77d614071ddc5!2z44Gf44GR44GV44KT5ZGz5ZmM44Op44O844Oh44OzIOOCquODquODs-ODlOODg-OCr-OCruODo-ODqeODquOCog!5e0!3m2!1sja!2sjp!4v1791954381398!5m2!1sja!2sjp" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
"""
st.components.v1.html(google_map_html_1, height=300)
st.image("18th-dinner1.jpg", caption="外観")
st.image("18th-dinner2.jpg", caption="土鍋味噌ラーメンたけさん")
st.write("ラーメンは普通に美味しかった。")
st.image("18th-dinner3.jpg", caption="夕食のラーメン")

st.markdown("---")



# --- 5日目 ---
st.markdown('<div id="day5"></div>', unsafe_allow_html=True)
st.header("9月19日 (5日目)：市内観光")
st.write("この日は主に国立チンギスハーン博物館と子供の宮殿に行った。")
st.write("まずはホテルで朝食を食べた。")
st.image("breakfast1.jpg", caption="朝食会場")
st.write("ここでもバイキング形式で嬉しい。")
st.image("breakfast2.jpg", caption="朝食バイキング")
st.image("19th-breakfast.jpg", caption="朝食")
st.write("１０時前にお出かけした。良い天気。")
st.image("19th-hotel.jpg", caption="ホテル")
st.write("１０時３０分頃、国立チンギスハン博物館に到着。")
st.image("19th-museum1.jpg", caption="博物館")
st.link_button(
    "🔍国立チンギスハン博物館のホームページ",
    "https://chinggismuseum.com/en",
)
st.write("９階まであって、しっかり見たら１日かかるくらい展示物が多かった。モンゴルの歴史がよく分かると思う。きっと価値の高いものが多かったんだろう。見応えがあったのは９階にあったチンギスハンの黄金像。この黄金像の部屋の前に２人のスタッフがいて、靴カバーをつけて鞄を外に置かなければならなかった。")
st.image("19th-museum2.jpg", caption="チンギスハンの黄金像")
st.write("１７時すぎに子供の宮殿に到着。ここではモンゴル伝統芸能の公演を見た。")
st.image("19th-palace1.jpg", caption="子供の宮殿")
st.write("１８時から１９時５分までで、演目は馬頭琴などの伝統楽器の演奏のほか、ホーミーやオルティン・ドーなどの民謡、軟体芸など盛り沢山。")
st.image("19th-palace2.jpg", caption="トゥメンエヘ歌舞団")
st.image("19th-palace3.jpg", caption="トゥメンエヘ歌舞団")
st.write("夕食はピザハットのピザを買い、ホテルで食べた。")
st.image("19th-dinner1.jpg", caption="ピザハット")
st.image("19th-dinner2.jpg", caption="夕食")
st.image("19th-dinner3.jpg", caption="夕食")
st.markdown("---")



# --- 6日目 ---
st.markdown('<div id="day6"></div>', unsafe_allow_html=True)
st.header("9月20日 (6日目)：市内観光")
st.write("この日は活動する最後の日の予定だったため、主にお土産を買うことにした。")
st.write("多くの観光客が集まるノミンデパート。")
st.image("20th-depart1.jpg", caption="ノミンデパート")
st.write("地下１階に観光客向けの食品があるが、このエスカレーターの場所が分かりづらい。")
st.image("20th-depart2.jpg", caption="ノミンデパート（１階〜地下１階）")
st.write("街中にこのようなアイスクリーム屋がたくさんあったから食べた。")
st.image("20th-ice1.jpg", caption="アイスクリーム")
st.image("20th-ice2.jpg", caption="アイスクリーム")
st.write("昼食はTHEBULLというお店でしゃぶしゃぶを食べた。")
st.image("20th-lunch1.jpg", caption="昼食")
st.image("20th-lunch2.jpg", caption="昼食")
st.write("昼食後少しお散歩して14:40にホテルに到着。予定では21日の朝4時45分にホテルにお迎えに来てもらい、チンギスハーン空港を7時45分発の便で日本に帰る予定なので、ホテルでゆっくりしていた。")
st.write("しかし、気がかりなのは台風25号の影響だ。台風情報を何回も確認しつつ、なんとか日本に帰れるのではないかと楽観視していた。結果的には、台風のスピードが速くなり、、、")
st.image("20th-taihoo.png", caption="銚子地方気象台『令和８年(2026年)台風25号に関する千葉県気象速報』より")
st.write("16時10分頃、明日日本に帰れないことが確定してしまう。乗る予定は501便だったが、22日の午前5時に変更された。")
st.image("20th-flight.jpg", caption="１日遅れ確定")
st.write("空港泊することも考えたが、海外旅行保険に入っていたため、21日夜は再び東横インに泊まることにした。")


st.markdown("---")




# --- 7日目 ---
st.markdown('<div id="day7"></div>', unsafe_allow_html=True)
st.header("9月21日 (7日目)：市内観光")
st.write("日本に帰っていたら食べられなかったが、この日もウランバートルホテルで朝食を食べることができた。")
st.image("21th-breakfast.jpg", caption="朝食")
st.write("9時頃散歩を開始。スフバートル広場で世界平和の鐘を見つけた。")
st.image("21th-peace1.jpg", caption="平和の鐘")
st.write("スフバートル広場で昨日まではチェスのイベントをやっていて、盛り上がっていたが、この日はやっていない。")
st.image("21th-square1.jpg", caption="スフバートル広場")
st.image("21th-square2.jpg", caption="スフバートル広場")
st.image("21th-square3.jpg", caption="チンギスハーン")
st.image("21th-square4.jpg", caption="スフバートル広場")
st.write("再び街をぶらぶらしている時に良いお店を見つける。")
st.image("21th-shop1.jpg", caption="お店")
st.image("21th-shop2.jpg", caption="お店")
st.write("お土産で買えそうなものがたくさんあった。")
st.image("21th-shop3.jpg", caption="店内の様子")
st.image("21th-shop4.jpg", caption="店内の様子")
st.write("一度ウランバートルホテルに戻り、11時30分頃にチェックアウトし、キャリーケースをホテルに預けた。")
st.write("昼食はNAGOMIで食べた。日本食が完全再現されていて美味しかった。")
st.image("21th-lunch1.jpg", caption="昼食")
st.image("21th-lunch2.jpg", caption="昼食")
st.write("昼食後、ザナバザルに行き、ウランバートルホテルでキャリーケースを受け取り、東横インでチェックインした。その際、翌朝空港までのタクシーの手配をお願いした。")

st.markdown("---")





# --- 8日目 ---
st.markdown('<div id="day8"></div>', unsafe_allow_html=True)
st.header("9月22日 (8日目)：市内観光")
st.write("朝1時に起床。1時45分にチェックアウトし、タクシーに乗った。道路はさすがに空いてて2時30分に空港に着いた。")
st.image("22th-port1.jpg", caption="チンギスハーン国際空港")
st.write("チンギスハーン国際空港は日本がODAで資金を援助している。")
st.image("22th-port2.jpg", caption="チンギスハーン国際空港")
st.image("22th-port4.jpg", caption="チンギスハーン国際空港")
st.write("空港で寝てる人がたくさんいた。")
st.image("22th-port5.jpg", caption="チンギスハーン国際空港")
st.write("5時に離陸した。")
st.image("22th-flight1.jpg", caption="飛行機")
st.image("22th-flight2.jpg", caption="機内食")
st.write("無事に成田空港に10時30分に到着し、家に帰った。")

st.markdown("---")

# メインファイルの最後のほうに追加
st.subheader("🇲🇳 もっとモンゴルを知ろう！")
st.write(
    "旅行記はここまでです！お疲れ様でした。最後に、モンゴルにまつわるクイズ全10問に挑戦してみませんか？"
)

# クイズページへ移動するボタン
st.page_link("pages/quiz.py", label="😃モンゴルクイズに挑戦する (全10問)")


# #おまけ
# #streamlit run main.pyでローカルで確認できる。
# #初期設定①git init, ②git remote add origin https:/// 
# #　①git add . ②git commit -m"◯◯◯" .　③git push origin main