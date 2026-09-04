import streamlit as st
import os

# 1. पेज की पूरी प्रीमियम VLVIP सेटिंग (मोबाइल स्क्रीन पर स्क्रॉल बार छिपाने के लिए)
st.set_page_config(page_title="Happy Janmashtami!", page_icon="🪈", layout="centered")

# 2. एडवांस CSS: हेडिंग, फोटो बॉर्डर और नीचे के कोट्स—सब कुछ 100% लाइव एनिमेटेड और नियॉन ग्लो
custom_css = """
<style>
    /* ऐप का शानदार डार्क और मॉडर्न फेस्टिव बैकग्राउंड */
    .stApp {
        background: linear-gradient(135deg, #090014 0%, #15002a 50%, #26004d 100%) !important;
        color: #ffffff;
        overflow: hidden !important;
    }
    
    /* मुख्य कंटेनर: नाम ऊपर से न कटे इसलिए padding-top को 2.5rem रखा है */
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 0rem !important;
        max-width: 450px !important;
    }

    /* सबसे ऊपर दिखने वाला डबल नाम और पूरा सही वाक्य (PRABHAT की तरफ से NANDANI को...) */
    .vip-sender-box {
        text-align: center;
        margin-top: 10px;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .vip-name {
        font-family: 'Georgia', serif;
        font-size: 1.9rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #FFD700, #ffaa00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(255, 170, 0, 0.6);
        display: inline-block;
    }
    .vip-receiver-name {
        font-family: 'Georgia', serif;
        font-size: 1.9rem;
        font-weight: bold;
        text-transform: uppercase;
        background: linear-gradient(45deg, #00ffcc, #00bbff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 0px 15px rgba(0, 255, 204, 0.6);
        display: inline-block;
    }
    .vip-sender-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: bold;
        letter-spacing: 1px;
        text-shadow: 0px 0px 8px rgba(255, 255, 255, 0.3);
    }
    
    /* मुख्य हेडिंग जो धीरे-धीरे चमकते हुए अपना रंग बदलेगी */
    .main-title {
        font-family: 'Georgia', serif;
        text-align: center;
        font-size: 2.3rem;
        font-weight: bold;
        letter-spacing: 1px;
        margin-top: 5px;
        margin-bottom: 8px;
        background: linear-gradient(to right, #ff007f, #FFD700, #00ffcc, #ff007f);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 4s linear infinite, headingGlow 2s ease-in-out infinite alternate;
    }
    
    @keyframes textShine {
        0% { background-position: 0% center; }
        100% { background-position: 200% center; }
    }
    
    @keyframes headingGlow {
        0% { filter: drop-shadow(0 0 5px rgba(255, 0, 127, 0.6)); }
        100% { filter: drop-shadow(0 0 15px rgba(255, 215, 0, 0.8)); }
    }
    
    /* इमेज के चारों तरफ का वीआईपी नियॉन बॉर्डर जो लगातार अपनी चमक और रंग बदलेगा */
    .stImage img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-height: 265px !important;
        width: auto !important;
        border-radius: 20px !important;
        border: 2px solid rgba(255, 0, 127, 0.4) !important;
        animation: superFloat 4s ease-in-out infinite, photoGlow 3s ease-in-out infinite alternate !important;
    }

    /* नीचे का शुभकामनाएं बॉक्स जिसके टेक्स्ट अब सोने की लहर की तरह लाइव चमकेंगे */
    .wishes-container {
        background: rgba(255, 255, 255, 0.04);
        border-radius: 15px;
        padding: 12px;
        margin-top: 15px;
        border: 1px solid rgba(255, 0, 127, 0.15);
        box-shadow: 0px 0px 15px rgba(153, 0, 255, 0.15);
        text-align: center;
    }

    .wish-text {
        font-family: 'Georgia', serif;
        color: #ffffff;
        font-size: 1.05rem;
        line-height: 1.6;
        margin-bottom: 8px;
        background: linear-gradient(to right, #ffffff, #FFD700, #00ffcc, #ffffff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 5s linear infinite;
    }
    
    .wish-highlight {
        font-weight: bold;
        background: linear-gradient(to right, #FFD700, #ff6600, #FFD700);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: textShine 3s linear infinite;
    }

    @keyframes photoGlow {
        0% { box-shadow: 0px 0px 15px #ff007f, 0px 0px 5px #9900ff !important; }
        100% { box-shadow: 0px 0px 35px #FFD700, 0px 0px 15px #ff6600 !important; }
    }

    @keyframes superFloat {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 3. जादुई डबल नाम बदलने वाला कोड (URL Parameters)
query_params = st.query_params
sender = query_params.get("name", "")
receiver = query_params.get("to", "") # यह नया डिब्बा (Variable) पाने वाले के नाम के लिए है

# 4. स्क्रीन पर सबसे ऊपर डबल नाम का पूरा सही वाक्य चमकेगा
if sender and receiver:
    st.markdown(
        f"""
        <div class="vip-sender-box">
            <span class="vip-name">🎉 {sender} 🎉</span><br>
            <span class="vip-sender-text">की तरफ से</span><br>
            <span class="vip-receiver-name">💖 {receiver} 💖</span><br>
            <span class="vip-sender-text">को हैप्पी जन्माष्टमी</span>
        </div>
        """, 
        unsafe_allow_html=True
    )
elif sender:
    # अगर सिर्फ भेजने वाले का नाम हो, तो पुराना वाक्य दिखेगा
    st.markdown(
        f"""
        <div class="vip-sender-box">
            <span class="vip-name">🎉 {sender} 🎉</span><br>
            <span class="vip-sender-text">की तरफ से आपको हैप्पी जन्माष्टमी</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

# 5. मुख्य हेडिंग
st.markdown("<h1 class='main-title'>✨ Happy Janmashtami ✨</h1>", unsafe_allow_html=True)

# 6. आपकी वही असली सुंदर फोटो 'images (52).jpeg'
image_path = "images (52).jpeg"

if os.path.exists(image_path):
    st.image(image_path, use_container_width=False)
else:
    st.warning("कृपया पेज को एक बार रिफ्रेश करें।")

# 7. नीचे का शुभकामनाएं बॉक्स
st.markdown(
    """
    <div class="wishes-container">
        <p class="wish-text">🌸 माखन चोर नन्द किशोर, बांधे जिसने प्रीत की डोर... <span class="wish-highlight">हरे कृष्णा! 🪈</span></p>
        <p class="wish-text">✨ श्री कृष्ण के कदम आपके घर आएं, आप खुशियों के दीप जलाएं! <span class="wish-highlight">शुभ जन्माष्टमी 🦚</span></p>
        <p class="wish-text" style="font-size: 0.95rem; color: #00ffcc; margin-bottom: 0;">May Lord Krishna fill your life with Love, Peace, and Happiness! 🌟</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# 8. आसमान से चमकीले सितारों की बारिश
st.snow()
