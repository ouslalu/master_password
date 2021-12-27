import yagmail

receiver = "xyz@gmail.com"
body = ["Microphone Check"]
yag = yagmail.SMTP(user="", password="")
yag.send(
    to=receiver,
    subject="my password reset",
    contents=body
)
