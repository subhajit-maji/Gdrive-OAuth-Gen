# 🚀 Generate Google Drive token.pickle, Client ID, Client Secret & Refresh Token

This guide explains how to generate a valid **Google OAuth 2.0 token (`token.pickle`)** and extract:

- ✅ Client ID  
- ✅ Client Secret  
- ✅ Refresh Token  

using **Android (Termux)** after Google’s new OAuth 2.0 security policy update.

These credentials can be used for:
- Cloudflare SecretX Index
- Drive OAuth scripts
- Google Drive API automation

---

## 🔗 Official References

- Google OAuth 2.0  
  https://developers.google.com/identity/protocols/oauth2  

- Google Drive API  
  https://developers.google.com/drive/api/v3/about-sdk  

- OAuth Client Credentials Guide  
  https://developers.google.com/workspace/guides/create-credentials  

- Termux (official)  
  https://f-droid.org/en/packages/com.termux/  

- Cloudflare Workers  
  https://developers.cloudflare.com/workers/  

- OAuth Native App Flow  
  https://developers.google.com/identity/protocols/oauth2/native-app  

- Refresh Token Docs  
  https://developers.google.com/identity/protocols/oauth2#offline  

- Google OAuth Security Policy  
  https://support.google.com/cloud/answer/9110914  

- Google OAuth Safety Update  
  https://developers.googleblog.com/2022/02/making-oauth-flows-safer.html  

---

## 🟢 Step 1: Install Termux

Download **Termux only from F-Droid** (Play Store version is deprecated):

👉 https://f-droid.org/en/packages/com.termux/

---

## 🟢 Step 2: Update packages & install dependencies

Open Termux and run:

```bash
apt update && apt upgrade -y
pkg install -y git python python-cryptography
pip install --upgrade pip
```

Install Google OAuth libraries:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

---

## ⚠️ Fix error: Installing pip is forbidden

If you get:

```
ERROR: Installing pip is forbidden
```

Run:

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python
```

Then reinstall libraries:

```bash
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

Reference:  
https://pip.pypa.io/en/stable/installation/

---

## 🟢 Step 3: Grant storage permission

```bash
termux-setup-storage
```

If it fails, allow manually:

Settings → Apps → Termux → Permissions → Storage

Reference:  
https://wiki.termux.com/wiki/Internal_and_external_storage  

---

## 🟢 Step 4: Create working directory

Create a folder:

```
/sdcard/SM
```

Then:

```bash
cd /sdcard/SM
```

---

## 🟢 Step 5: Clone repository

```bash
git clone https://github.com/subhajit-maji/Gdrive-OAuth-Gen
cd Gdrive-OAuth-Gen
```

---

## 🟢 Step 6: Create OAuth Client ID (IMPORTANT)

Go to Google Cloud Console:

👉 https://console.cloud.google.com/

1. Create a new project  
2. Enable **Google Drive API**  
3. APIs & Services → Credentials  
4. Create OAuth Client ID  
5. Application type: **Desktop App**  
6. Download `credentials.json`

Official guide:  
https://developers.google.com/workspace/guides/create-credentials  

Move file to:

```
/sdcard/SM/Gdrive-OAuth-Gen/credentials.json
```

⚠️ Do NOT store on external SD card.

---

## 🟢 Step 7: Generate token.pickle

Run:

```bash
python3 generate_drive_token.py
```

A URL appears like:

```
https://accounts.google.com/o/oauth2/auth?...
```

Open it in browser → Login → Allow permissions.

You’ll see:

> The authentication flow has completed. You may close this window.

OAuth native flow reference:  
https://developers.google.com/identity/protocols/oauth2/native-app  

---

## 🟢 Step 8: token.pickle created

File location:

```
/sdcard/SM/Gdrive-OAuth-Gen/token.pickle
```

This file stores encrypted OAuth credentials.

---

## 🟢 Step 9: Extract Client ID, Client Secret & Refresh Token

Run:

```bash
python3 unlock_token.py
```

Output will show:

- Client ID  
- Client Secret  
- Refresh Token  

Refresh token documentation:  
https://developers.google.com/identity/protocols/oauth2#offline  

---

## 🟢 Step 10: Use in Cloudflare SecretX Index

Paste these into your Cloudflare Worker script:

- Client ID  
- Client Secret  
- Refresh Token  

Cloudflare Workers docs:  
https://developers.cloudflare.com/workers/  

Drive Index reference:  


---

## 🔐 Security Notes

❌ Never share `credentials.json` or `token.pickle`  
🔑 Refresh tokens give full Google Drive access  
🧪 Keep OAuth app in **Testing mode** for personal use  
🛑 Do not upload tokens to GitHub  

Google OAuth security policy:  
https://support.google.com/cloud/answer/9110914  

---

## ✅ Why this works after Google OAuth update

Because it uses:

- Desktop OAuth Client  
- Loopback redirect (localhost)  
- Official `google-auth` library  
- No deprecated OOB flow  

Google announcement:  
https://developers.googleblog.com/2022/02/making-oauth-flows-safer.html  

---

## 🎉 Result

You successfully generate:

- ✅ token.pickle  
- ✅ Client ID  
- ✅ Client Secret  
- ✅ Refresh Token  
- ✅ Cloudflare SecretX Index working  

---

## 📄 License

For educational and personal use only.  
Follow Google and Cloudflare Terms of Service.
