import os
import requests
import urllib.parse

def main():
    # prompts.txt ගොනුව කියවීම
    if not os.path.exists("prompts.txt"):
        print("prompts.txt ගොනුව සොයාගත නොහැක!")
        return

    with open("prompts.txt", "r", encoding="utf-8") as file:
        prompts = [line.strip() for line in file if line.strip()]

    print(f"Prompts {len(prompts)} ක් හමු විය. Images සැදීම ආරම්භ කරමි...")

    # පින්තූර සුරැකීමට images නමින් folder එකක් සෑදීම
    os.makedirs("images", exist_ok=True)

    for i, prompt in enumerate(prompts, start=1):
        print(f"Generating image {i}...")
        
        # URL එකට ගැලපෙන ලෙස prompt එක සැකසීම
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Pollinations AI URL (API key අවශ්‍ය නොවේ)
        url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # post(1).webp, post(2).webp ලෙස නම ලබා දී save කිරීම
                file_name = f"images/post({i}).webp"
                with open(file_name, 'wb') as img_file:
                    img_file.write(response.content)
                print(f"✅ {file_name} සාර්ථකව save කරන ලදී.")
            else:
                print(f"❌ Image {i} සෑදීමේදී දෝෂයක්: {response.status_code}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
