import streamlit as st
import os
from PIL import Image
import random

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Our Story ❤️", layout="centered")

# ------------------ STYLE ------------------
st.markdown("""
<style>

/* ------------------ MAIN BACKGROUND ------------------ */
.stApp {
    background: 
        radial-gradient(circle at 20% 20%, rgba(255, 182, 193, 0.3), transparent 40%),
        radial-gradient(circle at 80% 80%, rgba(255, 105, 180, 0.2), transparent 40%),
        linear-gradient(135deg, #ffe6f0, #fff0f5);
    
    background-attachment: fixed;
    background-blend-mode: soft-light;
}

/* ------------------ HEADINGS ------------------ */
h1, h2, h3 {
    text-align: center;
    color: black;
}

/* ------------------ GENERAL TEXT ------------------ */
p, div {
    color: black !important;
}

/* ------------------ SIDEBAR ------------------ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffe6f0, #ffd6eb);
    padding: 15px;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: black !important;
    font-weight: 500;
}

/* Sidebar title */
section[data-testid="stSidebar"] h1 {
    color: #ff4da6 !important;
    text-align: center;
}

/* Sidebar radio buttons */
div[role="radiogroup"] label {
    position: relative;
    color: black !important;
    font-size: 16px;
    padding: 6px 10px;
    border-radius: 8px;
    transition: all 0.3s ease;
}

div[role="radiogroup"] label:hover {
    background-color: rgba(255, 105, 180, 0.2);
    color: #ff4da6 !important;

    box-shadow: 
        0 0 8px rgba(255, 105, 180, 0.4),
        0 0 15px rgba(255, 105, 180, 0.3),
        0 0 25px rgba(255, 182, 193, 0.3);

    transform: scale(1.05);
}

div[role="radiogroup"] label::after {
    content: "💖";
    position: absolute;
    right: 8px;
    opacity: 0;
    transform: scale(0.5);
    transition: all 0.3s ease;
}

div[role="radiogroup"] label:hover::after {
    opacity: 1;
    transform: scale(1);
}

/* ------------------ BUTTON ------------------ */
button {
    color: black !important;
}

/* 💌 Surprise button text white */
div.stButton > button:first-child p {
    color: white !important;
}

/* ------------------ LOVE CARD ------------------ */
.love-card {
    background: rgba(0, 0, 0, 0.85);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    margin-top: 25px;
    color: white !important;

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    border: 1px solid rgba(255, 182, 193, 0.4);

    box-shadow: 
        0 8px 30px rgba(255, 105, 180, 0.2),
        inset 0 0 10px rgba(255, 255, 255, 0.1);

    animation: fadeIn 2.5s ease-in;
}

.love-card p, 
.love-card b {
    color: white !important;
}

.love-text {
    white-space: pre-line;
    line-height: 1.8;
    font-size: 18px;
}

/* ------------------ IMAGE EFFECT ------------------ */
.image-card {
    position: relative;
    overflow: hidden;
    border-radius: 15px;
    cursor: pointer;
}

.image-card img {
    width: 100%;
    border-radius: 15px;
    transition: transform 0.4s ease;
}

.image-card:hover img {
    transform: scale(1.15);
}

.caption {
    position: absolute;
    bottom: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.9);
    color: black;
    padding: 10px;
    font-size: 14px;
    text-align: center;

    opacity: 0;
    transform: translateY(100%);
    transition: all 0.4s ease;
}

.image-card:hover .caption {
    opacity: 1;
    transform: translateY(0);
}

/* ------------------ BUTTON HEARTS ------------------ */
.button-hearts {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 9999;
}

.button-heart {
    position: absolute;
    bottom: 0;
    font-size: 20px;
    color: rgba(255, 105, 180, 0.7);
    animation: floatUpBtn 2s ease-out forwards;
}

@keyframes floatUpBtn {
    0% {
        transform: translateY(0) scale(1);
        opacity: 1;
    }
    100% {
        transform: translateY(-200px) scale(1.5);
        opacity: 0;
    }
}

/* ------------------ TITLE ------------------ */
.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: black;
    text-shadow: 0px 0px 10px rgba(255, 105, 180, 0.5);
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #444;
    margin-top: -10px;
}

/* ------------------ ANIMATION ------------------ */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* 🎮 Next Button Styling */
.next-btn button {
    background: linear-gradient(135deg, #ff4da6, #ff85c1) !important;
    color: white !important;
    border-radius: 25px !important;
    padding: 10px 20px !important;
    font-weight: bold;
    border: none;
    box-shadow: 0 5px 15px rgba(255, 105, 180, 0.4);
    transition: all 0.3s ease;
}

.next-btn button:hover {
    transform: scale(1.08);
    box-shadow: 0 8px 20px rgba(255, 105, 180, 0.6);
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEART FUNCTION ------------------
def show_button_hearts():
    placeholder = st.empty()

    hearts = '<div class="button-hearts">'
    for _ in range(12):
        hearts += f'<div class="button-heart" style="left:{random.randint(30,70)}%;">💖</div>'
    hearts += '</div>'

    placeholder.markdown(hearts, unsafe_allow_html=True)

# ------------------ IMAGE FOLDER ------------------
IMAGE_FOLDER = "assets/images"

def load_all_images():
    images = []
    if not os.path.exists(IMAGE_FOLDER):
        st.error("IMAGE FOLDER NOT FOUND ❌")
        return images

    for file in os.listdir(IMAGE_FOLDER):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            path = os.path.join(IMAGE_FOLDER, file)
            images.append((file, Image.open(path)))
    return images

images = load_all_images()

# ------------------ SIDEBAR ------------------
st.sidebar.title("Navigate 💖")
page = st.sidebar.radio("Navigation 💖", ["Home", "Gallery", "Letter 💌", "Story Mode", "Mini Game 💖", "Reasons 💖", "Forever? 💍"])

import streamlit.components.v1 as components

# ✅ session states
if "started" not in st.session_state:
    st.session_state.started = False

if "proposal_answer" not in st.session_state:
    st.session_state.proposal_answer = None

# 🎵 page-based music
def get_music(page):
    if page == "Home":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777090428/Tum_Mere_Ho_Hate_Story_Iv_128_Kbps_wjxpyo.mp3"
    elif page == "Gallery":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777091749/02_-_Samjhawan_-_HSKD_2014_fsmb8s.mp3"
    elif page == "Story Mode":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777112091/Sitaare_PenduJatt.Com.Se_qmj82t.mp3"
    elif page == "Mini Game 💖":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777116083/Tum_Se_Hi_Jab_We_Met_128_Kbps_lztgva.mp3"
    elif page == "Letter 💌":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777136823/Meri_Aashiqui_Aashiqui_2_128_Kbps_capoz6.mp3"
    elif page == "Reasons 💖":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777129749/Lae_Dooba_by_Sunidhi_Chauhan_-_Aiyaary_128_kbps_mqhqbn.mp3"
    elif page == "Forever? 💍":
        return "https://res.cloudinary.com/dk7ymleso/video/upload/v1777210022/Raabta_Title_Track_-_Arijit_Singh_Nikita_Gandhi_DJJOhAL.Com_ltutmk.mp3"
    else:
        return ""

# 💍 override music when YES is clicked
if page == "Forever? 💍" and st.session_state.proposal_answer == "yes":
    music_url = "https://res.cloudinary.com/dk7ymleso/video/upload/v1777212349/Tu_Mileya_-_Darshan_Raval_dh7tsl.mp3"
else:
    music_url = get_music(page)

# 🎶 PLAY ONLY AFTER ENTER
if st.session_state.started:
    components.html(f"""
    <audio autoplay loop id="bg-music" style="display:none;">
        <source src="{music_url}" type="audio/mp3">
    </audio>
    """, height=0)

# ------------------ HOME ------------------
if page == "Home":

    if not st.session_state.started:

        st.markdown("""
        <h1 class='fade-in heartbeat' style='
            text-align:center;
            font-size:42px;
            font-weight:bold;
            color:#000;
            text-shadow: 
                0 0 8px rgba(255,105,180,0.6),
                0 0 15px rgba(255,105,180,0.4),
                0 0 25px rgba(255,182,193,0.3);
            letter-spacing:1px;
        '>
            Welcome Chiku 💖
        </h1>
        """, unsafe_allow_html=True)

        st.markdown("<p style='color:black; font-size:18px; text-align:center;'>Are you ready to enter this little journey of love?</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:black; text-align:center;'>A place where every memory, every smile, and every moment of us lives forever ❤️</p>", unsafe_allow_html=True)
        st.markdown("<p style='color:#444; font-style:italic; text-align:center;'>Every click ahead holds a piece of us… 💫</p>", unsafe_allow_html=True)

        import time

        typing_placeholder = st.empty()
        text = "Before you click… just know, every moment inside was made with love 💖"

        typed = ""
        for char in text:
            typed += char
            typing_placeholder.markdown(f"""
            <div style="
                text-align:center;
                font-size:16px;
                color:#444;
                font-style:italic;
            ">
            {typed}|
            </div>
            """, unsafe_allow_html=True)
            time.sleep(0.03)

        typing_placeholder.markdown(f"""
        <div style="
            text-align:center;
            font-size:16px;
            color:#444;
            font-style:italic;
        ">
        {text}
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button("Enter ❤️"):
            st.session_state.started = True
            st.rerun()

        st.stop()

    else:

        st.markdown('<div class="title">Our Story ❤️</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle">A journey of love, memories & moments ✨</div>', unsafe_allow_html=True)

        if images:
            st.image(images[0][1], use_container_width=True)
        else:
            st.error("No images found")

        st.markdown("""
        <div class="love-card">
            <p class="love-text">
Dear Chiku,

It's been a year together... we've sailed through so many storms,
and I know we'll keep doing the same forever and ever.

This is just a small gesture from my side,
to take you through our beautiful journey of 365 days ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)

        if "show_surprise" not in st.session_state:
            st.session_state.show_surprise = False

        if st.button("Click for a Surprise 💌"):
            show_button_hearts()
            st.session_state.show_surprise = True
            st.rerun()

        if st.session_state.show_surprise:
            st.markdown("""
            <div style="
                background-color: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
                text-align: center;
            ">
                <h2 style="color:black;">💖 Surprise 💖</h2>
                <p style="color:black;">
                You are the best thing that ever happened to me ❤️<br>
                Every moment with you is magic ✨<br><br>
                I love you forever 💕
                </p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Close ❌"):
                show_button_hearts()
                st.session_state.show_surprise = False
                st.rerun()

# ------------------ GALLERY ------------------
elif page == "Gallery":

    st.markdown('<h2 style="color:black; text-align:center;">Our Memories 📸</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:#444;
        font-size:16px;
        margin-top:-10px;
        margin-bottom:15px;
        font-style:italic;
    ">
    Every picture here holds a piece of us…  
    a moment I wish I could pause forever 💖
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .image-card {
        position: relative;
        overflow: hidden;
        border-radius: 18px;
        margin: 18px 12px;
        box-shadow: 
            0 8px 20px rgba(255, 182, 193, 0.25),
            0 0 15px rgba(255, 192, 203, 0.15);
        transition: transform 0.4s ease, box-shadow 0.4s ease;
    }

    .image-card img {
        width: 100%;
        border-radius: 18px;
        transition: transform 0.4s ease;
    }

    .image-card:hover img {
        transform: scale(1.08);
    }

    .image-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 
            0 15px 35px rgba(255, 105, 180, 0.45),
            0 0 30px rgba(255, 182, 193, 0.5),
            0 0 60px rgba(255, 192, 203, 0.35);
    }

    .caption {
        position: absolute;
        bottom: 0;
        width: 100%;
        padding: 10px;
        background: linear-gradient(
            to top,
            rgba(255, 255, 255, 0.95),
            rgba(255, 255, 255, 0.7),
            transparent
        );
        color: #222;
        font-size: 14px;
        font-style: italic;
        text-align: center;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.4s ease;
    }

    .image-card:hover .caption {
        opacity: 1;
        transform: translateY(0);
    }
    </style>
    """, unsafe_allow_html=True)

    if not images:
        st.error("No images found ❌")
    else:
        cols = st.columns(3)

        messages = [
            "The moment everything began ❤️",
            "A memory I wish I could hold forever 🥺",
            "Your smile… still melts my heart 😊",
            "This moment lives in my heart ✨",
            "You looked so perfect here 💖",
            "One of my happiest days with you 💫",
            "I'd relive this a thousand times 💕",
            "Your happiness is my world 😍",
            "This felt like pure magic ✨",
            "With you… anywhere feels like home ❤️",
            "We were so lost in happiness 🥰",
            "A moment I'll cherish forever 💖",
            "Just us… always 💫❤️"
        ]

        for i, (name, img) in enumerate(images):
            with cols[i % 3]:

                import base64
                from io import BytesIO

                buffered = BytesIO()
                img.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()

                message = messages[i] if i < len(messages) else "A memory I'll always cherish ❤️"

                st.markdown(f"""
                <div class="image-card">
                    <img src="data:image/png;base64,{img_str}">
                    <div class="caption">{message}</div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div style="
            text-align:center;
            margin-top:25px;
            font-size:15px;
            color:#555;
            font-style:italic;
        ">
        And somehow… every memory still feels like the beginning 💕
        </div>
        """, unsafe_allow_html=True)

# ------------------ STORY MODE ------------------
elif page == "Story Mode":

    import time

    st.markdown('<h2 style="color:black; text-align:center;">Our Story 📖</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:#444;
        font-size:16px;
        margin-bottom:20px;
        font-style:italic;
    ">
    Not just memories… but moments that shaped us 💖<br>
    Click each chapter to relive it ✨
    </div>
    """, unsafe_allow_html=True)

    chapters = [
        ("ch1", "Chapter 1: The Fish Pond Episode (Part 1)", """There comes a boy handsome boy dressed in white shirt and blue jeans and a girl dressed in all black!! The boy was calm as wind and the girl was quick as squirrel!! Omg!! The girl had a thought how did I met such a handsome boy!! Both of them started talking and it was a happy meet up.. but there was something untold inside both of them .."""),

        ("ch2", "Chapter 2: The Fish Pond Story (Part 2)", """Next day they met again.. and the boy confessed!! That he has been liking that girl since last 1 year.. The girl also had something to tell but her past wounds didn't let her say that!! but the aura made her say 'Yes!!' The boy's happiness was on 7th cloud but the girl had that fear inside her that she'll get wounded again.."""),

        ("ch3", "Chapter 3 : Happy Days", """Just like that the boy and the girl started meeting daily, had long convos, looked at stars and what not!! The girl had a feeling that when people will get to about this they'll make fun of her so this fact was hidden from every one!! But she started healing day by day and every moment felt like heaven to her!!"""),

        ("ch4", "Chapter4: First Date 3rd Aug 2025", """The boy asked her for a date and she said 'Yes!!' Both of them were happy and the day was spent so well doing jungle hoppings, cafe dates and clicking pictures. She never enjoyed this much with anyone like that and her happiness was finally on 9th cloud that she actually got someone who's there with her without anything in return."""),

        ("ch5", "Chapter 5: A Big Wave of Ocean", """The girl was so in love that she even forgot that what if every one comes to know about it .. What if the boy comes to know about it!! So she tried going away from him on her own but she couldn't because the love was so strong that it didn't let her do so .. But then came a wave of ocean and everything was destroyed because the boy got to know about all this!! The boy was hurt badly and couldn't recover and decided to go away!!"""),

        ("ch6", "Chapter6: The Strong Bond", """Everything was almost finished!! Because now when the girl realised that she was actually in love the boy was leaving.. But inside she knew that they had a strong bond.. and hence she was given a chance and they united again!!"""),

        ("ch7", "Chapter7: A bigger wave", """Again came a bigger wave when the girl did the biggest blunder by having convo with someone else taking that to be really casual but the boy was hurt again infact in the worst way!! This time both of them thought everything to be over!! "kabhii kuch khatam hosakta h??" Ofc not!! They united on one last chance and this time the bond was stronger !!"""),

        ("ch8", "Chapter 8: Not the last one!!", """The love between them got unbreakable and even stronger!! May it be long distance or short one.. The love remained same But the girl still has this question inside her that if she had done something good to someone that she got this boy as the besstttttt gift of her life and she still keeps thanking God for this best gift of her her life""")
    ]

    for key, title, text in chapters:

        if key not in st.session_state:
            st.session_state[key] = False

        if f"{key}_done" not in st.session_state:
            st.session_state[f"{key}_done"] = False

        if st.button(f"🔒 {title}", key=key+"_btn"):
            st.session_state[key] = True

        if st.session_state[key]:

            if not st.session_state[f"{key}_done"]:

                placeholder = st.empty()

                placeholder.markdown("""
                <div style="text-align:center; color:#555; font-size:15px;">
                    unlocking memories... 💫
                </div>
                """, unsafe_allow_html=True)

                time.sleep(1.2)
                placeholder.empty()

                typed_text = ""
                type_placeholder = st.empty()

                for char in text:
                    typed_text += char

                    type_placeholder.markdown(f"""
                    <div style="
                        background: rgba(255,255,255,0.6);
                        padding: 22px;
                        border-radius: 20px;
                        margin-bottom: 18px;
                        backdrop-filter: blur(10px);
                        box-shadow: 0 10px 25px rgba(255,105,180,0.25);
                        line-height: 1.7;
                    ">
                        <h3 style="color:#ff4da6;">{title}</h3>
                        <p style="color:black; font-size:16px;">{typed_text}|</p>
                    </div>
                    """, unsafe_allow_html=True)

                    time.sleep(0.015)

                type_placeholder.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.6);
                    padding: 22px;
                    border-radius: 20px;
                    margin-bottom: 18px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 10px 25px rgba(255,105,180,0.25);
                    line-height: 1.7;
                ">
                    <h3 style="color:#ff4da6;">{title}</h3>
                    <p style="color:black; font-size:16px;">{text}</p>
                </div>
                """, unsafe_allow_html=True)

                st.session_state[f"{key}_done"] = True

            else:
                st.markdown(f"""
                <div style="
                    background: rgba(255,255,255,0.6);
                    padding: 22px;
                    border-radius: 20px;
                    margin-bottom: 18px;
                    backdrop-filter: blur(10px);
                    box-shadow: 0 10px 25px rgba(255,105,180,0.25);
                    line-height: 1.7;
                ">
                    <h3 style="color:#ff4da6;">{title}</h3>
                    <p style="color:black; font-size:16px;">{text}</p>
                </div>
                """, unsafe_allow_html=True)

    if st.session_state.get("ch8", False):
        st.markdown("""
        <div style="
            text-align:center;
            font-size:18px;
            color:#ff4da6;
            margin-top:30px;
            font-style:italic;
        ">
        ...and many more chapters are still being written 💖
        </div>
        """, unsafe_allow_html=True)

# ------------------ MINI GAME ------------------
elif page == "Mini Game 💖":

    st.markdown('<h2 style="text-align:center;">Mini Game 💖</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:#444;
        font-size:16px;
        margin-bottom:20px;
        font-style:italic;
    ">
    Let's see how well you remember our moments 🥺✨
    </div>
    """, unsafe_allow_html=True)

    questions = [
        {"q": "Where did we had our first convo? 💫",
         "options": ["Fish Pond 🐟", "Library 📚", "Cafeteria ☕"],
         "answer": "Fish Pond 🐟"},

        {"q": "What was our first date vibe? 💖",
         "options": ["Movie 🎬", "Cafe + Jungle hopping 🌿", "Shopping 🛍️"],
         "answer": "Cafe + Jungle hopping 🌿"},

        {"q": "What made us strongest? 💕",
         "options": ["Fights 💔", "Understanding ❤️", "Distance 🌍"],
         "answer": "Understanding ❤️"},

        {"q": "Who fell first? 👀",
         "options": ["Chikuu 😌", "Shubhu 😏", "Both 💕"],
         "answer": "Chikuu 😌"},

        {"q": "Who fell harder? 🥺",
         "options": ["Shubhu 💖", "Chiku 💙", "Both 💕"],
         "answer": "Shubhu 💖"},

        {"q": "What defines us best? 💫",
         "options": ["Chaos 😝", "Love ❤️", "Drama 🎭"],
         "answer": "Love ❤️"},

        {"q": "Our bond is like? 🌈",
         "options": ["Temporary 💔", "Strong & unbreakable 💖", "Confusing 😵"],
         "answer": "Strong & unbreakable 💖"}
    ]

    if "current_q" not in st.session_state:
        st.session_state.current_q = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "answered" not in st.session_state:
        st.session_state.answered = False

    if st.session_state.current_q >= len(questions):

        st.balloons()

        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.7);
            padding: 30px;
            border-radius: 25px;
            text-align:center;
            box-shadow: 0 10px 30px rgba(255,105,180,0.3);
        ">
            <h2 style="color:#ff4da6;">🎉 Congratulations 🎉</h2>
            <h3 style="color:black;">You are the Champion 💖</h3>
            <p style="font-size:18px;">
                You scored <b>{st.session_state.score}</b> out of <b>{len(questions)}</b> 🥺✨
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Play Again 💫"):
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.rerun()

    else:

        q_data = questions[st.session_state.current_q]

        st.markdown(f"""
        <div style="
            background: rgba(255,255,255,0.6);
            padding: 20px;
            border-radius: 20px;
            text-align:center;
            margin-bottom:20px;
            box-shadow: 0 8px 20px rgba(255,105,180,0.2);
        ">
            <h3>{q_data["q"]}</h3>
        </div>
        """, unsafe_allow_html=True)

        for opt in q_data["options"]:
            if st.button(opt):

                if not st.session_state.answered:

                    if opt == q_data["answer"]:
                        st.success("Awww you remember it perfectly 🥺💖")
                        st.session_state.score += 1
                    else:
                        st.error("Hehe wrong 😝 but still cute 💕")

                    st.session_state.answered = True

        if st.session_state.answered:
            if st.button("Next 💫", type="primary", use_container_width=True):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.rerun()

# ------------------ REASONS SECTION ------------------
elif page == "Reasons 💖":

    import time

    st.markdown('<h2 style="text-align:center;">Hidden Pieces of My Heart 💖</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:#444;
        font-size:16px;
        margin-bottom:20px;
        font-style:italic;
    ">
    Not everything is visible… some love is meant to be discovered 🥺✨
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .egg-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .egg {
        width: 80px;
        height: 100px;
        background: radial-gradient(circle at 30% 30%, #fff, #ffc0cb);
        border-radius: 50% 50% 45% 45%;
        box-shadow: 0 5px 15px rgba(255,105,180,0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        font-size: 22px;
    }

    .egg:hover {
        transform: scale(1.15) rotate(5deg);
        box-shadow: 0 10px 25px rgba(255,105,180,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

    reasons = [
        "The way you understand me without words 🥺",
        "Your smile that makes everything better 😊",
        "How safe I feel with you 💖",
        "The way you care even in small things 🌸",
        "Your voice… my favorite sound 🎶",
        "The way you handle everything so calmly 💫",
        "How you never give up on us ❤️",
        "Your little efforts that mean everything 🥹",
        "The way you love me… it's different 💕",
        "Because it's YOU… always you 💖"
    ]

    if "revealed" not in st.session_state:
        st.session_state.revealed = []

    if "current_msg" not in st.session_state:
        st.session_state.current_msg = ""

    if "final_done" not in st.session_state:
        st.session_state.final_done = False

    clicked = st.button("🥚", key="egg_btn")

    st.markdown("""
    <div class="egg-container">
        <div class="egg">🥚</div>
    </div>
    """, unsafe_allow_html=True)

    hints = [
        "Tap the egg 💖",
        "Another secret awaits… 🥺",
        "One more piece of my heart 💌",
        "You're getting closer… ✨"
    ]

    st.markdown(
        f"<p style='text-align:center; color:#555;'>{random.choice(hints)}</p>",
        unsafe_allow_html=True
    )

    if clicked:
        remaining = list(set(reasons) - set(st.session_state.revealed))

        if remaining:
            msg = random.choice(remaining)
            st.session_state.revealed.append(msg)
            st.session_state.current_msg = msg
        else:
            st.session_state.current_msg = ""

    if st.session_state.current_msg:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #fff, #ffe6f0);
            padding: 20px;
            border-radius: 25px;
            margin-top:20px;
            text-align:center;
            box-shadow: 0 10px 25px rgba(255,105,180,0.3);
            font-size:17px;
            animation: fadeIn 0.6s ease-in;
        ">
            💖 {st.session_state.current_msg}
        </div>
        """, unsafe_allow_html=True)

    if len(st.session_state.revealed) == len(reasons):

        if not st.session_state.final_done:

            placeholder = st.empty()
            final_text = "You've unlocked everything… but my love for you is still infinite 💖"

            typed = ""

            for char in final_text:
                typed += char

                placeholder.markdown(f"""
                <div style="
                    text-align:center;
                    margin-top:30px;
                    font-size:18px;
                    color:#ff4da6;
                    font-style:italic;
                ">
                    {typed}|
                </div>
                """, unsafe_allow_html=True)

                time.sleep(0.03)

            placeholder.markdown(f"""
            <div style="
                text-align:center;
                margin-top:30px;
                font-size:18px;
                color:#ff4da6;
                font-style:italic;
            ">
                {final_text}
            </div>
            """, unsafe_allow_html=True)

            st.session_state.final_done = True

        else:
            st.markdown("""
            <div style="
                text-align:center;
                margin-top:30px;
                font-size:18px;
                color:#ff4da6;
                font-style:italic;
            ">
            You've unlocked everything… but my love for you is still infinite 💖
            </div>
            """, unsafe_allow_html=True)

# ------------------ LETTER SECTION ------------------
elif page == "Letter 💌":

    import time
    import streamlit.components.v1 as components

    st.markdown('<h2 style="text-align:center;">A Letter For You 💌</h2>', unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:#444;
        font-size:16px;
        margin-bottom:20px;
        font-style:italic;
    ">
    Not everything can be said in moments… some things deserve a letter 💖
    </div>
    """, unsafe_allow_html=True)

    if "open_letter" not in st.session_state:
        st.session_state.open_letter = False

    if not st.session_state.open_letter:

        st.markdown("""
        <style>
        .envelope-wrapper {
            text-align:center;
            margin-top:40px;
        }

        .envelope {
            width: 240px;
            height: 150px;
            background: #ffc2d1;
            position: relative;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.25);
            cursor: pointer;
            overflow: hidden;
        }

        .flap {
            width: 0;
            height: 0;
            border-left: 120px solid transparent;
            border-right: 120px solid transparent;
            border-bottom: 75px solid #ff8fab;
            position: absolute;
            top: -75px;
            left: 0;
            transform-origin: bottom;
            animation: flapClose 0.6s forwards;
        }

        .tear-line {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: repeating-linear-gradient(
                90deg,
                #ff4d6d,
                #ff4d6d 6px,
                transparent 6px,
                transparent 12px
            );
            opacity: 0.7;
        }

        .open .flap {
            animation: tearOpen 0.8s forwards;
        }

        @keyframes tearOpen {
            0% { transform: rotateX(0deg); }
            50% { transform: rotateX(120deg); }
            100% { transform: rotateX(180deg); }
        }

        .envelope-text {
            margin-top:12px;
            color:#555;
            font-style:italic;
        }
        </style>

        <div class="envelope-wrapper">
            <div class="envelope open">
                <div class="tear-line"></div>
                <div class="flap"></div>
            </div>
            <div class="envelope-text">Click to open your letter 💌</div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Open Letter 💌"):
            st.session_state.open_letter = True
            st.rerun()

    else:

        st.markdown("""
        <div style="
        text-align:center;
        font-size:14px;
        color:#777;
        margin-bottom:10px;
        font-style:italic;
        ">
        ✉️ Opening something written straight from the heart...
        </div>
        """, unsafe_allow_html=True)

        letter_text = """If I had to explain what you mean to me,
I don’t think words would ever be enough…

But still, I’ll try.

You came into my life so unexpectedly,yet somehow, you became the most important part of it. 
I never thought that my wounds would ever recover and not even my closest ones helped me with it but Ig Bhagwanjiee ko na 
taras aagyii mujpar and unhone mereliyy tumhee bhejdiya.. Seriously aaj bhii maii maii Bhagwanjiee ko daily THANKYOU bolti hu
tumhee merii life ek ahem hissa banane k liyee!! Mujhe ajj bhii yaad haii the Day we met I didn't even had clue ki jis ladki k 
liyee shayrii likhi jaa raii thii wo maii hi huu😂😂.. Par literally jab mujhe pata chala na ki tum mujhse pyar karte ho pasand 
karte ho mere dimag me na yahinn sawal aur yahin dar thaa ki dekhna pakka ye bhii chala jaega mujhee chor k but din din bita aur 
jaise mere saree ghaww bhar gyy maii sab bhulne lagii thii..Trust me!! But fr ekdum se ek din dhakka laga aur man me ye aayaa ki 
maii kyun tumhe dukh de raii hu indirectly in sab baaton se anjaan rakhkar..isiliyy khud tumse door jane ki koshish karne lagii..
lekin maii nakam rahii qkii mujhse nii hoapaya!! Aur frr kyaa huaa??
Haan mere sare ghaw to theek hogyy tumhree sath but is karan maine tumhee gehra ghaww dediya jisse shayd tum ajj bhii nii nikal paee 
hoo.. chance milne k baad bhii maine wahinn kiyaa!!  
Chikuu galtiyan mujhse humesha anjane me huii hainn kabhii bhii tumhee hurt karne k iraadee se nii kii thii .. agar mere bus me hota 
na too maii bhii time travel kar k sabb khatam kar detii!! Haan agar aagee aayaa to zarur karungi Lekin aisa kuch nii haii abhii takk
to bus tumse hath jod k tumhree pair pad k SORRY hi keh saktii hu!!🙏🏻🙏🏻
Baby I don't know ki aagee humari life me kyaa problems aayengii but I gurantee thiss ki maii har phase me tumhree sath rahungii.. aur
tumse bhii bus yahin request haii ki chahe lakh jhagde ho jaenn lakh musibatein aajaee gussa hona buss 'chor k na jana!!🙏🏻🙏🏻' qkii jis 
din aisa huaa na us din maii khatam hojaungii!!

Pyar karna nibhana tumne sikhaya haii to bus ab usee end tak maii niibhaungii.. Humarii shadii hogii bachhe honge maii tumhree mummy papa
ki sewaa karungii ye sabb soch k hi man khush hojata haii and trust me this is the only motto left for me!! qkii aur kuch bacha hi nii haii
merii life me!! qkii 'merii aashiqui abb tum hii ho'🧿🧿
You are not just someone I love…
you are my comfort, my safe place, my happiness.
And no matter what happens,
one thing will always remain constant—
my love for you 💖
Ab handwritten letters to bohut dii isliyy is baar aise de raii huu..
I looooooveeeeee youuuuuuuuuu thee mossstttttttesstttt chikuuuu 😘😘🧿🧿
HAPPY ONE YEAR ANNEVERSARY BABY!!

With loads of huggies and kisses 
Yours and only yours and also forever yours


Shubhu
"""

        placeholder = st.empty()
        typed = ""

        for char in letter_text:
            typed += char

            placeholder.markdown(f"""
<div style="background: linear-gradient(135deg, #fffafc, #ffeef5);
padding: 35px;
border-radius: 20px;
line-height: 1.9;
font-size:17px;
box-shadow: 0 10px 30px rgba(255,105,180,0.2);
backdrop-filter: blur(6px);
border-left: 6px solid #ff4da6;
font-family: Georgia, serif;
position: relative;">

<div style="position:absolute; top:10px; right:20px; font-size:14px; color:#999; font-style:italic;">
💌 handwritten with love
</div>

{typed}|
</div>
""", unsafe_allow_html=True)

            time.sleep(0.02)

        placeholder.markdown(f"""
<div style="background: linear-gradient(135deg, #fffafc, #ffeef5);
padding: 35px;
border-radius: 20px;
line-height: 1.9;
font-size:17px;
box-shadow: 0 10px 30px rgba(255,105,180,0.2);
backdrop-filter: blur(6px);
border-left: 6px solid #ff4da6;
font-family: Georgia, serif;
position: relative;">

<div style="position:absolute; top:10px; right:20px; font-size:14px; color:#999; font-style:italic;">
💌 handwritten with love
</div>

{letter_text}
</div>
""", unsafe_allow_html=True)

        # 💖 FINAL WORKING NEVER-ENDING HEARTS
        components.html("""
<style>
#heart-container {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 999999;
}
</style>

<div id="heart-container"></div>

<script>
const container = document.getElementById("heart-container");

function createHeart() {
    const heart = document.createElement("div");
    heart.innerHTML = "💖";

    heart.style.position = "absolute";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.bottom = "-20px";
    heart.style.fontSize = (16 + Math.random() * 20) + "px";
    heart.style.opacity = Math.random();
    heart.style.transition = "transform 4s linear, opacity 4s linear";

    container.appendChild(heart);

    setTimeout(() => {
        heart.style.transform = "translateY(-110vh)";
        heart.style.opacity = "0";
    }, 50);

    setTimeout(() => {
        heart.remove();
    }, 4000);
}

setInterval(createHeart, 250);
</script>
""", height=800)

# ------------------ FOREVER (PROPOSAL) ------------------
elif page == "Forever? 💍":

    if "proposal_answer" not in st.session_state:
        st.session_state.proposal_answer = None

    if "no_clicks" not in st.session_state:
        st.session_state.no_clicks = 0

    st.markdown("""
    <style>
    .proposal-box {
        background: linear-gradient(135deg, #fff0f5, #ffe6f0);
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255,105,180,0.25);
        animation: fadeIn 1.5s ease-in;
    }

    .proposal-text {
        font-size: 26px;
        font-weight: bold;
        color: #222;
        animation: heartbeat 1.5s infinite;
    }

    @keyframes heartbeat {
        0% { transform: scale(1); }
        25% { transform: scale(1.05); }
        50% { transform: scale(1); }
        75% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }

    .romantic-line {
        color: #555;
        font-style: italic;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="romantic-line" style="text-align:center;">
    Every moment with you led me here… 💫
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="proposal-box">
        <div class="proposal-text">
            Will you be mine forever? 💍
        </div>
        <br>
        <div style="color:#444;">
            Not just today… not just tomorrow…<br>
            but in every lifetime, every world, every moment ❤️
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Yes 💖"):
            st.session_state.proposal_answer = "yes"
            show_button_hearts()
            st.rerun()

    with col2:
        if st.button("No 😢"):
            st.session_state.no_clicks += 1

    no_msgs = [
        "Are you really sure? 🥺",
        "Think once more… my heart is waiting 💔",
        "I'll still choose you… every time ❤️",
        "Running away won't help 😏",
        "Bas ab Yes hi dabana padega 💖"
    ]

    if st.session_state.no_clicks > 0:
        idx = min(st.session_state.no_clicks - 1, len(no_msgs) - 1)
        st.markdown(f"<p style='text-align:center; color:#ff4d6d; font-weight:bold;'>{no_msgs[idx]}</p>", unsafe_allow_html=True)

    if st.session_state.proposal_answer == "yes":
        st.markdown("""
        <div style='
            text-align:center;
            font-size:26px;
            margin-top:25px;
            color:#ff4d88;
            animation: fadeIn 2s ease-in;
        '>
        💍 He said YES! 💖✨<br><br>
        And just like that…<br>
        our forever begins again!! This song is for youu!! ❤️
        </div>
        """, unsafe_allow_html=True)

        show_button_hearts()