# Inspired in https://www.instagram.com/p/CC2vRqbAnqB/

import instaloader

mod = instaloader.InstaLoader()

a = input("Enter The User Name --> ")

mod.download_profile(a, profile_pic_only=True)
