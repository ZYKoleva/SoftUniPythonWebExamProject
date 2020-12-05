import os


def clean_up_image_files(ad):
    ad_images = [ad.image_one, ad.image_two, ad.image_three, ad.image_four, ad.image_five, ad.image_six, ad.image_seven, ad.image_eight, ad.image_nine, ad.image_ten]
    for img in ad_images:
        if img:
            os.remove(img.path)