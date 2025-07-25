filenames = [
    "IMG_3827.PNG",
    "final_resume_realv3.docx",
    "untitled-22.psd",
    "asd213!.pdf",
    "notes_final_REALLYFINAL.txt",
    "chaos1.JPG",
    "weird$$file(name).mp3",
    "Screenshot_2021-08-04.png",
    "resume-copy(2).docx",
    "pic_final_for_real_THISONE.jpg"
]

folder = "files_to_rename"

import os
os.makedirs(folder, exist_ok=True)

for name in filenames:
    with open(os.path.join(folder, name), "w") as f:
        f.write("")  # empty file
