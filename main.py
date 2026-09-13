import os
import time
import urllib.parse
import requests

# පින්තූර save කිරීමට 'images' නමින් ෆෝල්ඩරයක් සාදයි
os.makedirs("images", exist_ok=True)

print("Image generation started...")

for i in range(1, 51):
    try:
        # ඔබට අවශ්‍ය Prompt එක මෙහි ලබා දෙන්න
        # පින්තූර 50ම එක සමාන නොවීම සඳහා 'variation {i}' යන්න එකතු කර ඇත
        prompt = f"A beautiful futuristic city landscape, cinematic lighting, highly detailed, 8k, variation {i}"
        
        # URL එකට ගැලපෙන ලෙස Prompt එක සකස් කිරීම
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Pollinations AI URL (nologo=true මගින් watermark ඉවත් කරයි)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?nologo=true"

        # Image එක ලබා ගැනීම
        response = requests.get(url)
        
        if response.status_code == 200:
            # පින්තූරය 'images' ෆෝල්ඩරය තුළ save කිරීම
            with open(f"images/image_{i}.jpg", 'wb') as f:
                f.write(response.content)
            print(f"[{i}/50] Image {i} සාර්ථකව generate විය.")
        else:
            print(f"[{i}/50] Image {i} ලබාගැනීමට නොහැකි විය. Error Code: {response.status_code}")
            
        # ඊළඟ රූපය ලබාගැනීමට පෙර තත්පර 60ක් (විනාඩියක්) රැඳී සිටීම
        # අවසාන පින්තූරයට (50 වෙනි) පසුව රැඳී සිටීම අවශ්‍ය නොවේ
        if i < 50:
            time.sleep(60)

    except Exception as e:
        print(f"Error at image {i}: {e}")

print("සම්පූර්ණ ක්‍රියාවලිය සාර්ථකව අවසන්!")
