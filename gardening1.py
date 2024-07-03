import streamlit as st
import numpy as np

st.title("鉢花寄せ植え")

  
options = ["１-２月","３-４月","５-６月","７-８月","９-１０月","１１-１２月"]
sample_select = st.sidebar.selectbox('月を選択',options)
options = ["１-２月","３-４月","５-６月","７-８月","９-１０月","１１-１２月"]

st.write("オススメ草花")

if sample_select == "１-２月":
  images = ["panji.png","bakopa.png","shikuramen.png"]
  captions = ["パンジー","バコパ","シクラメン"]
elif sample_select == "３-４月":
  images = ["arissamu.png","magaretto.png","wasurenagusa.png"]
  captions =["アリッサム","マーガレット","忘れな草"]
elif sample_select == "５-６月":
  images = ["pechunia.png","burakikamu.png","inpachensu.png"]
  captions = ["ペチュニア","ブラキカム","インパチェンス"]
elif sample_select == "７-８月":
  images = ["burusuta.png","sukabiosa.png","cheriseji.png"]
  captions = ["ブルースター","スカビオサ","チェリーセージ"]
elif sample_select == "９-１０月":
  images = ["nadeshiko.png","kingyoso.png","hatsuyukikazura.png"]
  captions = ["なでしこ","金魚草","ハツユキカズラ"]  
elif sample_select == "１１-１２月":
  images = ["chekkaberry.png","habotan.png","purimura.png"]
  captions = ["チェッカーベリー","葉牡丹","プリムラ"]
  

else:
    img = "notfound.png"

# output


if images:
    st.image(images, width=200, caption=captions)

def main():
   
 if st.button("ポイント"):

# 月に応じて異なるコメントを表示する
    if sample_select == "１-２月":
     st.write("冬の寄せ植えを上手に作るコツは、寒さに強い植物を選ぶことです。 耐寒性のある花や葉色の美しいカラーリーフ植物を使えば、長期間楽しめます。また、鉢底の穴から水が抜けるよう土を入れ、日当たりと風通しの良い場所に置くことも大切です。")
    elif sample_select == '３-４月':
     st.write("春の先には、梅雨、夏と、植物にとっては過酷な季節が待ち受けています。せっかくならできるだけ長く晩秋まで楽しむことが出来るとお得感がありますよね。開花期間が長い春の植物して、ベゴニアやニチニチソウ、ゼラニウムなどもあげられます")
    elif sample_select == '５-６月':
     st.write("6月は雨やジメジメした日も多くなり、気分も憂鬱になりがちですよね。そんな6月には、シェードガーデン（日陰や半日陰の庭）を好み、日当たりでなくても美しく育つ草花を使って寄せ植えを作りましょう。")
    elif sample_select == '７-８月':
     st.write("8月は人間もぐったりするような暑い日が続きます。そんなときは、暑さに負けずに咲き続ける花や、高温多湿を好む観葉植物、丈夫で涼し気なカラーリーフを使って寄せ植えを作りましょう。")
    elif sample_select == '９-１０月':
     st.write("10月は秋がぐっと深まりとても涼しく過ごしやすくなります。秋の風情を感じる草花をゆったりした気持ちで育てたいですね。")
    elif sample_select == '１１-１２月':
     st.write("12月は寒さが本格的になり、寄せ植えに使える花の種類は少なくなりますが、ガーデンシクラメン、パンジー・ビオラなど冬の定番苗の品種が揃う月。クリスマスの寄せ植えもおすすめです。")

   

if __name__ == "__main__":
    main()

