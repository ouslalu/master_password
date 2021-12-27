import yagmail

receiver = "olalekanusmanhassan@gmail.com"
body = ["Microphone Check"]
yag = yagmail.SMTP(user="lokousmanhas@gmail.com", password="Bolalo123#")
yag.send(
    to=receiver,
    subject="my password reset",
    contents=body
)